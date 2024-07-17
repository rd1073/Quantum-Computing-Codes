'''Applying CNOT gate on the state |00>, |01>, |10>, |11>,
 print the quantum circuit and states (matrix form, latex form), Visualize using Bloch sphere'''

import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 


def QC(num_qubits, state):
    qc = QuantumCircuit(num_qubits)

    if state == '01':
        qc.x(1)
    elif state == '10':
        qc.x(0)
    elif state == '11':
        qc.x(0)
        qc.x(1)
 
    # Apply the CNOT gate with qubit 0 as control and qubit 1 as target
    qc.cx(0, 1)

    print(f"Quantum Circuit for initial state |{state}>:")
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

states = ['00', '01', '10', '11']
for state in states:
    QC(num_qubits, state)

