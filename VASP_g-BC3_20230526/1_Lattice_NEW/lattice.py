import os
from typing import OrderedDict
import numpy as np
import matplotlib.pyplot as plt

File = open(r"LATTICE.dat","r")
Lines = File.readlines()

Data = [[],[]]
for i in range(len(Lines)):
    Line = Lines[i].strip("\n").split()
    Data[0].append(float(Line[0]))
    Data[1].append(float(Line[1]))

order = 4
Coeff=np.polyfit(Data[0],Data[1],order)
poly=np.poly1d(Coeff)

crit = poly.deriv().r
r_crit = crit[crit.imag==0].real
test = poly.deriv(2)(r_crit) 
x_min = r_crit[test>0]
y_min = poly(x_min)
tmp_minY=y_min[0]
tmp_minX=x_min[0]

if(len(x_min)>1):
    for i in range(len(x_min)):
        if(y_min[i]<tmp_minY):
            tmp_minY=y_min[i]
            tmp_minX=x_min[i]
print(tmp_minX,tmp_minY)

X=np.linspace(min(Data[0]),max(Data[0]),100)

plt.xlabel("Lattice Constant ($\AA$)",fontsize = 12)
plt.ylabel("Energy (eV)", fontsize = 12)
plt.scatter(Data[0],Data[1],marker = "o",label="Calculated values")
plt.plot(X,poly(X),label=f"Fitted polynomial of order: {order}")
plt.scatter(tmp_minX,tmp_minY,marker="x",s=100,linewidth=2,label=f"Minimum energy at: {round(tmp_minX,6)} $\AA$")

plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("",format="pdf")
