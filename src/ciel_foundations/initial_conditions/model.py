from dataclasses import dataclass

@dataclass
class InitialCondition:
    potential: float
    chaos: float
    seed: float = 0.0
    winding: int = 0
    memory: float = 0.0
