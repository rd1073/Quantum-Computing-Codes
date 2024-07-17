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
        display(latex_drawer(statevector))
    except ImportError:
        pass  # Ignore if LaTeX rendering module not available
    
    print("\nBloch Sphere Visualization:")
    plot_bloch_multivector(statevector)
    plt.show()