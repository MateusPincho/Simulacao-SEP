import numpy as np
import math

pi = math.pi

#Parametros da carga em serie
Rf = 4 #Ohm
Xf = 0.38 #Ohm
Zf = complex(Rf,Xf) #Ohm

#Parametros das impedancias 1 e 2 dos transformadores
Rt1 = 7.6e-3 #Ohm
Xt1 = 3.8e-3 #Ohm
Zt1 = complex(Rt1,Xt1) #Ohm

Rt2 = 33.9e-3 #Ohm
Xt2 = 0.85e-3 #Ohm
Zt2 = complex(Rt2,Xt2) #Ohm

#Parametros das admitancias dos transformadores
Rm1 = 4320 #Ohm
Xm1 = -5050 #Ohm
Ym1 = complex((1/Rm1),(1/Xm1)) #S

Rm2 = 432000 #Ohm
Xm2 = -505000 #Ohm
Ym2 = complex((1/Rm2),(1/Xm2)) #S

Rm3 = 402000 #Ohm
Xm3 = -607000 #Ohm
Ym3 = complex((1/Rm3),(1/Xm3)) #S

#Parametros das linhas de transmissao
RLT = 0.172 #Ohm
LLT = 2.18e-3 #Henry
CLT = 0.0136e-6 #Faraday

ZLT80 = 80*complex(RLT,2*pi*60*LLT) #Ohm
YLT80 = 80*complex(0, 2*pi*60*CLT) #S

ZLT100 = 100*complex(RLT,2*pi*60*LLT) #Ohm
YLT100 = 100*complex(0, 2*pi*60*CLT) #S

ZLT120 = 120*complex(RLT, 2*pi*60*LLT) #Ohm
YLT120 = 120*complex(0, 2*pi*60*CLT) #S

#Parametros das cargas em derivacao
Rc1 = 8000 #Ohm
Lc1 = -41 #Henry
Zc1 = complex((Rc1),(2*pi*60*Lc1)) #S
Yc1 = 1/Zc1

Rc2 = 1350.55 #Ohm
Lc2 = -7.83 #Henry
Yc2 = complex((Rc2),(2*pi*60*Lc2)) #S


Rc3 = 649 #Ohm
Lc3 = -3.2 #Henry
Yc3 = complex((1/Rc3),(1/2*pi*60*Lc3)) #S

#Matriz da carga em serie
Carga_Serie = ([[1, Zf], [0, 1]])

#Matrizes dos transformadores
T1 = np.array([[(69/500)*(1+Ym1*Zt1), (500/69)*(Zt1+Zt2+Ym1*Zt1*Zt2)], [(69/500)*Ym1, (500/69)*(1+Ym1*Zt2)]])
T2 = np.array([[(500/230)*(1+Ym2*Zt1), (230/500)*(Zt1+Zt2+Ym2*Zt1*Zt2)], [(500/230)*Ym2, (230/500)*(1+Ym2*Zt2)]])
T3 = np.array([[(230/69)*(1+Ym3*Zt1), (69/230)*(Zt1+Zt2+Ym3*Zt1*Zt2)], [(230/69)*Ym3, (69/230)*(1+Ym3*Zt2)]])

#Matrizes das linhas de transmissao
LT1 = np.array([[(YLT80/2)*(ZLT80)+1, ZLT80], [((4*YLT80)+(ZLT80)*(YLT80**2))/4, 1+((ZLT80*YLT80)/2)]])
LT2 = np.array([[(YLT80/2)*(ZLT80)+1, ZLT80], [((4*YLT80)+(ZLT80)*(YLT80**2))/4, 1+((ZLT80*YLT80)/2)]])
LT3 = np.array([[(YLT80/2)*(ZLT80)+1, ZLT80], [((4*YLT80)+(ZLT80)*(YLT80**2))/4, 1+((ZLT80*YLT80)/2)]])

LT4= np.array([[(YLT120/2)*(ZLT120)+1, ZLT120], [((4*YLT120)+(ZLT120)*(YLT120**2))/4, 1+((ZLT120*YLT120)/2)]])
LT5 = np.array([[(YLT120/2)*(ZLT120)+1, ZLT120], [((4*YLT120)+(ZLT120)*(YLT120**2))/4, 1+((ZLT120*YLT120)/2)]])

LT6 = np.array([[(YLT100/2)*(ZLT100)+1, ZLT100], [((4*YLT100)+(ZLT100)*(YLT100**2))/4, 1+((ZLT100*YLT100)/2)]])

#Matrizes das cargas em derivacao
Carga1 = np.array([[1, 0], [Yc1, 1]])

Carga2 = np.array([[1, 0], [Yc2, 1]])

Carga3 = np.array([[1, 0], [Yc3, 1]])

#Paralelo das linhas 1 e 2

PLT12 = np.array([[((LT1[0,0]*LT2[0,1])+(LT2[0,0]*LT1[0,1])/(LT1[0,1]+LT2[0,1])), (LT1[0,1]*LT2[0,1])/(LT1[0,1]+LT2[0,1])], [(LT1[1,0]+LT2[1,0]+((LT1[0,0]-LT2[0,0])*(LT2[1,1]-LT1[1,1])))/(LT1[0,1]+LT2[0,1]), ((LT2[0,1]*LT1[1,1])+(LT1[0,1]*LT2[1,1]))/(LT1[0,1]+LT2[0,1])]])



#Cascata dos quadripólos

Cascata1 = np.matmul(Carga_Serie,T1)
Cascata2 = np.matmul(Cascata1,PLT12)
Cascata3 = np.matmul(Cascata2,Carga1)
Cascata4 = np.matmul(Cascata3,LT3)
Cascata5 = np.matmul(Cascata4,T2)
Cascata6 = np.matmul(Cascata5,Carga2)
Cascata7 = np.matmul(Cascata6,LT4)
Cascata8 = np.matmul(Cascata7,T3)
Cascata_Final = np.matmul(Cascata8,Carga3)

print(Yc1)