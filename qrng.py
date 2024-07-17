
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit,  transpile
from qiskit.compiler import assemble
#from qiskit.tools.jupyter import *
from qiskit.visualization import plot_bloch_multivector, plot_state_city, state_drawer
from qiskit_aer import Aer, AerSimulator

import matplotlib.pyplot as plt
import numpy as np
print("All libraries imported successfully!")


def real_map(value, leftMin, leftMax, rightMin, rightMax):
    # Calculate the spans of the input and output ranges
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Scale the value to the 0-1 range
    valueScaled = (value - leftMin) / leftSpan

    # Map the value to the output range
    mappedValue = rightMin + (valueScaled * rightSpan)

    return mappedValue


def QRandom(a, b):
    qubits = 3  # Set the number of qubits to 3
    q = QuantumRegister(qubits, 'q')
    circ = QuantumCircuit(q)
    c0 = ClassicalRegister(qubits, 'c0')
    circ.add_register(c0)

    for i in range(qubits):
        circ.h(q[i])

    for i in range(qubits):
        circ.measure(q[i], c0[i])

    backend = Aer.get_backend('statevector_simulator')
    job = transpile(circ, backend)
    result = job.result()
    
    output = result.get_statevector(circ, decimals=5)

    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(len(output)):
        if abs(output[i]) != 0:
            n1 = i
            n2 = np.real(output[i])
            n3 = np.imag(output[i])

    y = real_map(n1 + n2 + n3, -qubits, len(output) - 1 + qubits, a, b)
    plot_state_city(output)
    return y

x = []
for i in range(100):
    x.append(QRandom(0, 100))
    print(str(i) + ": " + str(QRandom(0, 100)))

plt.plot(x)
plt.show()





def QRandom(a, b):
    qubits = 6  # Set the number of qubits to 6
    q = QuantumRegister(qubits, 'q')
    circ = QuantumCircuit(q)
    c0 = ClassicalRegister(qubits, 'c0')
    circ.add_register(c0)

    for i in range(qubits):
        circ.h(q[i])

    for i in range(qubits):
        circ.measure(q[i], c0[i])

    backend = Aer.get_backend('statevector_simulator')
    job = transpile(circ, backend)
    result = job.result()
    output = result.get_statevector(circ, decimals=5)

    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(len(output)):
        if abs(output[i]) != 0:
            n1 = i
            n2 = np.real(output[i])
            n3 = np.imag(output[i])

    y = real_map(n1 + n2 + n3, -qubits, len(output) - 1 + qubits, a, b)
    plot_state_city(output)
    return y

x = []
for i in range(100):
    x.append(QRandom(0, 100))
    print(str(i) + ": " + str(QRandom(0, 100)))
plt.plot(x)
plt.show()



def QRandom(a, b):
    qubits = 5  # Set the number of qubits to 5
    q = QuantumRegister(qubits, 'q')
    circ = QuantumCircuit(q)
    c0 = ClassicalRegister(qubits, 'c0')
    circ.add_register(c0)

    for i in range(qubits):
        circ.h(q[i])

    for i in range(qubits):
        circ.measure(q[i], c0[i])

    backend = Aer.get_backend('statevector_simulator')
    job = transpile(circ, backend)
    result = job.result()
    output = result.get_statevector(circ, decimals=5)

    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(len(output)):
        if abs(output[i]) != 0:
            n1 = i
            n2 = np.real(output[i])
            n3 = np.imag(output[i])

    y = real_map(n1 + n2 + n3, -qubits, len(output) - 1 + qubits, a, b)
    plot_state_city(output)
    return y

x = []
for i in range(100):
    x.append(QRandom(0, 100))
    print(str(i) + ": " + str(QRandom(0, 100)))
plt.plot(x)
plt.show()