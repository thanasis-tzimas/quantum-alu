from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

a = QuantumRegister(1, 'a')
b = QuantumRegister(1, 'b')
carry_in = QuantumRegister(1, 'carry_in')
carry_out = QuantumRegister(1, 'carry_out')
sel = QuantumRegister(1, 'select')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(sel, a, b, carry_in, carry_out, cr)

qc.cx(sel, b)
qc.ccx(a, b, carry_in)
qc.cx(a, b)
qc.ccx(b, carry_in, carry_out)
qc.cx(b, carry_in)
qc.cx(a, b)

qc.barrier(b, carry_in, carry_out)
qc.measure(carry_out, cr[0])
qc.measure(carry_in, cr[1])
qc.measure(b, cr[2])

qc.draw(output='mpl', style='iqp',
        filename='full_sub.pdf')
