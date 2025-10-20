import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Siniestros = [461210, 518830, 574390, 690200, 706580, 740550, 763660, 804950]
Primas = [482880, 546620, 591390, 690240, 707440, 751330, 791320, 848870]

datos = pd.DataFrame(data=Siniestros, columns=['Siniestros'])
datos['Primas'] = Primas
print(datos)

modelo = st.linregress(datos.Primas, datos.Siniestros)
print(modelo)

coef = modelo.slope
intercept = modelo.intercept
error_estandar = modelo.stderr
p_valor = modelo.pvalue
print(error_estandar, p_valor)

plt.style.use('ggplot')
plt.scatter(Primas, Siniestros, color='c')
x = np.linspace(min(Primas),max(Primas),500)
y = coef * x + intercept
plt.plot(x, y)
plt.show()