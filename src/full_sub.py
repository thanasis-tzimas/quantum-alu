from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

a = QuantumRegister(1, 'a')
b = QuantumRegister(1, 'b')
carry = QuantumRegister(1, 'carry')
anc = QuantumRegister(1, 'ancilla')
sel = QuantumRegister(1, 'select')
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(sel, a, b, carry, anc, cr)

qc.cx(sel, b)
qc.ccx(a, b, carry)
qc.cx(a, b)
qc.ccx(b, carry, anc)
qc.cx(b, carry)
qc.cx(a, b)

# TODO: put a barrier and measure
qc.barrier(b, carry)
qc.measure(carry, cr[0])
qc.measure(b, cr[1])

qc.draw(output='mpl', style='iqp',
        filename='full_sub.pdf')
