from qiskit import QuantumCircuit

# Init a circuit with 2 qbits and 0 classic bits
circuit = QuantumCircuit(3, 0)

# Carry = A and B
circuit.ccx(0, 1, 2)
# Sum = A xor B
circuit.cx(0, 1)
# This an optional operation
# This un-does the last CX opeation
# on qubit B, returning it to its
# initial state
circuit.cx(0, 1)

# Draw the circuit
circuit.draw(output="mpl", filename="diagrams/half-adder.png")
