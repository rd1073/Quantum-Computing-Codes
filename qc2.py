import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 


def QC(num_qubits):
    qc = QuantumCircuit(num_qubits)

    # The default state is |0> for both qubits, so we only need to set the second qubit to |1>
    qc.x(1)  # Apply X gate to the second qubit to set it to |1>
 
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
