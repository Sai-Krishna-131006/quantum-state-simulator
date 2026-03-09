# Quantum State Simulator

This project is a simple Python-based simulator designed to explore mathematical foundations of a single qubit in quantum mechanics.
It implements fundamental concepts such as quantum state representation, measurement of states using born rule, expectation values of observables, and Bloch vector visualization.

This demonstrates how qubit states are represented in Hilbert space and how measurements and observables are computed through operator formalism.

## Implemented Comcepts

The simulator currently demonstrates the following fundamental concepts
• Quantum state representation using complex vectors  
• State normalization (⟨ψ|ψ⟩ = 1)  
• Measurement probabilities using the **Born rule**  
• Projection operators for measurement  
• Expectation values of observables  
• Pauli operators (X, Y, Z)  
• Density matrix representation for pure states  
• Bloch vector representation of a qubit  
• Simulation of repeated quantum measurements

---

## Mathematical Background

A qubit is represented as a complex vector:
ψ = (a, b)
where `a` and `b` are probability amplitudes.

The normalization condition is:
⟨ψ|ψ⟩ = 1

Measurement probabilities are calculated using the Born rule:
P(n) = ⟨ψ|(|n⟩⟨n|)|ψ⟩

Expectation value of an observable A is given by:
⟨A⟩ = ⟨ψ|A|ψ⟩

These equations form the foundation of quantum measurement theory.

---

## Visualization

The simulator provides graphical visualization of:

• Measurement probabilities  
• Bloch vector representation of the qubit state  

These visualizations help interpret the geometric structure of qubit states.

---

## Project Structure
quantum-state-simulator
├── main.py
├── states.py
├── operators.py
├── measurement.py
├── visualization.py
├── experiment.py
├── requirements.txt
└── README.md

---

## Installation

Clone the repository:
  git clone https://github.com/Sai-Krishna-131006/quantum-state-simulator.git

Install dependencies:
  pip install -r requirements.txt

Run the simulator:
  python main.py


---

## Purpose of the Project

The goal of this project is to build an understanding of qubit systems by directly implementing the mathematical formalism of quantum mechanics.

Instead of relying on large quantum computing frameworks (like Qiskit, Cirq, PennyLane), the simulator focuses on demonstrating the foundational linear algebra behind quantum states, measurements, and observables.

---

## Future Extensions

This project will serve as a foundation for exploring more advanced quantum phenomena, including:

• Time evolution of quantum states  
• Two-level quantum systems  
• Rabi oscillations  
• Time-dependent perturbation theory  
• Quantum gate operations  
• Multi-qubit systems  

These extensions will build on the current implementation of state vectors and operator-based measurements.

---

## Libraries Used

• NumPy  
• Matplotlib
