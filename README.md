# Spain Weather Forecast

Este repositorio contiene un proyecto de series temporales para la predicción meteorológica en diferentes regiones de España. Se utilizan datos obtenidos desde la API de [Aemet](https://opendata.aemet.es/centrodedescargas/productosAEMET) y de [Open Meteo](https://open-meteo.com/), los cuales se almacenan en archivos CSV y se organizan en distintas carpetas.

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
    ├── Algorithms
    │   └── intro.txt
    ├── Data
    │   ├── homogenized
    │   │   ├── aemet
    │   │   └── open_meteo
    │   ├── raw
    │   │   ├── aemet
    │   │   │   └── temp_historico.csv
    │   │   └── open_meteo
    │   │       └── historico_provincias_espana.csv
    │   └── transformed
    │       └── intro.txt
    ├── EDA
    │   ├── eda_daily_almeria.ipynb
    │   ├── eda_daily_coruna.ipynb
    │   ├── eda_daily_madrid.ipynb
    │   └── .ipynb_checkpoints
    ├── .gitignore
    ├── get_historical.py
    └── README.md
```

A grandes rasgos:

- **Algorithms/**: Contiene scripts o cuadernos con modelos de predicción y algoritmos de machine learning/deep learning.
- **Data/**: 
  - **raw/**: Datos originales sin procesar descargados de Aemet y Open Meteo.
  - **homogenized/**: Datos procesados o limpiados para su uso en modelado.
  - **transformed/**: Datos transformados, listos para ser usados en análisis o entrenamiento.
- **EDA/**: Cuadernos Jupyter para el análisis exploratorio de datos (EDA) específico de cada región.
- **get_historical.py**: Script para descargar o actualizar los datos históricos.
- **README.md**: Este archivo que describe el proyecto.


---

## Requisitos

1. **Python 3.8+** (o la versión que se haya utilizado para el proyecto).
2. **Bibliotecas** (ejemplo):
   - `pandas`
   - `numpy`
   - `matplotlib`
   - `seaborn`
   - `scikit-learn`
   - `statsmodels`
   - `requests` (para la descarga de datos desde APIs)
   - `jupyter` o `jupyterlab`
   - Cualquier otra biblioteca específica (por ejemplo, `prophet`, `tensorflow`, etc.)
3. **Conexión a Internet** para la descarga de datos (si se desea actualizar con `get_historical.py`).

Se recomienda crear y usar un entorno virtual para gestionar dependencias:

```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate     # En Windows
    pip install -r requirements.txt
```

*(En caso de que se disponga de un archivo **requirements.txt** con las dependencias.)*