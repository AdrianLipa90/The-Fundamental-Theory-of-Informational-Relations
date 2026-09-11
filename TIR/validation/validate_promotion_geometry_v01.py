from __future__ import annotations
import numpy as np


def J(d: int) -> np.ndarray:
    I = np.eye(d)
    Z = np.zeros_like(I)
    return np.block([[Z, -I], [I, Z]])


def realify(M: np.ndarray) -> np.ndarray:
    M = np.asarray(M, dtype=complex)
    return np.block([[M.real, -M.imag], [M.imag, M.real]])


def promotion(alpha: complex, beta: complex, d: int) -> np.ndarray:
    if not np.isclose(abs(alpha) ** 2 + abs(beta) ** 2, 1.0, atol=1e-12):
        raise ValueError("non-normalized promotion")
    return np.vstack([alpha * np.eye(d), beta * np.eye(d)])


def qgt(P: np.ndarray, dmu: np.ndarray, dnu: np.ndarray) -> complex:
    Q = np.eye(P.shape[0], dtype=complex) - P @ P.conj().T
    return complex(np.trace(dmu.conj().T @ Q @ dnu))


def main() -> int:
    checks = []
    P = promotion(1 / np.sqrt(2), 1j / np.sqrt(2), 2)
    checks.append(("metric", np.allclose(P.conj().T @ P, np.eye(2), atol=1e-12)))
    RP = realify(P)
    checks.append(("J_intertwiner", np.allclose(J(4) @ RP, RP @ J(2), atol=1e-12)))

    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    checks.append(("local_gate_intertwiner", np.allclose(np.kron(np.eye(2), H) @ P, P @ H, atol=1e-12)))

    Pbell = promotion(1 / np.sqrt(2), 1 / np.sqrt(2), 2)
    CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)
    bell = CNOT @ Pbell @ np.array([1,0], dtype=complex)
    checks.append(("bell", np.allclose(bell, np.array([1,0,0,1]) / np.sqrt(2), atol=1e-12)))
    checks.append(("segre", np.isclose(abs(bell[0]*bell[3]-bell[1]*bell[2]), 0.5, atol=1e-12)))

    theta, phi = 1.123, -0.456
    c, s, phase = np.cos(theta/2), np.sin(theta/2), np.exp(1j*phi)
    p = np.array([[c],[phase*s]], dtype=complex)
    dt = np.array([[-0.5*s],[0.5*phase*c]], dtype=complex)
    dp = np.array([[0],[1j*phase*s]], dtype=complex)
    qtt, qpp, qtp = qgt(p,dt,dt), qgt(p,dp,dp), qgt(p,dt,dp)
    checks.append(("FS_theta", np.isclose(qtt.real, 0.25, atol=1e-12)))
    checks.append(("FS_phi", np.isclose(qpp.real, 0.25*np.sin(theta)**2, atol=1e-12)))
    checks.append(("Berry", np.isclose(qtp.imag, 0.25*np.sin(theta), atol=1e-12)))

    for name, ok in checks:
        print(f"{name}: {'PASS' if ok else 'FAIL'}")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
