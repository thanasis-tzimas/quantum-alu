from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

input = QuantumRegister(2, 'I')
sel = QuantumRegister(1, 'S')
anc = QuantumRegister(3, 'anc')
cr = ClassicalRegister(1, 'c')
qc = QuantumCircuit(input, sel, anc, cr)

qc.ccx(input[1], sel, anc[0])
qc.x(anc[0])
qc.ccx(input[0], anc[0], anc[1])
qc.x(anc[0])
qc.x(anc[1])
qc.ccx(anc[0], anc[1], anc[2])
qc.x(sel)

qc.barrier(input, sel)
qc.measure(sel, cr)

qc.draw(output='mpl', style='iqp',
        filename='mux.pdf')
