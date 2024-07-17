''' Create and simulate the multi qubit gates'''

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer, plot_histogram
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def create_multi_qubit_circuit():
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(3, 'c')
    circ = QuantumCircuit(q, c)

    # Apply multi-qubit gates
    circ.h(q[0])  # Apply Hadamard gate on q[0]
    circ.cx(q[0], q[1])  # Apply CNOT gate with q[0] as control and q[1] as target
    circ.ccx(q[0], q[1], q[2])  # Apply Toffoli (CCX) gate with q[0] and q[1] as controls and q[2] as target
    
    circ.measure(q, c)
    
    return circ

def simulate_circuit(circuit):
    # Remove the measurement operations for statevector simulation
    circuit_no_measure = circuit.remove_final_measurements(inplace=False)
    
    statevector = Statevector.from_instruction(circuit_no_measure)

    print("Statevector (Matrix Form):")
    print(statevector.data)

    print("Statevector (LaTeX Form):")
    print(state_drawer(statevector, output='latex'))

    print("Bloch Sphere Visualization:")
    plot_bloch_multivector(statevector)
    plt.show()

def analyze_circuit(circuit):
    depth = circuit.depth()
    width = circuit.width()
    size = circuit.size()
    single_qubit_gates = circuit.num_nonlocal_gates()
    two_qubit_gates = circuit.num_tensor_factors()

    print("\nCircuit Analysis:")
    print(f"Depth: {depth}")
    print(f"Width: {width}")
    print(f"Size: {size}")
    print(f"Number of single-qubit gates: {single_qubit_gates}")
    print(f"Number of two-qubit gates: {two_qubit_gates}")

# Create the multi-qubit gate circuit
multi_qubit_circuit = create_multi_qubit_circuit()
print("Multi-Qubit Gate Quantum Circuit:")
print(multi_qubit_circuit)

# Simulate the multi-qubit gate circuit
simulate_circuit(multi_qubit_circuit)

# Analyze the multi-qubit gate circuit
analyze_circuit(multi_qubit_circuit)
