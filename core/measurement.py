import numpy as np

def measurement_probabilities(psi, zero, one):
    """Compute measurement probabilities for |0> and |1>."""
    P0 = zero @ np.conjugate(zero.T)
    P1 = one @ np.conjugate(one.T)

    p0 = (np.conjugate(psi.T) @ P0 @ psi).real.item()
    p1 = (np.conjugate(psi.T) @ P1 @ psi).real.item()

    return p0, p1

def expectation_value(psi, operator):
    """Compute expectation value ⟨ψ|A|ψ⟩."""
    value = (np.conjugate(psi.T) @ operator @ psi).real.item()
    return value