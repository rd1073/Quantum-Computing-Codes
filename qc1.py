import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 


# Function to create a quantum circuit with specified number of qubits
def create_quantum_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits)
    # Example: Apply H gate to all qubits to create a superposition state
    for qubit in range(num_qubits):
        qc.h(qubit)
    return qc

# Function to print the quantum circuit and its state
def display_quantum_circuit_and_state(qc):
    # Print the quantum circuit
    print("Quantum Circuit:")
    print(qc)

    # Get the statevector
    statevector = Statevector.from_instruction(qc)

    # Print the state in matrix form
    print("\nStatevector (matrix form):")
    print(statevector.data)

    # Render the state in LaTeX form
    print("\nStatevector (LaTeX form):")
    #display(latex_drawer(statevector))
    print(state_drawer(statevector))


    # Visualize the state using Bloch spheres
    print("\nBloch Sphere Visualization:")
    plot_bloch_multivector(statevector).show()
    plt.show()


    # Visualize the state using state city plot
    print("\nState City Visualization:")
    plot_state_city(statevector).show()
    plt.show()

# Main code
num_qubits = 3  # Change this to initialize with different number of qubits
qc = create_quantum_circuit(num_qubits)
display_quantum_circuit_and_state(qc)
