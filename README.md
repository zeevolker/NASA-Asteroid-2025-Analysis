# NASA Asteroid 2025 Analysis

## Project Overview

Analisis Near-Earth Asteroids menggunakan NASA NeoWs API.

## Objectives

- Mengumpulkan data asteroid
- Membersihkan data
- Melakukan EDA
- Membuat dashboard interaktif

## Dataset

Source:
https://api.nasa.gov

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly
- NASA NeoWs API

## Key Findings

- 1.655 asteroid dianalisis
- 172 asteroid hazardous
- Diameter terbesar 49 km
- Kecepatan maksimum 186.000 km/jam

## Dashboard Preview

<p align="center">
  <img src="assets/Dashboard Top 10 Highest Risk Score.png" width="900">
  <img src="assets/Dashboard Size Category Distribution.png" width="900">
  <img src="assets/Dashboard Asteroid per Month.png" width="900">
</p>

## Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
