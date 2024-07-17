import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 


def QC(num_qubits):
    qc = QuantumCircuit(num_qubits)

 # Initialize the qubits to |0> and |1>
    qc.x(1)  # Apply X gate to the second qubit to set it to |1>

    # Apply Pauli and Hadamard gates
    qc.x(0)  # Apply Pauli-X gate to the first qubit
    qc.y(1)  # Apply Pauli-Y gate to the second qubit
    qc.z(0)  # Apply Pauli-Z gate to the first qubit
    qc.h(1)  # Apply Hadamard gate to the second qubit
 
    print("Quantum Circuit:")
    print(qc)

    # Get the statevector
    statevector = Statevector.from_instruction(qc)

    # Print the state in matrix form
    print("\nStatevector (matrix form):")
    print(statevector.data)

    # Render the state in LaTeX form
    print("\nStatevector (LaTeX form):")
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
num_qubits = 3  
QC(num_qubits)
