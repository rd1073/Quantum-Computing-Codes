from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np
from qiskit_aer import Aer


def here(n):
    qc=QuantumCircuit(n)

    for q in range(n):
        qc.h(q)

    print("Quantu circuit")
    print(qc)

    statevector=Statevector.from_instruction(qc)

    print("Matrix form")
    print(statevector.data)

    print("Latex form")
    print(state_drawer(statevector))


    print("Block sphere")
    plot_bloch_multivector(statevector)
    plt.show()

    print("State city")
    plot_state_city(statevector)
    plt.show()



here(3)