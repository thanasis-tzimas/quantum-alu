from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

a = QuantumRegister(2, 'a')
b = QuantumRegister(2, 'b')
anc = QuantumRegister(9, 'anc')
cr = ClassicalRegister(4, 'c')
qc = QuantumCircuit(a, b, anc, cr)

qc.ccx(a[0], b[0], anc[0])
qc.ccx(a[0], b[1], anc[1])
qc.ccx(a[1], b[0], anc[2])
qc.ccx(a[1], b[1], anc[3])
qc.cx(anc[1], anc[4])
qc.cx(anc[2], anc[5])
qc.cx(anc[3], anc[7])
qc.ccx(anc[4], anc[5], anc[6])
qc.cx(anc[4], anc[5])
qc.ccx(anc[6], anc[7], anc[8])
qc.cx(anc[6], anc[7])

qc.barrier(a, b)

qc.draw(output='mpl', style='iqp',
        filename='bit_mul.pdf')
