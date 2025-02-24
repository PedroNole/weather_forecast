import requests
import pandas as pd
import datetime
import time

def get_weather_data(lat, lon, start_date, end_date, max_retries=5):
    base_url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,windspeed_10m_max",
        "timezone": "Europe/Madrid"
    }
    
    delay = 5
    for attempt in range(max_retries):
        response = requests.get(base_url, params=params)
        if response.status_code == 429:
            print(f"Error 429 para ({lat}, {lon}). Esperando {delay} s antes de reintentar (Intento {attempt+1}/{max_retries})...")
            time.sleep(delay)
            delay *= 2  # retroceso exponencial
        else:
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data["daily"])
            df["date"] = pd.to_datetime(df["time"]).dt.date
            return df
    raise Exception(f"No se pudieron obtener datos para ({lat}, {lon}) desde {start_date} hasta {end_date} tras {max_retries} intentos.")

# Definimos el rango completo de fechas (desde 2013 hasta la fecha actual)
start_date_total = "2013-01-01"
end_date_total = datetime.date.today().strftime("%Y-%m-%d")

# Diccionario de provincias (capitales) con sus coordenadas
provincias = {
    "A Coruña": {"lat": 43.37012643, "lon": -8.39114853},
    "Albacete": {"lat": 38.99588053, "lon": -1.85574745},
    "Alicante": {"lat": 38.34548705, "lon": -0.4831832},
    "Almería": {"lat": 36.83892362, "lon": -2.46413188},
    "Ávila": {"lat": 40.65586958, "lon": -4.69771277},
    "Badajoz": {"lat": 38.87874339, "lon": -6.97099704},
    "Barcelona": {"lat": 41.38424664, "lon": 2.17634927},
    "Vizcaya": {"lat": 43.25721957, "lon": -2.92390606},
    "Burgos": {"lat": 42.34113004, "lon": -3.70419805},
    "Cáceres": {"lat": 39.47316762, "lon": -6.37121092},
    "Cádiz": {"lat": 36.52171152, "lon": -6.28414575},
    "Castellón": {"lat": 39.98640809, "lon": -0.03688142},
    "Ceuta": {"lat": 35.88810209, "lon": -5.30675127},
    "Ciudad Real": {"lat": 38.98651781, "lon": -3.93131981},
    "Córdoba": {"lat": 37.87954225, "lon": -4.78032455},
    "Cuenca": {"lat": 40.07653762, "lon": -2.13152306},
    "Girona": {"lat": 41.98186075, "lon": 2.82411899},
    "Granada": {"lat": 37.17641932, "lon": -3.60001883},
    "Guadalajara": {"lat": 40.63435548, "lon": -3.16210273},
    "Huelva": {"lat": 37.26004113, "lon": -6.95040588},
    "Huesca": {"lat": 42.14062739, "lon": -0.40842276},
    "Jaén": {"lat": 37.7651913, "lon": -3.7903594},
    "Las Palmas": {"lat": 28.099378545, "lon": -15.413368411},
    "León": {"lat": 42.59912097, "lon": -5.56707631},
    "Lleida": {"lat": 41.61527355, "lon": 0.62061934},
    "La Rioja": {"lat": 42.46644945, "lon": -2.44565538},
    "Lugo": {"lat": 43.0091282, "lon": -7.55817392},
    "Madrid": {"lat": 40.40841191, "lon": -3.68760088},
    "Málaga": {"lat": 36.72034267, "lon": -4.41997511},
    "Melilla": {"lat": 35.294731, "lon": -2.942281},
    "Murcia": {"lat": 37.98436361, "lon": -1.1285408},
    "Ourense": {"lat": 42.33654919, "lon": -7.86368375},
    "Asturias": {"lat": 43.36232165, "lon": -5.84372206},
    "Palencia": {"lat": 42.0078373, "lon": -4.53460106},
    "Baleares": {"lat": 39.57114699, "lon": 2.65181698},
    "Navarra": {"lat": 42.814102, "lon": -1.6451528},
    "Pontevedra": {"lat": 42.43381442, "lon": -8.64799018},
    "Salamanca": {"lat": 40.96736822, "lon": -5.66538084},
    "Gipuzkoa": {"lat": 43.31717158, "lon": -1.98191785},
    "Santa Cruz de Tenerife": {"lat": 28.462854082, "lon": -16.247206286},
    "Cantabria": {"lat": 43.46297885, "lon": -3.80474784},
    "Segovia": {"lat": 40.9498703, "lon": -4.12524116},
    "Sevilla": {"lat": 37.38620512, "lon": -5.99251368},
    "Soria": {"lat": 41.76327912, "lon": -2.46624798},
    "Tarragona": {"lat": 41.11910287, "lon": 1.2584219},
    "Teruel": {"lat": 40.34412951, "lon": -1.10927177},
    "Toledo": {"lat": 39.85715187, "lon": -4.02431421},
    "Valencia": {"lat": 39.47534441, "lon": -0.37565717},
    "Valladolid": {"lat": 41.65232777, "lon": -4.72334924},
    "Álava": {"lat": 42.85058789, "lon": -2.67275685},
    "Zamora": {"lat": 41.49913956, "lon": -5.75494831},
    "Zaragoza": {"lat": 41.65645655, "lon": -0.87928652}
}

lista_df = []

for provincia, coords in provincias.items():
    print(f"Consultando datos para {provincia}...")
    try:
        df_provincia = get_weather_data(coords["lat"], coords["lon"], start_date_total, end_date_total, 3)
        df_provincia["provincia"] = provincia
        lista_df.append(df_provincia)
        time.sleep(1)
    except Exception as e:
        print(f"Error al consultar {provincia}: {e}")

if lista_df:
    df_total = pd.concat(lista_df, ignore_index=True)
    print(df_total.head())
    df_total.to_csv("historico_provincias_espana.csv", index=False)
else:
    print("No se obtuvieron datos de ninguna provincia.")
