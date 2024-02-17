from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library import MCMT
from qiskit.circuit.library.standard_gates import CXGate

digits: int = 4
p = QuantumRegister(digits, 'p')
q = QuantumRegister(digits, 'q')
eq = QuantumRegister(1, 'p=q')
cr = ClassicalRegister(1, 'c')
qc = QuantumCircuit(p, q, eq, cr)

for i in range(digits):
    qc.cx(p[i], q[i])
    qc.x(q[i])

qc.append(MCMT(CXGate(), 1, 1), [q, eq])
qc.barrier(eq)
qc.measure(eq, cr)

qc.draw(output='mpl', style='iqp', filename='eq.pdf')
