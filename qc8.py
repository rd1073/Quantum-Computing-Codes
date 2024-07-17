'''Create Bell states and perform circuit analysis'''

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


def create_bell_state_circuit():
    q = QuantumRegister(2, 'q')
    c = ClassicalRegister(2, 'c')
    circ = QuantumCircuit(q, c)

    # Create a Bell state
    circ.h(q[0])  # Apply Hadamard gate on q[0]
    circ.cx(q[0], q[1])  # Apply CNOT gate on q[0] and q[1]

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


bell_circuit = create_bell_state_circuit()
print("Bell State Quantum Circuit:")
print(bell_circuit)

analyze_circuit(bell_circuit)

# Simulate the Bell state circuit
simulate_circuit(bell_circuit)

# Analyze the Bell state circuit
