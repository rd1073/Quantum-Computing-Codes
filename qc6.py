'''Proving various circuit identities, print the quantum circuit and states 
(matrix form, latex form), Visualize using Bloch sphere
'''
import numpy as np
from qiskit import QuantumCircuit,  transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit_aer import Aer
 



def display_circuit_identity(qc, description):
    print(f"Quantum Circuit: {description}")
    print(qc)
    
    statevector = Statevector.from_instruction(qc)
    
    print("\nStatevector (matrix form):")
    print(statevector.data)
    
    # Render the state in LaTeX form (if applicable)
    try:
        print("\nStatevector (LaTeX form):")
        print(state_drawer(statevector))
    except ImportError:
        pass  # Ignore if LaTeX rendering module not available
    
    print("\nBloch Sphere Visualization:")
    plot_bloch_multivector(statevector)
    plt.show()

    print("\nState City Visualization:")
    plot_state_city(statevector)
    plt.show()


def hadamard_identity(num_qubits):
    # H * H = I
    qc = QuantumCircuit(num_qubits)
    for q in range(num_qubits):
        qc.h(q)
        qc.h(q)
    
    display_circuit_identity(qc, f"Hadamard Identity (H * H = I, {num_qubits} qubits)")

def cnot_identity(num_qubits):
    # CNOT * CNOT = I
    qc = QuantumCircuit(num_qubits)
    for q in range(num_qubits - 1):
        qc.cx(q, q + 1)
        qc.cx(q, q + 1)
    
    display_circuit_identity(qc, f"CNOT Identity (CNOT * CNOT = I, {num_qubits} qubits)")

def swap_gate_identity(num_qubits):
    # SWAP using three CNOT gates
    qc = QuantumCircuit(num_qubits)
    for qubit in range(num_qubits - 1):
        qc.cx(qubit, qubit + 1)
        qc.cx(qubit + 1, qubit)
        qc.cx(qubit, qubit + 1)
    
    display_circuit_identity(qc, f"SWAP Gate Identity using CNOT gates ({num_qubits} qubits)")

# Main code
num_qubits = 3  # Change this to test with different number of qubits
hadamard_identity(num_qubits)
cnot_identity(num_qubits)
swap_gate_identity(num_qubits)