import requests
import pandas as pd
from datetime import datetime, timedelta
import time

# =====================
# KONFIGURASI
# =====================

API_KEY = "hr5fCPMfqb44cosTKlaFkr6fAdMV5f40NZWWvodx"

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

OUTPUT_FILE = "data/asteroids_2025.csv"

# =====================
# PENAMPUNG DATA
# =====================

asteroids = []

current_date = START_DATE

# =====================
# PENGAMBILAN DATA
# =====================

while current_date <= END_DATE:

    next_date = current_date + timedelta(days=7)

    if next_date > END_DATE:
        next_date = END_DATE

    print(
        f"Mengambil data "
        f"{current_date.strftime('%Y-%m-%d')} "
        f"sampai "
        f"{next_date.strftime('%Y-%m-%d')}"
    )

    url = (
        "https://api.nasa.gov/neo/rest/v1/feed"
        f"?start_date={current_date.strftime('%Y-%m-%d')}"
        f"&end_date={next_date.strftime('%Y-%m-%d')}"
        f"&api_key={API_KEY}"
    )

    try:

        response = requests.get(url, timeout=30)

        if response.status_code != 200:
            print("ERROR:", response.status_code)
            print(response.text)
            break

        data = response.json()

        for date in data["near_earth_objects"]:

            for asteroid in data["near_earth_objects"][date]:

                try:

                    if not asteroid["close_approach_data"]:
                        continue

                    approach = asteroid["close_approach_data"][0]

                    diameter_min = (
                        asteroid["estimated_diameter"]
                        ["meters"]
                        ["estimated_diameter_min"]
                    )

                    diameter_max = (
                        asteroid["estimated_diameter"]
                        ["meters"]
                        ["estimated_diameter_max"]
                    )

                    diameter_avg = (
                        diameter_min + diameter_max
                    ) / 2

                    velocity_kmh = float(
                        approach["relative_velocity"]
                        ["kilometers_per_hour"]
                    )

                    velocity_kps = float(
                        approach["relative_velocity"]
                        ["kilometers_per_second"]
                    )

                    miss_distance_km = float(
                        approach["miss_distance"]
                        ["kilometers"]
                    )

                    miss_distance_ld = float(
                        approach["miss_distance"]
                        ["lunar"]
                    )

                    close_date = pd.to_datetime(
                        approach["close_approach_date"]
                    )

                    # =====================
                    # KATEGORI UKURAN
                    # =====================

                    if diameter_avg < 50:
                        size_category = "Small"

                    elif diameter_avg < 300:
                        size_category = "Medium"

                    elif diameter_avg < 1000:
                        size_category = "Large"

                    else:
                        size_category = "Huge"

                    # =====================
                    # VERY CLOSE FLAG
                    # =====================

                    very_close = (
                        miss_distance_km < 1_000_000
                    )

                    # =====================
                    # RISK SCORE
                    # =====================

                    risk_score = (
                        diameter_avg *
                        velocity_kmh
                    ) / miss_distance_km

                    # =====================
                    # IMPACT ENERGY
                    # (Sederhana untuk portfolio)
                    # =====================

                    mass_proxy = diameter_avg ** 3

                    impact_energy = (
                        0.5 *
                        mass_proxy *
                        (velocity_kps * 1000) ** 2
                    )

                    asteroids.append({

                        "id":
                            asteroid["id"],

                        "name":
                            asteroid["name"],

                        "hazardous":
                            asteroid[
                                "is_potentially_hazardous_asteroid"
                            ],

                        "absolute_magnitude":
                            asteroid["absolute_magnitude_h"],

                        "diameter_min_m":
                            diameter_min,

                        "diameter_max_m":
                            diameter_max,

                        "diameter_avg_m":
                            diameter_avg,

                        "size_category":
                            size_category,

                        "close_approach_date":
                            approach[
                                "close_approach_date"
                            ],

                        "year":
                            close_date.year,

                        "month":
                            close_date.month,

                        "day":
                            close_date.day,

                        "velocity_kmh":
                            velocity_kmh,

                        "velocity_kps":
                            velocity_kps,

                        "miss_distance_km":
                            miss_distance_km,

                        "miss_distance_ld":
                            miss_distance_ld,

                        "very_close":
                            very_close,

                        "risk_score":
                            risk_score,

                        "impact_energy":
                            impact_energy,

                        "orbiting_body":
                            approach["orbiting_body"],

                        "nasa_jpl_url":
                            asteroid["nasa_jpl_url"]
                    })

                except Exception as e:
                    print("Skip asteroid:", e)

    except Exception as e:
        print("Request Error:", e)

    current_date = next_date + timedelta(days=1)

    time.sleep(1)

# =====================
# DATAFRAME
# =====================

df = pd.DataFrame(asteroids)

# Hapus duplikat
df.drop_duplicates(inplace=True)

# Ranking Risiko
df["risk_rank"] = (
    df["risk_score"]
    .rank(
        ascending=False,
        method="dense"
    )
)

# =====================
# SIMPAN CSV
# =====================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

# =====================
# RINGKASAN
# =====================

print("\n===== SUMMARY =====")

print("Jumlah Data:", len(df))

print(
    "Hazardous:",
    df["hazardous"].sum()
)

print(
    "Non-Hazardous:",
    (~df["hazardous"]).sum()
)

print(
    "Diameter Terbesar:",
    round(
        df["diameter_max_m"].max(),
        2
    ),
    "meter"
)

print(
    "Kecepatan Maksimum:",
    round(
        df["velocity_kmh"].max(),
        2
    ),
    "km/jam"
)

print(
    "Jarak Terdekat:",
    round(
        df["miss_distance_km"].min(),
        2
    ),
    "km"
)

print(
    "File tersimpan:",
    OUTPUT_FILE
)