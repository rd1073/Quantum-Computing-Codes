'''Grovers Algorithm'''

from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np
from qiskit_aer import Aer, AerSimulator

def initialize_s(qc, qubits):
    """Apply a Hadamard gate to all qubits in the list."""
    for q in qubits:
        qc.h(q)
    return qc

def oracle(qc, qubits):
    """Apply the oracle to mark the solution state |101⟩."""
    qc.cz(qubits[0], qubits[2])
    return qc

def diffuser(qc, qubits):
    """Apply the diffuser circuit."""
    # Apply H-gates to all qubits
    for q in qubits:
        qc.h(q)
    # Apply X-gates to all qubits
    for q in qubits:
        qc.x(q)
    # Apply multi-controlled-Z gate
    qc.h(qubits[2])
    qc.cx(qubits[0], qubits[2])
    qc.h(qubits[2])
    # Apply X-gates again
    for q in qubits:
        qc.x(q)
    # Apply H-gates again
    for q in qubits:
        qc.h(q)
    return qc

def grover_algorithm(num_iterations=1):
    # Define the number of qubits
    n = 3
    
    # Create quantum circuit with n qubits and n classical bits
    qc = QuantumCircuit(n, n)
    
    # Define the qubits to use
    qubits = [0, 1, 2]
    
    # Initialize all qubits to superposition
    initialize_s(qc, qubits)
    
    # Define the number of iterations for Grover's algorithm
    for _ in range(num_iterations):
        # Apply the oracle
        oracle(qc, qubits)
        
        # Apply the diffuser
        diffuser(qc, qubits)
    
    # Measure the qubits
    qc.measure(qubits, qubits)
    
    return qc

def simulate_circuit(circuit, shots=1024):
    """Simulates the given quantum circuit using the Aer simulator and returns the result."""
    simulator = AerSimulator()
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit).result()
    counts = result.get_counts()
    return counts

def plot_results(counts):
    """Plots the results in a histogram."""
    plot_histogram(counts)
    plt.title("Grover's Algorithm")
    plt.show()

def main():
    # Define the number of iterations for Grover's algorithm
    num_iterations = 1
    
    # Run Grover's algorithm
    grover_circuit = grover_algorithm(num_iterations)
    
    # Simulate the circuit
    counts = simulate_circuit(grover_circuit)
    
    # Plot the results
    plot_results(counts)

if __name__ == "__main__":
    main()
