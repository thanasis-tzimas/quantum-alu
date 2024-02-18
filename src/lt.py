from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

p = QuantumRegister(1, 'p')
q = QuantumRegister(1, 'q')
gt = QuantumRegister(1, 'p>q')
cr = ClassicalRegister(1, 'c')
qc = QuantumCircuit(p, q, gt, cr)

qc.x(p)
qc.ccx(p, q, gt)
qc.x(p)

qc.barrier(p, q, gt)
qc.measure(gt, cr)

qc.draw(output='mpl', style='iqp', filename='lt.pdf')
