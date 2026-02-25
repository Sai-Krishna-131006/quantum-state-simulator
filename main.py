import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Basis States
# -----------------------------
def computational_basis():
    zero = np.array([[1], [0]], dtype=complex)
    one = np.array([[0], [1]], dtype=complex)
    return zero, one


# -----------------------------
# Normalize State
# -----------------------------
def normalize_state(psi):
    norm = np.sqrt(np.conjugate(psi.T) @ psi)
    return psi / norm


# -----------------------------
# Measurement Probabilities
# -----------------------------
def measurement_probabilities(psi, zero, one):
    P0 = zero @ np.conjugate(zero.T)
    P1 = one @ np.conjugate(one.T)

    prob0 = (np.conjugate(psi.T) @ P0 @ psi).real.item()
    prob1 = (np.conjugate(psi.T) @ P1 @ psi).real.item()

    return prob0, prob1


# -----------------------------
# Visualization
# -----------------------------
def plot_probabilities(prob0, prob1):
    states = ['|0>', '|1>']
    probs = [prob0, prob1]

    plt.bar(states, probs)
    plt.ylim(0, 1)
    plt.title("Measurement Probabilities")
    plt.ylabel("Probability")
    plt.show()


# -----------------------------
# Main Execution
# -----------------------------
def main():
    zero, one = computational_basis()

    # Create arbitrary state
    psi = np.array([[3], [4]], dtype=complex)

    # Normalize
    psi = normalize_state(psi)

    print("Normalized state:")
    print(psi)

    # Compute probabilities
    prob0, prob1 = measurement_probabilities(psi, zero, one)

    print("Probability of |0>:", prob0)
    print("Probability of |1>:", prob1)
    print("Sum:", prob0 + prob1)

    # Plot
    plot_probabilities(prob0, prob1)


if __name__ == "__main__":
    main()