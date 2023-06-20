from qiskit import QuantumCircuit

# Init a circuit with 4 qubits
circuit = QuantumCircuit(4, 0)

circuit.ccx(0, 1, 2)
circuit.cx(0, 1)
circuit.ccx(1, 2, 3)
circuit.cx(1, 2)
# Optional operation
circuit.cx(0, 1)

print(circuit.draw('text'))
