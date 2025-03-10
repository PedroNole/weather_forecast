# Spain Weather Forecast

Este repositorio contiene un proyecto de series temporales para la predicción meteorológica en diferentes regiones de España. Se utilizan datos obtenidos desde la API de [Aemet](https://opendata.aemet.es/centrodedescargas/productosAEMET), de [Open Meteo](https://open-meteo.com/) y de [Comunidad de Madrid](https://datos.madrid.es/), los cuales se almacenan en archivos CSV y se organizan en distintas carpetas.

---

## Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Datos](#datos)
7. [Análisis Exploratorio (EDA)](#análisis-exploratorio-eda)
8. [Algoritmos y Modelos](#algoritmos-y-modelos)

---

## Descripción General

Este proyecto se centra en la construcción de modelos de predicción meteorológica (temperatura, precipitación, etc.) para distintas zonas de España. Para ello, se emplean datos históricos proporcionados por Aemet y Open Meteo, los cuales se utilizan para:

- **Entrenamiento de modelos de series temporales** (ARIMA, Prophet, LSTM, entre otros).
- **Validación y comparación** de resultados para diferentes regiones (ej. Almería, A Coruña, Madrid).
- **Generación de predicciones** de corto y mediano plazo.

---

## Estructura del Proyecto

La estructura principal del repositorio se basa en las siguientes carpetas y archivos:

```bash
    Spain Weather Forecast
    │
    ├── Algorithms
    │   └── intro.txt
    │
    ├── Data
    │   ├── homogenized
    │   │   ├── aemet
    │   │   │   ├── tratamiento_datos_aemet.ipynb
    │   │   │   └── tratamiento_datos_aemet_pyspark.ipynb
    │   │   │       
    │   │   ├── madrid
    │   │   │
    │   │   └── open_meteo
    │   │       └── tratamiento_datos_open_meteo.ipynb
    │   │   
    │   ├── raw
    │   │   ├── aemet
    │   │   │   └── temp_historico.csv  # Datos históricos diarios en España recogidos por Aemet. 
    │   │   │
    │   │   ├── madrid
    │   │   │   └── madrid.csv # Datos históricos por horas de las estaciones de la Comunidad de Madrid.
    │   │   │
    │   │   └── open_meteo
    │   │       ├── historico_provincias_espana.csv # Datos históricos diarios en España recogidos por Open Meteo API.
    │   │       └── get_historical.py
    │   │
    │   └── transformed
    │       ├── transformed_aemet.csv
    │       └── transformed_open_meteo.csv
    │
    ├── Models
    │   ├── Sarimax
    │   │   └── predicciones.pkl ...
    │   │
    │   └── ...
    │
    ├── EDA
    │   ├── daily                       # EDA de tres regiones de España.
    │   │   ├── eda_daily_almeria.ipynb
    │   │   ├── eda_daily_coruna.ipynb
    │   │   └── eda_daily_madrid.ipynb
    │   │
    │   └── hours
    │       └── eda_hours_madrid.ipynb    
    │   
    │
    ├── .gitignore
    ├── enviroment.yml
    └── README.md
```

A grandes rasgos:

- **Algorithms/**: Contiene scripts o cuadernos con modelos de predicción y algoritmos de machine learning.
- **Data/**: 
  - **raw/**: Datos originales sin procesar descargados de Aemet, Open Meteo y Comunidad de Madrid.
  - **homogenized/**: Carpeta orientada a la transformación de los datos.
  - **transformed/**: Carpeta con los archivos de datos ya transformados y listos para usar.
- **EDA/**: Cuadernos Jupyter para el análisis exploratorio de datos (EDA) específico de cada región.
- **README.md**: Este archivo que describe el proyecto.

---

## Requisitos

1. **Python 3.11+**
2. **Bibliotecas**:
    - `python=3.11`
    - `scikit-learn`
    - `statsmodels`
    - `requests` (para la descarga de datos desde APIs)
    - `jupyter` o `jupyterlab`
    - `pandas`
    - `numpy`
    - `scikit-learn`
    - `pyspark`
    - `plotly`
    - `statsmodels`
    - `pmdarima`
    - Cualquier otra biblioteca específica (por ejemplo, `prophet`, `tensorflow`, etc.)
3. **Conexión a Internet** para la descarga de datos (si se desea actualizar con `get_historical.py`).

*(En caso de que se disponga de un archivo **enviroment.yml** con las dependencias.)*

---

## Instalación

1. **Clonar el repositorio:**
```bash
    git clone https://github.com/escuuu/weather_forecast.git
    cd nombre-del-repo
```
2. **Crear un entorno virtual *(opcional pero recomendado)*:**
```bash
conda env create -f enviroment.yml
conda activate weather_forecast
```
3. **Instalar dependencias:**
```bash
pip install -r enviroment.yml
```

---

## Uso

1. **Descarga de datos:** Si se desea actualizar o descargar los datos desde la API de Aemet y Open Meteo, ejecutar:
```bash
python get_historical.py
```

2. **Preprocesado:** Dependiendo de la estrategia de limpieza y homogenización, existen scripts o notebooks que transforman los datos en crudos a datos procesados. Revisar la carpeta `Data/homogenized/` y `Data/transformed/` y los scripts asociados.
3. **Análisis Exploratorio:** Abrir los notebooks de la carpeta EDA/ para revisar los análisis de cada región. Por ejemplo:
```bash
jupyter notebook EDA/daily/eda_daily_madrid.ipynb
```
4. **Entrenamiento de Modelos:** En la carpeta `Algorithms/` se incluyen los algoritmos de predicción.

---

## Análisis Exploratorio (EDA)

En la carpeta `EDA/` se encuentran los cuadernos Jupyter con estudios exploratorios por zonas:

- `eda_daily_almeria.ipynb`
- `eda_daily_coruna.ipynb`
- `eda_daily_madrid.ipynb`

Cada cuaderno contiene:

- Visualizaciones de variables (temperatura, precipitación, etc.).
- Detección y manejo de valores atípicos.
- Análisis de correlaciones.

---

## Algoritmos y Modelos

En la carpeta `Algorithms/` se detallan diferentes aproximaciones de modelado:

- Modelos clásicos de series temporales: *Sarimax*.
- Modelos de machine learning: *RandomForestRegressor*.