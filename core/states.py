import numpy as np

def basis_states():
    """Return computational basis states |0> and |1>."""
    zero = np.array([[1],[0]], dtype=complex)
    one = np.array([[0],[1]], dtype=complex)
    return zero, one

def normalize_state(psi):
    """Normalize a quantum state vector."""
    norm = np.sqrt(np.conjugate(psi.T) @ psi)
    return psi / norm

def density_matrix(psi):
    """Construct density matrix ρ = |ψ><ψ| for a pure state."""
    return psi @ np.conjugate(psi.T)