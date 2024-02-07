from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

a = QuantumRegister(1, 'a')
b = QuantumRegister(1, 'b')
carry = QuantumRegister(1, 'carry')
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(a, b, carry, cr)

qc.ccx(a, b, carry)
qc.cx(a, b)

qc.barrier(b, carry)
qc.measure(carry, cr[0])
qc.measure(b, cr[1])

qc.draw(output='mpl', style='iqp', filename='half_add.pdf')
