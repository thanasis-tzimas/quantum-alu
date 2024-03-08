from qiskit import QuantumCircuit, QuantumRegister

from qiskit.circuit.library.arithmetic.adders.adder import Adder

class SimpleRippleCarryAdder(Adder):
    
    def __init__(
        self, num_state_qubits: int, name="SimpleRippleCarryAdder"
    ) -> None:
        """A simple ripple carry adder, based on the 
        classic implementation of the ripple carry adder.

        Args:
            num_state_qubits (int): The number of qubits in either input register for
                state :math:`|a>` or :math:`|b>`. The two input
                registers must have the same number of qubits.
            name (str, optional): The name of the circuit object.
        Raises:
            ValueError: If ``num_state_qubits`` is lower than 1.
        """
        if num_state_qubits < 1:
            raise ValueError("The number of qubits must be at least 1.")
        
        super().__init__(num_state_qubits, name=name)
        
        qr_a = QuantumRegister(num_state_qubits, name="a")
        qr_b = QuantumRegister(num_state_qubits, name="b")
        qr_c = QuantumRegister(num_state_qubits, name="cin")
        qr_z = QuantumRegister(1, name="cout")

        self.add_register(qr_c, qr_a, qr_b, qr_z)

        circuit = QuantumCircuit(*self.qregs, name=name)

        # build ripple-carry adder circuit
        for i in range(num_state_qubits - 1):
            circuit.ccx(qr_a[i], qr_b[i], qr_z)
            circuit.cx(qr_a[i], qr_b[i])
            circuit.ccx(qr_b[i], qr_c[i], qr_z)
            circuit.cx(qr_b[i], qr_c[i])
            circuit.cx(qr_a[i], qr_b[i])
            if i+1 < num_state_qubits:
                circuit.swap(qr_z, qr_c[i+1])
        
        self.append(circuit.to_gate(), self.qubits)
        