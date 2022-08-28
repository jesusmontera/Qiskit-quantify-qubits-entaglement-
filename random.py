from qiskit import QuantumCircuit
import qiskit.quantum_info as qi
from qiskit import Aer
from qiskit.providers.aer.library import SaveStatevector
from qiskit.compiler import transpile
import numpy as np
import matplotlib.pyplot as plt
from Entagleclass import EntagleClass



def InsertSaveStates(qc,nq):
    num_qubits = qc.num_qubits
    pos=1
    nIns=len(qc.data)
    
    for i in range(nIns):
        _inst = SaveStatevector(nq, label = 'psi_' + str(i))
        qc.data.insert(pos, [_inst, qc.qubits, None])
        pos+=2
    nIns=len(qc.data)
    
    
    
        
def printInstrucciones(qc):
    nInstrucs=len(qc.data)
    print("\nINSTRUCCIONES " , nInstrucs)
    for i in range(nInstrucs):
        tupi=qc.data[i]
        print(tupi[0])
        sq="Qubits : "
        for k in range(len(tupi[1])):
            sq+=str(tupi[1][k].index)+ " "
        print(sq)

def printProbabilies(sv):
    
    dic = sv.probabilities_dict()
    i=0
    total=0
    print("\nProbabilities\n")
    for key, value in dic.items():
        if value>0:
            total +=  value            
            print(i, ") ",key, ' : ', np.round(value*100,3), " %")
        i+=1
    print("total= ", np.round(total*100,3), " %")


nq=5
nstates=int(2**nq)
simulator = Aer.get_backend('aer_simulator')
qc = QuantumCircuit(nq)
##qc.h(0)
##qc.cx(0,1)
##qc.ry(np.pi/4,1)
##qc.x(0)



sv = qi.random_statevector(nstates)
qc.initialize(sv)

for d in range(20):
    qc=qc.decompose()

qc = transpile(qc, simulator)
InsertSaveStates(qc,nq )
#printInstrucciones(qc)


job = simulator.run(qc,shots=100)
res = job.result()


objentagle= EntagleClass(nq)


for i in range (int(len(qc.data)/2)):
    svsaved=res.data(0)['psi_'+str(i)]
    posInstruc=i*2
    tupi=qc.data[posInstruc]
    si=str(i+1) + ") " +  tupi[0].name + " ( "    
    for k in range(len(tupi[1])):
        si+=str(tupi[1][k].index)
        if k < len(tupi[1]) -1 : si +=' , '
    print(si + ")")
        
    objentagle.calc_QC_SVentagle(qc,posInstruc,svsaved)
    print (objentagle.GetEntagleString(True))
print("ENTRELAZAMINTO AL FINAL SOLO CON statvector.dictionary")    
objentagle.calcSVentagle(svsaved)
print (objentagle.GetEntagleString(True))
##printProbabilies(svsaved)

#qc.draw(output='mpl',scale =0.4)    
#plt.show()

#printInstrucciones(qc)
#printProbabilies(qc)




