from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library import MCMT
from qiskit.circuit.library.standard_gates import CXGate
from qiskit import transpile, execute
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

p = QuantumRegister(1, 'p')
q = QuantumRegister(1, 'q')
eq = QuantumRegister(1, 'p=q')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(p, q, eq, cr)

qc.cx(p, q)
qc.x(q)

qc.append(MCMT(CXGate(), 1, 1), [q, eq])
qc.x(q)
qc.barrier(p, q, eq)
qc.measure(p, cr[0])
qc.measure(q, cr[1])
qc.measure(eq, cr[2])

qc.draw(output='mpl', style='iqp', filename='eq.pdf')

sim = Aer.get_backend('qasm_simulator')
qct = transpile(qc, sim)
result = execute(qct, sim).result()
plot_histogram(result.get_counts(), filename='eqhist.pdf')
