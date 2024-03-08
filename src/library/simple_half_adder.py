from qiskit.circuit import Gate
from qiskit import QuantumCircuit, QuantumRegister

class SimpleHalfAdder(QuantumCircuit):
    def __init__(
        self, name="SimpleHalfAdder"
    ) -> None:
        """A simple half adder circuit based on the classic
        implementation of the half adder digital circuit.

        Args:
            name (str, optional): The name of the circuit object.
        """
        super().__init__(name=name)

        qr_a = QuantumRegister(1, name="a")
        qr_b = QuantumRegister(1, name="b")
        qr_c = QuantumRegister(1, name="cout")

        self.add_register(qr_a, qr_b, qr_c)

        circuit = QuantumCircuit(*self.qregs, name=name)

        # build half adder circuit
        circuit.ccx(qr_a, qr_b, qr_c)
        circuit.cx(qr_a, qr_b)

        pass