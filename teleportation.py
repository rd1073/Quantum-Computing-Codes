from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer

def create_bell_pair(qc, a, b):
    """Creates a Bell pair between qubits a and b."""
    qc.h(a)     # Apply Hadamard gate to qubit 'a'
    qc.cx(a, b) # Apply CNOT gate with 'a' as control and 'b' as target
    return qc

def alice_gates(qc, psi, a):
    """Applies gates on Alice's side to 'psi' and 'a'."""
    qc.cx(psi, a)
    qc.h(psi)
    return qc

def measure_and_send(qc, psi, a):
    """Measures qubits 'psi' and 'a', and sends the classical result to Bob."""
    qc.measure(psi, 0)
    qc.measure(a, 1)
    return qc

def bob_gates(qc, qubit, crz, crx):
    """Applies gates on Bob's side based on the classical bits he received."""
    # Apply conditional gates
    qc.x(qubit).c_if(crx, 1) # Apply X gate if crx == 1
    qc.z(qubit).c_if(crz, 1) # Apply Z gate if crz == 1
    return qc

def quantum_teleportation():
    # Create quantum circuit with 3 qubits and 2 classical bits
    q = QuantumRegister(3, name='q') # Qubit shared between Alice and Bob
    c0 = ClassicalRegister(1, name='c0') # Classical bit for qubit 'psi' measurement
    c1 = ClassicalRegister(1, name='c1') # Classical bit for qubit 'a' measurement
    qc = QuantumCircuit(q, c0, c1)

    # Step 1: Create entangled Bell pair between Alice and Bob
    create_bell_pair(qc, 1, 2)
    
    # Step 2: Prepare the qubit to be teleported ('psi')
    qc.h(0) # Apply Hadamard gate to qubit 'psi'
    
    # Step 3: Alice applies her gates
    alice_gates(qc, 0, 1)
    
    # Step 4: Alice measures qubits 'psi' and 'a', and sends classical bits to Bob
    measure_and_send(qc, 0, 1)
    
    # Step 5: Bob applies his gates based on the classical bits
    bob_gates(qc, 2, c0, c1)
    
    return qc

def simulate_teleportation(circuit):
    """Simulates the quantum teleportation circuit."""
    simulator = AerSimulator()
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit).result()
    counts = result.get_counts()
    return counts

def plot_results(counts):
    """Plots the measurement results in a histogram."""
    plot_histogram(counts)
    plt.title("Quantum Teleportation Results")
    plt.show()

def main():
    # Create and simulate the quantum teleportation circuit
    teleportation_circuit = quantum_teleportation()
    counts = simulate_teleportation(teleportation_circuit)
    
    # Plot the results
    plot_results(counts)

if __name__ == "__main__":
    main()
