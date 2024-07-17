'''Circuit analysis (circuit depth, width, size, no. of single qubit gates, two qubit gates etc), 
print the quantum circuit and states (matrix form, latex form), Visualize using Bloch sphere
'''
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Function to analyze and visualize the quantum circuit
def analyze_and_visualize_circuit(qubits):
    q = QuantumRegister(qubits, 'q')
    c = ClassicalRegister(qubits, 'c')
    circ = QuantumCircuit(q, c)

    # Apply some gates to the circuit
    for i in range(qubits):
        circ.h(q[i])
    circ.cx(q[0], q[1])
    circ.cx(q[1], q[2])
    
    # Print the quantum circuit
    print("Quantum Circuit:")
    print(circ)

    # Get circuit depth, width, and size
    depth = circ.depth()
    width = circ.width()
    size = circ.size()
    single_qubit_gates = circ.num_nonlocal_gates()
    two_qubit_gates = circ.num_tensor_factors()

    # Print circuit analysis
    print("\nCircuit Analysis:")
    print(f"Depth: {depth}")
    print(f"Width: {width}")
    print(f"Size: {size}")
    print(f"Number of single-qubit gates: {single_qubit_gates}")
    print(f"Number of two-qubit gates: {two_qubit_gates}")

    # Create a separate circuit for statevector simulation without measurement
    state_circ = QuantumCircuit(q)
    for i in range(qubits):
        state_circ.h(q[i])
    state_circ.cx(q[0], q[1])
    state_circ.cx(q[1], q[2])

    # Simulate the statevector
    circuit_no_measure = circ.remove_final_measurements(inplace=False)
    
    statevector = Statevector.from_instruction(circuit_no_measure)
    

    # Print the statevector in matrix form
    print("\nStatevector (Matrix Form):")
    print(statevector.data)

    # Print the statevector in LaTeX form
    print("\nStatevector (LaTeX Form):")
    print(state_drawer(statevector, output='latex'))

    # Visualize the state using a Bloch sphere
    print("\nBloch Sphere Visualization:")
    plot_bloch_multivector(statevector)
    plt.show()

# Run the function with 3 qubits
analyze_and_visualize_circuit(3)
