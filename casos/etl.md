# Importación de datos y procesos ETL con pandas

Las siglas ETL significan extraer, transformar, cargar (Extract,
Transform and Load). Es el proceso por excelencia para recopilar y unir
datos de distintas fuentes con el objeto de facilitar el estudio y
análisis de los mismos.\
Como buena práctica, se recomienda almacenar primero los datos \"en
crudo\" y transformarlos posteriormente, lo que permite repetir el
proceso periódicamente, trabajar formatos intermedios mucho más ágiles y
facilitar la limpieza sin modificar archivos originales.

## Introducción al manejo de funciones en un DataFrame de pandas

Para el análisis de datos en python, la opción más extendida es trabajar
con set de datos (llamados dataframe) en la librería de análisis de
datos por excelencia en python: **pandas**. La estructura de DataFrame
en pandas ofrece un entorno flexible y robusto para almacenar, explorar
y manipular datos con precisión.\
El dataframe es el formato estándar de información utilizado en los
proyectos de análisis de datos. A pesar de restar velocidad de cálculo
(aunque cada nueva versión de Pandas mejora este aspecto) nos ofrece una
enorme facilidad en el manejo y análisis de datos.\
Un dataframe se diferencia de una tabla SQL en que se manipula
directamente en la memoria del programa ya que no reside en un servidor
remoto.\
Son más adecuados para el análisis "offline" complejos con estadísticas,
visualización y modelos matemáticos. El límite tamaño de un dataframe lo
determina la cantidad de memoria RAM del equipo donde se ejecute.
Existen ejemplos de implementaciones con 100 millones de filas.\
Veamos cómo generar un dataframe con la instrucción
**`pd.DataFrame(data)`** usando los siguientes atributos:

-   `data`: pueden ser Series, arrays, constants

-   `index`: Por defecto será un indice autoincremental: 0, 1, 2, \....

-   `columns`: Nombre de las columnas

-   `dtype`: Si no existe, pandas deducirá el tipo. Podrán cambiarse
    posteriormente.

Si el nombre de la columna no contiene espacios, se puede hacer mención
a las columnas ya existentes de dos formas: **`df.Importe`** o
**`df[’Importe’]`**, siendo la última opción la única posible si
nombramos la columna con algún espacio en blanco.\
El motor de **pandas** incluye internamente, entre otras, las librerías
**numpy** y **dateutil**. En consecuencia, se puede acceder a funciones
de estas librerías de forma intuitiva. No obstante, es recomendable
importar NumPy para operar independientemente con Pandas ya que ambas
librerías son perfectamente compatibles.

Por ejemplo podemos calcular la media con la siguiente función sin
necesidad de importar numpy:

Los dataframe se componen de filas y columnas. Así para cualquier
cálculo (por ejemplo la suma), conviene tener en cuenta si las funciones
se aplican a la columna *(por defecto*) o a la fila.

-   `axis=0`: Lectura en horizontal. axis=0 puede cambiarse por
    `axis=’index’`

-   `axis=1`: Lectura en vertical. axis=1 equivale a `axis=’columns’`

![Estructura de un dataframe en
pandas](../SESION_04_PANDAS/images/pandas_axis.png){width="10cm"}

Veamos unos ejemplos ilustrativos partiendo del anterior dataframe,
donde sólo importando la librería pandas puedo hacer uso de funciones
embebidas de numpy:

En el siguiente ejemplo se hace uso de las funciones de numpy. Podemos
ver que ambas librerías admiten argumentos en las fórmulas:

No obstante, actualmente los argumentos internos de numpy no son
plenamente compatibles. Por ejemplo, **pandas** posee el argumento
**skipna** para ignorar los datos `NaN`, en cambio en numpy habría que
utilizar `np.nanmedian()`.

## Importación de datos a un dataframe de pandas

A la hora de trabajar con varias fuentes de información es recomendable
primero almacenar \"tal cual\" han sido obtenidos los datos (denominado
también \"en crudo\") y como paso siguiente iniciar el proceso de
transformación, análisis y procesamiento. Esta mecánica tiene varios
beneficios:

-   Registro de todos los datos \"en crudo\", sin ningún tipo de filtro,
    agregación o manipulación. Así, el proceso puede repetirse las veces
    que queramos, ya que no modificamos los datos fuentes.

-   Creación de datos intermedios en formatos más ágiles y rápidos para
    su lectura. Esto facilita la implementación de procesos de limpieza
    de datos sin modificar los ficheros originales.

-   Creación de tantos ficheros finales como fines queramos utilizarlos
    con los datos unicamente necesarios.

Pandas puede importar datos casi desde cualquier formato o base de
datos, siendo las más utilizadas:

-   **CSV**: `pd.read_csv()`

-   **Excel**: `pd.read_excel()`

-   **Parquet**: `pd.read_parquet()`

-   **Feather**: `pd.read_feather()`

-   **JSON**: `pd.read_json()`

-   **HTML**: `pd.read_html()`

-   **SQL**: `pd.read_sql()`

-   **HDF5**: `pd.read_hdf()`

-   **SAS**: `pd.read_sas()`

-   **STATA**: `pd.read_stata()`

-   **SPSS**: `pd.read_spss()`

-   **Pickle**: `pd.read_pickle()`

-   **Fixed-width**: `pd.read_fwf()`

-   **Clipboard**: `pd.read_clipboard()`

A continuación veremos las más conocidas o utilizadas.

### Importación desde texto plano (csv, txt)

Con la función **`pd.read_csv(fichero)`** puede crearse fácilmente un
dataframe partiendo de un fichero csv. También puede ser usado para leer
cualquier fichero de texto plano (conocidos como txt). Veamos cuales son
sus principales parámetros:

-   `sep`: Separador en formato *str*. Ejemplo: '`;`' o '`\t`'
    (tabulado). Por defecto '`,`'

-   `decimal`: Separador de decimales. Ejemplo: '`,`'. Por defecto '`.`'

-   `header`: *int*, número de fila donde figuran los nombres de las
    columnas.

-   `names`: *str*, Listado con los nombres a usar como cabecera del
    DataFrame.

-   `index_col`: *int*, columna a usar como Index (nombre de las filas)
    del DataFrame. `index_col=False` fuerza a pandas a no usar la
    primera columna como index.

-   `skiprows`: *int*, indica las líneas iniciales que omitimos en la
    importación

-   `skipfooter`: *int*, indica las líneas finales que omitimos en la
    importación

-   `encoding`: *str*, para indicar el formato del fichero, por ejemplo:
    utf-8 o ansi

-   `comment`: *str*, indicamos el indicador al inicio del texto para
    indicar que esa línea está comentada y no sea importada

-   `nrows`: *int*, indicamos el número de filas a importar, función muy
    util a la hora de visualizar el contenido de ficheros grandes.

-   `usecols`: *list*, indicamos exactamente qué columnas queremos
    importar

-   **Otros** [^1]: skip_blank_lines, parse_dates, compression (lee
    desde un zip), memory_map\...

### Video nº 1 A {#video-nº-1-a .unnumbered}

::: casopractico
Video Video nº 1 A
:::

### Importación desde Excel

De la misma forma, con la función **`pd.read_excel(fichero)`** se crea
un dataframe desde un fichero MS Excel. Los principales parámetros se
detallan a continuación. No obstante es recomendable consultar el
listado de argumentos en la página oficial[^2]:

-   `sheet_name`: *string, int o list*

-   `header`: *int*, número de fila con los nombres de las columnas.

-   `skiprows`: *int*, indica las primeras filas que deben ignorarse.

-   `usecols`: *int o list*, indica la columa/s a importar. Ej: 'B:C' o
    range(1,3)

-   `skipfooter`: *int*, indica las filas del final que deben ignorarse.
    Por defecto: None

-   `index_col`: columna a usar como Index del DataFrame.

-   `names`: *str*, Listado con los nombres a usar como cabecera del
    DataFrame.

Señalar que para trabajar sin ningún problema con cualquier formato o
versión de fichero Excel, es recomendable la instalación de las
siguientes librerías:

-   openpyxl

-   xlrd

-   lxml

-   xlwt

-   html5lib

-   pyxlsb

### ¿Sabias qué? {#sabias-qué .unnumbered}

::: casopractico
¿Sabias qué? ¿Sabías que es habitual que cada programador añada a cada
proyecto un fichero llamado requirements.txt donde se listan todas las
bibliotecas y dependencias necesarias para ejecutar el código? Este
archivo actúa como una \"lista de la compra\" que especifica exactamente
qué paquetes externos necesita el proyecto y, opcionalmente, sus
versiones específicas. Por ejemplo, podría incluir líneas como
pandas==2.0.0 o numpy\>=1.24.0.\
La ventaja principal es que cualquier otra persona (o tú mismo en el
futuro) puede recrear el mismo entorno de trabajo simplemente ejecutando
pip install -r requirements.txt, asegurando que el código funcione
exactamente como estaba previsto. Te dejo el link del fichero
requirements.txt utilizado para la elaboración de estas unidades:
<https://github.com/franciscogarate/cdiae/blob/main/requirements.txt>
:::

### Importación desde sql

Pandas puede conectarse fácilmente con cualquier base de datos de la
familia de SQL (SQL, MySQL, MariaDB, etc.). En este caso, y para añadir
facilidad a la hora de que cualquiera pueda replicar sin necesidad de
disponer de un servidor de SQL, vamos a realizar la conexión con una
base de datos Sqlite[^3]. No obstante, puede adaptarse el ejemplo a una
base de datos SQL más avanzada ya que la query sería compatible.

## Guardado o exportación de ficheros

El último paso del proceso de ETL es la carga o guardado de los datos
(loading). Pandas, con la misma facilidad que puede leer datos de un
fichero csv o Excel, puede exportar cualquier dataframe a múltiples
formatos con instrucciones como **`df.to_csv()`** o **`df.to_excel()`**
respectivamente.\

![DataFrame exportado a un fichero
xlsx](images/pandas_to_excel.png){width="11cm"}

Adicionalmente, existe la función **`pd.ExcelWriter`** (más avanzada)
para trabajar con pestañas dentro de un fichero Excel. No obstante, en
un proceso de manejo de base de datos, no son los formatos más
recomendados para ficheros intermedios. Aunque pandas infiere bastante
bien el formato de los campos, a la hora de ser importados los ficheros
en un proceso distinto, normalmente hay que volver a formatear y asignar
el formato que tienen dichos campos. Para evitar esto, existen formatos
como **feather** o **parquet** que conservan el formato tal y como los
hemos guardado.

## Formatos feather y parquet

Como he mencionado, no es buena práctica utilizar el mismo formato del
fichero origen (raw) sino que los datos una vez transformados vamos a
guardarlo como ficheros intermedios en un formato que conserve el tipado
de los datos.\
Así, la mejor opción para ficheros intermedios son los formatos
**Feather y Parquet** (ambos basados en Apache Arrow). Feather y Parquet
mantienen los tipos de datos originales (int64, float64, datetime,
etc.), a diferencia de CSV que convierte todo a texto.\
Veamos las principales características, así como los pros y contras de
cada uno de ellos.

### Feather {#feather .unnumbered}

El formato **Feather** es un formato de archivo binario para almacenar
datos de forma eficiente. Es un formato abierto y ligero que se utiliza
para el intercambio de datos entre aplicaciones y lenguajes de
programación.\
Es el lenguaje ideal para guardar nuestras base de datos *intermedias*
en nuestro flujo de transformaciones en python, así como para compartir
dichos ficheros con otros programas escritos en R, ya que R también lee
sin problemas el formato Feather.

### Parquet {#parquet .unnumbered}

El formato **Parquet**, en cambio, es un formato de archivo columnar (en
columnas) muy eficiente que se utiliza para almacenar datos
principalmente de texto. También es un formato abierto y ligero que se
utiliza para el intercambio de datos entre aplicaciones y lenguajes de
programación.\
Ambos tienen compatibilidad con pandas, pero Parquet es más eficiente
para grandes volúmenes de datos. Sus funciones serían:

-   **`df.to_feather(’ruta/archivo.feather’)`**

-   **`df.to_parquet(’ruta/archivo.parquet’, engine=’pyarrow’)`**

Las principales diferencias entre ambos son:

-   Feather está diseñado específicamente para ser extremadamente rápido
    en lectura/escritura

-   Feather usa un formato binario sencillo basado en Apache Arrow, lo
    que lo hace ideal para intercambio rápido entre Python y R.

-   Parquet utiliza una compresión más compleja pensada en reducir el
    tamaño

-   Feather tiene menor compresión que Parquet, resultando en archivos
    más grandes, pero con acceso más rápido.

Mi recomendación para ficheros temporales de cualquier tamaño es
Feather, y Parquet para ficheros muy pesados que vayan a almacenarse en
la nube (\> 10 GB) o dataset con muchas columnas, ya que en estos casos,
Parquet puede llegar a comprimir hasta 10 veces más. No obstante, ten en
cuenta que cuando trabajas con fichero .parquet no vas a poder importar
las primeras líneas para visualizarlas, siempre habrá que importar todo
el fichero.\
Por último, existe también el formato pickle (similar a feather) aunque
es específico para python (**`df.to_pickle()`** y
**`df.read_pickle()`**). Sólo debe ser utilizado como formato
intermedio, desconfiando de ficheros pickles (.pkl) de fuentes no
fiables por sus riesgos de seguridad.

## Vista y verificación de datos

Una buena costumbre antes de empezar a analizar, es chequear la
consistencia de los datos. A continuación, se muestran los principales
recursos que dispone pandas para realizar una correcta tarea de
validación de datos.

-   **`df.head(n)`**: muestra las n primeras filas del dataframe/serie.

-   **`df.tail(n)`**: muestra las n últimas filas del dataframe/serie.

-   **`df.describe()`**: muestra las principales métricas (conteo,
    medias, percentiles, similar a `.summary()` en R)

-   **`df.info()`**: Muestra información del df, como el tipo de dato y
    la memoria usada.

-   **`df.memory_usage()`**: muestra uso de memoria por columna (más
    detallado que **`.info()`**)

-   **`df.shape`**: muestra las dimensiones (filas, columnas) del
    dataframe

-   **`df.columns`**: muestra los nombres de las columnas

-   **`df.dtypes`**: muestra el tipo de dato de cada columna

-   **`df.sample(n)`**: muestra n filas aleatorias (útil para datasets
    grandes)

## Rutas o estructura de carpetas recomendada

Para mantener una estructura y manejo intuitivo de los ficheros
originales y aquellos que vamos generando, es habitual contar con la
siguiente estructura de carpetas, sino exacta si parecida:

-   **`/data/01_raw`** - para los ficheros originales.

-   **`/data/02_intermediate`** - para los ficheros intermedios.

-   **`/data/03_model_input`** - para los ficheros preparados para la
    lectura de nuestros modelos de regresión o clasificación.

-   **`/data/04_outputs`** - para los ficheros finales o de reporting.

### Video nº 1 B {#video-nº-1-b .unnumbered}

::: casopractico
Video Video nº 1 B
:::

[^1]: <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>

[^2]: <https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html>

[^3]: Arquitectura de bases de datos SQL de código abierto y que ocupa
    mínimo espacio: <https://www.sqlite.org>
