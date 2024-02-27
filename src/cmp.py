from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

sel = QuantumRegister(1, 's')
p = QuantumRegister(1, 'p')
q = QuantumRegister(1, 'q')
cmp = QuantumRegister(1, 'cmp')
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(sel, p, q, cmp, cr)

qc.x(sel)
qc.cx(sel, p)
qc.x(sel)
qc.cx(sel, q)
qc.ccx(p, q, cmp)
qc.x(sel)
qc.cx(sel, p)
qc.x(sel)
qc.cx(sel, q)

qc.barrier(sel, p, q, cmp)
qc.measure(sel, cr[0])
qc.measure(cmp, cr[1])

qc.draw(output='mpl', style='iqp', filename='cmp.pdf')
