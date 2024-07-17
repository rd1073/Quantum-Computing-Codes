'''Deutsch ALgorithm'''

from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer import Aer, AerSimulator

def deutsch_oracle(circuit, qubits, constant):
    """Applies the Deutsch oracle to the given circuit.
    
    Args:
        circuit (QuantumCircuit): The quantum circuit to which the oracle will be applied.
        qubits (list): The list of qubits to be used.
        constant (bool): If True, the oracle is constant. If False, the oracle is balanced.
    """
    if constant:
        # Apply identity operation (oracle does nothing)
        pass
    else:
        # Apply CNOT gate (balanced function)
        circuit.cx(qubits[0], qubits[1])

def deutsch_algorithm(constant):
    """Implements the Deutsch algorithm.
    
    Args:
        constant (bool): If True, the oracle is constant. If False, the oracle is balanced.
    """
    # Create a quantum circuit with 2 qubits and 1 classical bit
    qc = QuantumCircuit(2, 1)
    
    # Apply Hadamard gates to both qubits
    qc.h(0)
    qc.h(1)
    
    # Apply the oracle
    deutsch_oracle(qc, [0, 1], constant)
    
    # Apply Hadamard gate to the first qubit again
    qc.h(0)
    
    # Measure the first qubit
    qc.measure(0, 0)
    
    return qc

def simulate_circuit(circuit):
    """Simulates the given quantum circuit using the Aer simulator and returns the result.
    
    Args:
        circuit (QuantumCircuit): The quantum circuit to be simulated.
    """
    simulator = AerSimulator()
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit).result()
    counts = result.get_counts()
    
    return counts

def main():
    # Create and simulate the Deutsch algorithm circuit for a constant function
    constant_circuit = deutsch_algorithm(constant=True)
    constant_counts = simulate_circuit(constant_circuit)
    
    # Create and simulate the Deutsch algorithm circuit for a balanced function
    balanced_circuit = deutsch_algorithm(constant=False)
    balanced_counts = simulate_circuit(balanced_circuit)
    
    # Plot the results
    print("Constant function results:")
    print(constant_counts)
    plot_histogram(constant_counts)
    plt.title("Constant Function")
    plt.show()
    
    print("Balanced function results:")
    print(balanced_counts)
    plot_histogram(balanced_counts)
    plt.title("Balanced Function")
    plt.show()

if __name__ == "__main__":
    main()
