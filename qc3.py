'''Pauli's gates an Hadamard hate'''
import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 


def QC(num_qubits):
    qc = QuantumCircuit(num_qubits)

 # Initialize the qubits to |0> and |1>
    '''qc.x(1)  # Apply X gate to the second qubit to set it to |1>

    # Apply Pauli and Hadamard gates
    qc.x(0)  # Apply Pauli-X gate to the first qubit
    qc.y(1)  # Apply Pauli-Y gate to the second qubit
    qc.z(0)  # Apply Pauli-Z gate to the first qubit
    qc.h(1) '''
    qc.x(1)

# Apply Pauli gates and Hadamard gate to the first qubit
    qc.x(0)  # Apply X gate to qubit 0
    qc.y(0)  # Apply Y gate to qubit 0
    qc.z(0)  # Apply Z gate to qubit 0
    qc.h(0)  # Apply Hadamard gate to qubit 0

    # Apply Pauli gates and Hadamard gate to the second qubit
    qc.x(1)  # Apply X gate to qubit 1
    qc.y(1)  # Apply Y gate to qubit 1
    qc.z(1)  # Apply Z gate to qubit 1
    qc.h(1) # Apply Hadamard gate to the second qubit
 
    print("Quantum Circuit:")
    print(qc)

    # Get the statevector
    statevector = Statevector.from_instruction(qc)

    # Print the state in matrix form
    print("\nStatevector (matrix form):")
    print(statevector.data)

    # Render the state in LaTeX form
    print("\nStatevector (LaTeX form):")
    #print(statevector, output="latex")
    #print(qc.draw(output='latex'))


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
