import numpy as np
from core.states import basis_states, normalize_state, density_matrix
from core.operators import pauli_x, pauli_y, pauli_z
from core.measurement import measurement_probabilities, expectation_value
from visualization import plot_probabilities, plot_bloch, plot_experiment
from experiments.experiment import simulate_measurements


def main():

    zero, one = basis_states()

    # Example state
    psi = np.array([[3],[4]], dtype=complex)

    psi = normalize_state(psi)

    print("Normalized State:")
    print(psi)

    # Measurement probabilities
    p0, p1 = measurement_probabilities(psi, zero, one)

    print("Probability of |0>:", p0)
    print("Probability of |1>:", p1)

    # Simulated experiment
    count0, count1 = simulate_measurements(p0, p1)

    print("Measurement simulation (1000 shots):")
    print("|0> count:", count0)
    print("|1> count:", count1)

    # Pauli operators
    X = pauli_x()
    Y = pauli_y()
    Z = pauli_z()

    # Expectation values
    exp_x = expectation_value(psi, X)
    exp_y = expectation_value(psi, Y)
    exp_z = expectation_value(psi, Z)

    print("Expectation <X>:", exp_x)
    print("Expectation <Y>:", exp_y)
    print("Expectation <Z>:", exp_z)

    # Density matrix
    rho = density_matrix(psi)
    print("Density Matrix:")
    print(rho)

    # Visualization
    plot_probabilities(p0, p1)
    plot_bloch(exp_x, exp_y, exp_z)
    plot_experiment(count0, count1)


if __name__ == "__main__":
    main()