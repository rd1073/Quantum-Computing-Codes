'''5. Phase kickback, print the quantum circuit and states (matrix form, latex form), 
Visualize using Bloch sphere
'''

import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 


def QC(num_qubits):
    qc = QuantumCircuit(num_qubits)

    qc.h(0)
    
    # Apply Controlled-Z (CZ) gates between the first qubit and all other qubits
    for i in range(1, num_qubits):
        qc.cz(0, i)
    
    # Apply Hadamard gate again to the first qubit
    qc.h(0)
 
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
num_qubits = 2
QC(num_qubits)
