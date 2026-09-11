from __future__ import annotations

import numpy as np


LEVELS = {
    1: ("H", 2, 4, "CP^1"),
    2: ("O", 4, 8, "CP^3"),
    3: ("S_16", 8, 16, "CP^7"),
    4: ("A_32", 16, 32, "CP^15"),
}


def J(dim_complex: int) -> np.ndarray:
    eye = np.eye(dim_complex)
    zero = np.zeros_like(eye)
    return np.block([[zero, -eye], [eye, zero]])


def realify(matrix: np.ndarray) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=complex)
    return np.block([[matrix.real, -matrix.imag], [matrix.imag, matrix.real]])


def promotion(alpha: complex, beta: complex, dim_old: int) -> np.ndarray:
    if not np.isclose(abs(alpha) ** 2 + abs(beta) ** 2, 1.0, atol=1e-12):
        raise ValueError("non-normalized promotion")
    eye = np.eye(dim_old, dtype=complex)
    return np.vstack([alpha * eye, beta * eye])


def cnot(qubits: int, control: int, target: int) -> np.ndarray:
    if control == target:
        raise ValueError("control and target must differ")
    dim = 2**qubits
    out = np.zeros((dim, dim), dtype=complex)
    for col in range(dim):
        bits = [(col >> (qubits - 1 - q)) & 1 for q in range(qubits)]
        if bits[control]:
            bits[target] ^= 1
        row = 0
        for bit in bits:
            row = (row << 1) | bit
        out[row, col] = 1.0
    return out


def ghz_target(qubits: int) -> np.ndarray:
    state = np.zeros(2**qubits, dtype=complex)
    state[0] = 1 / np.sqrt(2)
    state[-1] = 1 / np.sqrt(2)
    return state


def build_ghz(qubits: int) -> np.ndarray:
    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    state = h @ np.array([1, 0], dtype=complex)
    for n in range(2, qubits + 1):
        state = promotion(1.0, 0.0, state.size) @ state
        state = cnot(n, control=n - 1, target=0) @ state
    return state


def main() -> int:
    checks: list[tuple[str, bool]] = []

    checks.append((
        "hierarchy",
        list(LEVELS.values()) == [
            ("H", 2, 4, "CP^1"),
            ("O", 4, 8, "CP^3"),
            ("S_16", 8, 16, "CP^7"),
            ("A_32", 16, 32, "CP^15"),
        ],
    ))

    phase = 0.371
    for qubits, dim in ((1, 2), (2, 4), (3, 8)):
        p = promotion(1 / np.sqrt(2), np.exp(1j * phase) / np.sqrt(2), dim)
        checks.append((f"metric_{qubits}Q", np.allclose(p.conj().T @ p, np.eye(dim), atol=1e-12)))
        rp = realify(p)
        checks.append((f"J_{qubits}Q", np.allclose(J(2 * dim) @ rp, rp @ J(dim), atol=1e-12)))

    for qubits in (2, 3, 4):
        for control in range(qubits):
            for target in range(qubits):
                if control == target:
                    continue
                gate = cnot(qubits, control, target)
                checks.append((
                    f"CNOT_{qubits}Q_{control}_{target}",
                    np.allclose(gate.conj().T @ gate, np.eye(2**qubits), atol=1e-12),
                ))

        state = build_ghz(qubits)
        checks.append((f"GHZ_{qubits}Q", np.allclose(state, ghz_target(qubits), atol=1e-12)))
        for split in range(1, qubits):
            rank = np.linalg.matrix_rank(
                state.reshape(2**split, 2 ** (qubits - split)),
                tol=1e-10,
            )
            checks.append((f"Schmidt_{qubits}Q_split_{split}", rank == 2))

    failed = [name for name, ok in checks if not ok]
    print(f"carrier_hierarchy_v02: {len(checks) - len(failed)}/{len(checks)} PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
