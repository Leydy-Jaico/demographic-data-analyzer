# 📊 Analizador de Datos Demográficos

Proyecto desarrollado en Python utilizando la librería Pandas para realizar análisis de datos demográficos a partir de un conjunto de datos del Censo de 1994.

Este proyecto forma parte de los desafíos de la certificación de Análisis de Datos con Python de freeCodeCamp.

---

# 🎯 Objetivo del Proyecto

El objetivo de este proyecto es analizar información demográfica mediante técnicas de análisis de datos utilizando Python y Pandas.

A partir de un conjunto de datos reales se realizan cálculos estadísticos y filtros para responder diferentes preguntas relacionadas con:

- educación
- salarios
- raza
- ocupación
- país de origen
- horas trabajadas
- edad

---

# 🛠 Tecnologías Utilizadas

- Python 
- Pandas


---

# 📁 Dataset Utilizado

El proyecto utiliza el archivo:

```text
adult.data.csv
```

Este dataset contiene información demográfica del Censo de 1994.

---

# 📌 Información General del Dataset

| Característica | Valor |
|---|---|
| Total de registros | 32,561 |
| Total de columnas | 15 |
| Variables numéricas | 6 |
| Variables categóricas | 9 |
| Memoria utilizada | 3.7 MB |

---

# 📋 Columnas del Dataset

```python
Index([
'age',
'workclass',
'fnlwgt',
'education',
'education-num',
'marital-status',
'occupation',
'relationship',
'race',
'sex',
'capital-gain',
'capital-loss',
'hours-per-week',
'native-country',
'salary'
], dtype='object')
```

---

# 🧾 Explicación de las Columnas

| Columna | Descripción |
|---|---|
| age | Edad de la persona |
| workclass | Tipo de trabajo |
| fnlwgt | Peso estadístico del censo |
| education | Nivel educativo |
| education-num | Nivel educativo en formato numérico |
| marital-status | Estado civil |
| occupation | Ocupación |
| relationship | Relación familiar |
| race | Raza |
| sex | Sexo |
| capital-gain | Ganancia de capital |
| capital-loss | Pérdida de capital |
| hours-per-week | Horas trabajadas por semana |
| native-country | País de origen |
| salary | Nivel salarial |

---

# 📊 Tipos de Datos

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32561 entries, 0 to 32560
Data columns (total 15 columns):
```

---

# 🔎 Explicación de Tipos de Datos

## 🔹 int64
Representa datos numéricos enteros.

Ejemplos:
- edad
- ganancias
- pérdidas
- horas trabajadas

---

## 🔹 object
Representa datos categóricos o de texto.

Ejemplos:
- raza
- ocupación
- país
- salario

---

# ❓ Preguntas Resueltas en el Proyecto

El programa responde automáticamente las siguientes preguntas:

1. ¿Cuántas personas hay por raza?
2. ¿Cuál es la edad promedio de los hombres?
3. ¿Qué porcentaje tiene Bachelor's Degree?
4. ¿Qué porcentaje con educación avanzada gana más de 50K?
5. ¿Qué porcentaje sin educación avanzada gana más de 50K?
6. ¿Cuál es el mínimo de horas trabajadas por semana?
7. ¿Qué porcentaje de personas que trabajan menos horas gana más de 50K?
8. ¿Qué país tiene el mayor porcentaje de personas con salario mayor a 50K?
9. ¿Cuál es la ocupación más popular en India entre quienes ganan más de 50K?

---

# 🧠 Análisis Realizados

Durante el proyecto se aplicaron técnicas de:

- lectura de archivos CSV
- manipulación de DataFrames
- filtrado de datos
- agrupación de información
- estadísticas descriptivas
- conteo de categorías
- cálculos porcentuales
- pruebas unitarias

---

# 📂 Estructura del Proyecto

```text
demographic-data-analyzer/
│
├── adult.data.csv
├── demographic_data_analyzer.py
├── main.py
├── test_module.py
└── README.md
```

---

# 📄 Explicación de Archivos

## demographic_data_analyzer.py

Contiene toda la lógica principal del análisis de datos utilizando Pandas.

---

## main.py

Ejecuta el programa principal y corre automáticamente las pruebas unitarias.

---

## test_module.py

Contiene las pruebas unitarias utilizadas para verificar que los resultados obtenidos sean correctos.

---

# ▶️ Cómo Ejecutar el Proyecto

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Leydy-Jaico/demographic-data-analyzer.git
```

---

## 2️⃣ Ingresar a la carpeta del proyecto

```bash
cd demographic-data-analyzer
```

---

## 3️⃣ Ejecutar el programa

```bash
python main.py
```

---

# ✅ Resultado Esperado

Si todo funciona correctamente aparecerá:

```text
Ran 10 tests

OK
```

Esto indica que:
- todas las preguntas fueron resueltas correctamente,
- el análisis funciona,
- y las pruebas unitarias fueron aprobadas.

---

# 📈 Resultados Obtenidos

Algunos resultados del análisis fueron:

| Análisis | Resultado |
|---|---|
| Edad promedio de hombres | 39.4 |
| Porcentaje con Bachelor's | 16.4% |
| País con mayor porcentaje >50K | Iran |
| Ocupación más popular en India | Prof-specialty |

---

# 📚 Aprendizajes Obtenidos

Este proyecto permitió reforzar conocimientos sobre:

- análisis de datos con Pandas
- manejo de DataFrames
- limpieza y exploración de datos
- filtros y consultas
- automatización de pruebas
- organización de proyectos Python
- uso de Git y GitHub

---

# 👩‍💻 Autor

Leydy Jaico

Proyecto académico desarrollado como práctica de análisis de datos con Python.

---

# 🙌 Agradecimientos

Agradecimiento especial a:

- freeCodeCamp, por proporcionar el desafío y material de aprendizaje.
- TECHY, programa en el que actualmente participo y gracias al cual continúo fortaleciendo mis conocimientos en tecnología, programación y análisis de datos.

Este proyecto fue desarrollado como parte de mi proceso de aprendizaje y crecimiento profesional en el área de desarrollo y ciencia de datos.
