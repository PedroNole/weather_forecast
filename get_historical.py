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
    
    delay = 2  # segundos iniciales de espera en caso de error 429
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

# Rango de fechas completo (desde 2013 hasta hoy)
start_date_total = "2013-01-01"
end_date_total = datetime.date.today().strftime("%Y-%m-%d")

# Diccionario de provincias (capitales) con coordenadas redondeadas a 4 decimales
provincias = {
    # "A Coruña": {"lat": 43.3701, "lon": -8.3911},
    # "Albacete": {"lat": 38.9959, "lon": -1.8557},
    # "Alicante": {"lat": 38.3455, "lon": -0.4832},
    # "Almería": {"lat": 36.8389, "lon": -2.4641},
    # "Ávila": {"lat": 40.6559, "lon": -4.6977},
    # "Badajoz": {"lat": 38.8787, "lon": -6.9710},
    # "Barcelona": {"lat": 41.3842, "lon": 2.1763},
    # "Vizcaya": {"lat": 43.2572, "lon": -2.9239},
    # "Burgos": {"lat": 42.3411, "lon": -3.7042},
    # "Cáceres": {"lat": 39.4732, "lon": -6.3712},
    # "Cádiz": {"lat": 36.5217, "lon": -6.2841},
    # "Castellón": {"lat": 39.9864, "lon": -0.0369},

    "Ceuta": {"lat": 35.8881, "lon": -5.3068},

    # "Ciudad Real": {"lat": 38.9865, "lon": -3.9313},
    # "Córdoba": {"lat": 37.8795, "lon": -4.7803},

    "Cuenca": {"lat": 40.0765, "lon": -2.1315},

    # "Girona": {"lat": 41.9819, "lon": 2.8241},
    # "Granada": {"lat": 37.1764, "lon": -3.6000},

    "Guadalajara": {"lat": 40.6344, "lon": -3.1621},

    # "Huelva": {"lat": 37.2600, "lon": -6.9504},
    # "Huesca": {"lat": 42.1406, "lon": -0.4084},
    # "Jaén": {"lat": 37.7652, "lon": -3.7904},
    # "Las Palmas": {"lat": 28.0994, "lon": -15.4134},
    # "León": {"lat": 42.5991, "lon": -5.5671},
    # "Lleida": {"lat": 41.6153, "lon": 0.6206},
    # "La Rioja": {"lat": 42.4664, "lon": -2.4457},
    # "Lugo": {"lat": 43.0091, "lon": -7.5582},
    # "Madrid": {"lat": 40.4165, "lon": -3.7026},
    # "Málaga": {"lat": 36.7203, "lon": -4.4200},
    # "Melilla": {"lat": 35.2947, "lon": -2.9423},
    # "Murcia": {"lat": 37.9844, "lon": -1.1285},
    # "Ourense": {"lat": 42.3365, "lon": -7.8637},
    # "Asturias": {"lat": 43.3623, "lon": -5.8437},
    # "Palencia": {"lat": 42.0078, "lon": -4.5346},
    # "Baleares": {"lat": 39.5711, "lon": 2.6518},

    "Navarra": {"lat": 42.8141, "lon": -1.6452},
    "Pontevedra": {"lat": 42.4338, "lon": -8.6480},
    "Salamanca": {"lat": 40.9674, "lon": -5.6654},
    "Gipuzkoa": {"lat": 43.3172, "lon": -1.9819},
    "Santa Cruz de Tenerife": {"lat": 28.4629, "lon": -16.2472},
    "Cantabria": {"lat": 43.4630, "lon": -3.8047},
    "Segovia": {"lat": 40.9499, "lon": -4.1252},
    "Sevilla": {"lat": 37.3862, "lon": -5.9925},
    "Soria": {"lat": 41.7633, "lon": -2.4662},
    "Tarragona": {"lat": 41.1191, "lon": 1.2584},
    "Teruel": {"lat": 40.3441, "lon": -1.1093},
    "Toledo": {"lat": 39.8572, "lon": -4.0243},
    "Valencia": {"lat": 39.4753, "lon": -0.3757},
    "Valladolid": {"lat": 41.6523, "lon": -4.7233},
    "Álava": {"lat": 42.8506, "lon": -2.6728},
    "Zamora": {"lat": 41.4991, "lon": -5.7549},
    "Zaragoza": {"lat": 41.6565, "lon": -0.8793}
}

lista_df = []

for provincia, coords in provincias.items():
    print(f"Consultando datos para {provincia}...")
    try:
        df_provincia = get_weather_data(coords["lat"], coords["lon"], start_date_total, end_date_total)
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
