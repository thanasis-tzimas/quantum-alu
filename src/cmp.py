from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

a = QuantumRegister(1, 'a')
b = QuantumRegister(1, 'b')
eq = QuantumRegister(1, 'a=b')
lt = QuantumRegister(1, 'a<b')
gt = QuantumRegister(1, 'a>b')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(a, b, eq, lt, gt, cr)

qc.cx(a, b)
qc.cx(b, eq)
qc.cx(a, b)
qc.x(eq)
qc.x(a)
qc.ccx(a, b, lt)
qc.x(a)
qc.x(b)
qc.ccx(a, b, gt)
qc.x(b)

qc.barrier(a, b, eq, gt, lt)
qc.measure(eq, cr[0])
qc.measure(lt, cr[1])
qc.measure(gt, cr[2])

qc.draw(output='mpl', style='iqp',
        filename='cmp.pdf')
