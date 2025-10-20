# Bondad del Ajuste y demostración del cumplimiento de hipótesis

## Riqueza de la distribución de la probabilidad prevista

¿Qué distribución elegir? ¿Cómo de bueno es el ajuste de cada
distribución?\
La **bondad de ajuste** de un modelo estadístico describe cómo de bien
se ajusta un conjunto de observaciones. Las medidas de bondad resumen la
discrepancia entre los valores observados y los valores esperados en el
modelo de estudio. *(Bondad o goodness debería haber sido traducido como
Riqueza)*\
Para poder concluir si una distribución dada se ajusta a un conjunto de
datos, y poder dar un valor cuantitativo a dicho ajuste, se suelen
utilizar principalmente los siguientes test:

-   Test de Kolmogorov-Smirnov (K-S)

-   Test de Chi cuadrado o $X^2$ de Pearson *(el más utilizado)*

-   Test de Anderson-Darling (AD), Shapiro-Wilk, Jarque-Bera

-   Criterio de Información de Akaike (AIC), BIC \...

### Test de Kolmogorov-Smirnov

El test de **Kolmogorov-Smirnov** o K-S permite medir el grado de
concordancia existente entre la distribución de un conjunto de datos y
una distribución teórica específica.\
Si el valor del test K-S es pequeño o el p-value es alto, no podemos
rechazar la hipótesis de que las distribuciones de las dos muestras son
las mismas.\
En **scipy.Stats** se dispone de la función **`st.kstest()`** con los
siguientes argumentos:

-   **x**: la muestra a validar

-   **cdf**: el nombre de la distribución en formato string

-   **args**: los parámetros de la distribución (si los disponemos)

Y que devuelven los siguientes 2 valores:

-   statistic: El valor del estadístico K-S

-   pvalue

Ejemplo de calculo del estadistico K-S con el fichero \"siniestros.xls\"
del Ejercicio 07_02:

### Test de Chi cuadrado o $X^{2}$ de Pearson

La Chi-cuadrada o $X^{2}$ permite conocer las diferencias entre una
distribución de **frecuencias observadas** y otra **esperada o
teórica**. Se utiliza para realizar contrastes de bondad de ajuste, de
homogeneidad y de independencia cuando los tamaños muestrales son
grandes.\
Cuanto mayor sea el valor de $X^{2}$, la hipótesis se encuentra más
alejada del valor correcto. Por tanto, cuanto más se aproxima a cero el
valor de chi-cuadrado, más ajustadas están ambas distribuciones.\
En scipy se dispone de la función
**`st.chisquare(f_obs, f_exp, ddof=0, axis=0)`**

El estadístico $R^2$ es la parte de variabilidad que es explicada por el
modelo. Mientras más pequeños sean los residuos, mayor será el
estadístico $R^2$.

### Test de Anderson-Darling

El test **Anderson-Darling** prueba la hipótesis nula de que una muestra
se extrae de una población que sigue una distribución determinada.\
Este test funciona para distribuciones normales, exponenciales,
logísticas o Gumbel (Extreme Value Type I): *norm, expon, logistic,
gumbel, gumbel_l, gumbel_r*\
SciPy dispone de la función **`st.anderson(x, dist=’norm’)`**

Si el estadístico es mayor que estos valores críticos para el nivel de
significación correspondiente, se puede rechazar la hipótesis nula de
que los datos proceden de la distribución elegida.

### Test de Shapiro-Wilk

La prueba **Shapiro-Wilk** prueba la hipótesis nula de que los datos se
extrajeron de una distribución normal.\
**`st.shapiro(x)`** realiza la prueba de normalidad de Shapiro-Wilk.
Devuelve el **valor del estadístico** y el **p-value**.\
El test de Shapiro-Wilk posee mayor potencia que el resto de test de
ajuste a una normal, especialmente cuando disponemos de pocos datos.

Con este p-valor no rechazamos la hipótesis nula de normalidad. Esto es,
en la muestra hay evidencia de que proceda de una distribución normal.

### Test de Jarque-Bera

La prueba de **Jarque-Bera** comprueba si los datos de la muestra tienen
la asimetría y la curtosis correspondientes a una **distribución
normal**.\
La prueba de bondad de ajuste de Jarque-Bera con los datos de la muestra
se realiza con la función **`st.jarque_bera(x)`**.\
Devuelve, igual que la función anterior, el **valor del estadístico** y
el **p-value**. Esta prueba sólo funciona para un número suficiente de
muestras de datos ($>$`<!-- -->`{=html}2000), ya que la estadística de
la prueba tiene una distribución asintótica de Chi-cuadrado con 2 grados
de libertad.\
Ejemplo de realizar el test J-B a dos distribuciones generadas
aleatoriamente (la primera Normal y la segunda Rayleith):

## Gráfica Q-Q

Una vez seleccionada nuestra distribución candidata a validar, para
reforzar nuestra hipótesis y obtener una mayor fiabilidad se puede
mostrar la gráfica conocida como **quantil-quantil** (*quantile-quantile
plot*, gráfico Q-Q o qqplot).\
Consiste en una comparación visual entre las funciones de distribución
teórica (cuantiles teoricos) y los datos extraídos de la muestra
ordenados. Si los datos están visualmente superpuestos, se puede
concluir que ambas distribuciones se comportan de igual manera.\
Tanto **scipy.stats** como **stasmodels** disponen de funciones para
realizar, junto con matplotlib, los gráficos Q-Q:

-   **`scipy.stats.probplot(sample, dist=st.`*`distribucion`*`, plot=plt)`**

-   **`statsmodels.api.qqplot(sample, dist=’norm’, line=’s’)`**

Ejemplo usando **scipy.stats** y la función **`.probplot()`**:

![image](../SESION_07_STATS/images/Figure_2.png)

Ejemplo usando **statsmodels.api** y la función **`.qqplot()`**:

![image](../SESION_07_STATS/images/Figure_3.png)

### Requisitos para parámetros específicos en Solvencia II {#requisitos-para-parámetros-específicos-en-solvencia-ii .unnumbered}

*\"Las entidades aseguradoras calcularán el capital de solvencia
obligatorio directamente a partir de la **distribución de probabilidad
prevista** generada por su modelo interno, utilizando la medida del
valor en riesgo establecida en el artículo 74.1 de la Ley 20/2015, de 14
de julio.\"* (art. 85. RDOSSEAR).

-   No se establece ningún método concreto para calcular la distribución
    de probabilidad prevista para los modelos internos (art. 121.4
    Directiva y art. 84. RDOSSEAR), sino usar prácticas de mercado
    generalmente aceptadas.

-   En el caso de **parámetros propios de empresa**, estos deben ser
    calculados con los métodos estandarizados usados para el mercado,
    incluyendo los supuestos de distribución probabilística. Así, para
    el cálculo de la **desviación típica** especifica de la empresa, se
    usará el MSEP (Error Cuadrático Medio de Predicción) de una
    **distribución ajustada a una lognormal**. (anexo XVII Reglamento
    Delegado).

### Requisitos para modelos internos en Solvencia II {#requisitos-para-modelos-internos-en-solvencia-ii .unnumbered}

-   *\"La **distribución de probabilidad prevista** subyacente al modelo
    interno asignará probabilidades a las variaciones del importe de los
    fondos propios básicos de la empresa de seguros o reaseguros o de
    otros importes, como las pérdidas y ganancias, siempre que estos
    importes puedan utilizarse para determinar las variaciones de los
    fondos propios básicos.\"* (art. 228 Reglamento Delegado).

-   Las técnicas actuariales **adecuadas, aplicables y pertinentes**
    quedan reguladas en el art. 229 del RD. Destacando, entre otros, los
    siguientes requisitos:

    -   que las técnicas se basen en información actual y \[\...\] se
        tengan en cuenta el progreso en la **ciencia actuarial** y las
        prácticas de mercado generalmente aceptadas

    -   que la empresa de seguros tenga un conocimiento detallado de la
        teoría económica y actuarial, así como de las hipótesis
        subyacentes

    -   que las **técnicas** estén **adaptadas** a los datos utilizados
        en el modelo interno

    -   que los resultados del modelo interno no incluyan un **error de
        modelo** o un error **de estimación** significativos; cuando sea
        posible, la distribución de probabilidad prevista se ajustará
        para tener en cuenta los errores de modelo y de estimación

    -   que el cálculo de los resultados del modelo interno pueda
        presentarse de **forma transparente**

## Video nº 12 {#video-nº-12 .unnumbered}

::: casopractico
Video nº 12 Video 12
:::
