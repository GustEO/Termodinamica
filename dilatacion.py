#!/usr/bin/env python
# coding: utf-8

# In[13]:


#llamar librerias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd


# # Barra de Cobre
# L=0.702
# Ti=21

# In[83]:


datacu=np.loadtxt('cobre.txt')
L1=0.702
Ti1=21
T1=datacu[:,0]
dT1=T1-Ti1
dL1=datacu[:,1]
datacu=pd.DataFrame(datacu)
dx1=datacu.iloc[:,:-1].values-Ti1
dy1=datacu.iloc[:,1].values

modelo =LinearRegression(fit_intercept=False)
modelo.fit(X=dx1,y=dy1)
modelo.intercept_,modelo.coef_.flatten()
m1=modelo.coef_[0]
m1


# In[63]:


#desviaciones

errox1=np.std(dT1)
errory1=np.std(dL1)


# In[84]:


plt.scatter(dT1,dL1,label='Datos')
plt.errorbar(dT1,dL1,xerr=errox1,yerr=errory1,fmt='o', capsize=2, capthick=0.5, ecolor='black')
plt.plot(dT1,m1*dT1,'r',label='Tendencia')
plt.legend()
plt.title('Grafica de dilatacion termica de una barra de Cobre')
plt.xlabel('Variacion de temperatura $\Delta T(\pm 1)\,^{\circ}C$')
plt.ylabel('Variacion de longitud $\Delta L(\pm 1e^{-6})\, m$')
ecuacion="$\Delta L=1.085e^{-6}\Delta$ T"
plt.annotate(ecuacion,(-20,0.00008))


# # Barra de Aluminio
# L=0.706
# Ti=24

# In[101]:


dataal=np.loadtxt('aluminio.txt')
L2=0.706
Ti2=24
T2=dataal[:,0]
dT2=T2-Ti2
dL2=dataal[:,1]

dataal=pd.DataFrame(dataal)
dx2=dataal.iloc[:,:-1].values-Ti2
dy2=dataal.iloc[:,1].values

modelo2 =LinearRegression(fit_intercept=False)
modelo2.fit(X=dx2.reshape(-1,1),y=dy2)
m2=modelo2.coef_[0]
m2/L2


# In[85]:


#desviaciones

errox2=np.std(dT2)
errory2=np.std(dL2)


# In[88]:


plt.scatter(dT2,dL2,label='Datos')
plt.errorbar(dT2,dL2,xerr=errox2,yerr=errory2,fmt='o', capsize=2, capthick=0.5, ecolor='black')
plt.plot(dT2,m2*dT2,'r',label='Tendencia')
plt.legend()
plt.title('Grafica de dilatacion termica de una barra de Aluminio')
plt.xlabel('Variacion de temperatura $\Delta T(\pm 1)\,^{\circ}C$')
plt.ylabel('Variacion de longitud $\Delta L(\pm 1e^{-6})\, m$')
ecuacion="$\Delta L=1.331e^{-6}\Delta$ T"
plt.annotate(ecuacion,(-20,0.0001))


# # Barra de Acero
# L=0.708
# Ti=23

# In[60]:


dataac=np.loadtxt('hierro.txt')
L=0.708
Ti=23
T=dataac[:,0]
dT=T-Ti
dL=dataac[:,1]

dataac=pd.DataFrame(dataac)
dx3=dataac.iloc[:,:-1].values-Ti
dy3=dataac.iloc[:,1].values

modelo3 =LinearRegression(fit_intercept=False)
modelo3.fit(X=dx3.reshape(-1,1),y=dy3)
m3=modelo3.coef_[0]
m3


# In[90]:


#desviaciones

errox3=np.std(dT)
errory3=np.std(dL)


# In[94]:


plt.scatter(dT,dL,label='Datos')
plt.errorbar(dT,dL,xerr=errox3,yerr=errory3,fmt='o', capsize=2, capthick=0.5, ecolor='black')
plt.plot(dT,m3*dT,'r',label='Tendencia')
plt.legend()
plt.title('Grafica de dilatacion termica de una barra de Aluminio')
plt.xlabel('Variacion de temperatura $\Delta T(\pm 1)\,^{\circ}C$')
plt.ylabel('Variacion de longitud $\Delta L(\pm 1e^{-6})\, m$')
ecuacion="$\Delta L=7.886e^{-7}\Delta$ T"
plt.annotate(ecuacion,(-20,5e-5))


# # Errores porcentuales
# 
# ## aluminio

# In[100]:


alt=2.4e-5
alexp=1.886-6
error_porcentual = abs((alexp - alt) / alt) * 100
print(f"{error_porcentual:.2f}%")


# ## Cobre

# In[102]:


cut=1.7e-7
cuexp=1.154e-6
error_porcentual = abs((cuexp - cut) / cut) * 100
print(f"{error_porcentual:.2f}%")


# ## Acero
# 

# In[103]:


act=1.2e-7
acexp=1.114e-6
error_porcentual = abs((acexp - act) / act) * 100
print(f"{error_porcentual:.2f}%")

