import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

alpha = 7.
lamdba = 0.0025
theta = 1/lamdba

# Opcion 1:
mean = alpha / lamdba
var = alpha / (lamdba ** 2)
std = np.sqrt(var)
print(mean, std)

# Opcion 2:
print(st.gamma.mean(a=alpha, scale=1/lamdba), st.gamma.std(a=alpha, scale=1/lamdba))

# Opcion 3:
siniestralidad = st.gamma(a=alpha, scale=1/lamdba)
print(siniestralidad.mean(), siniestralidad.std())

# Opcion 4: 
m, v = siniestralidad.stats('mv')
print(m,np.sqrt(v))

percentiles = (0.5, 0.9, 0.95, 0.99, 0.996, 0.998)

for i in percentiles:
	print(f'El percentil {i:.3f} teorico es {st.gamma.ppf(i, a=alpha, scale=1/lamdba):.2f}')

s = np.random.gamma(alpha, theta, size=10000)
for i in percentiles:
	# los percentiles en np.percentile van de 0 a 100
	print(f'El percentil {i:.3f} de la simulacion es {np.percentile(s, i*100):.2f}')

# Grafica:
plt.hist(s, 50, density=True)
x = np.linspace (0, 9000, 200) 
y = st.gamma.pdf(x, a=alpha, scale=1/lamdba)
plt.plot(x, y)
plt.show()
