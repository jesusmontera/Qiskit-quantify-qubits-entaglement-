# Qiskit-quantify-qubits-entaglement-
Calculate entaglement in Qiskit for each qubit with the rest in detail. Uses purity, circuit instructions and stavector dictionary. Entaglement measure from 0(not) to 1 (max), while putiry is from 0.5(max) to 1 (not).
There aer 2 files, random.py creates a 5 qubit random circuit, decompose and insert save state vectors instrucions. 
The other file, entagleclass.py calculates entaglement for each instruction:

 if purity from qubit trace is ledd than one 1.0, then it looks for the cx instructions in the circuit, and if the qubits are entagled with cx, then calculate the statevector.probabilities_dict() to get coincidences and quantify entaglement. It detects is are Positive entagled (both qubits give the same and result), or negative entagled marking the result with 'X'. For example at instruction
 105,u(0), the qubit 0 is entagled with Q1 negative(Q1X) 0.559  and  with Q2 positive 0.575 
 
 105) u ( 0)
entagle by statevector.probabilities_dict + purity + search cx
Q0 = 0.56739  purity = 0.51037 detail [ Q1X =0.559 Q2  =0.575  ]
Q1 = 0.55937  purity = 0.52229 detail [ Q0X =0.559  ]
Q2 = 0.57541  purity = 0.54689 detail [ Q0  =0.575  ]
