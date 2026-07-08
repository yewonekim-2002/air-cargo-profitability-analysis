import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://apis.data.go.kr/B551177/AviationStatsByCountry/getTotalTonsOfCargo"

params = {
    "serviceKey": API_KEY,
    "from_month": "202401",
    "to_month": "202412",
    "periodicity": "0",
    "pax_cargo": "N",
    "baggage_type": "1",
    "type": "json"
}

response = requests.get(url, params=params)

print(response.status_code)

print(response.json())

data = response.json()

print(data.keys())

print(data["response"].keys())

print(data["response"]["body"].keys())

items = data["response"]["body"]["items"]

df = pd.DataFrame(items)

print(df.head())

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

output_path = BASE_DIR / "data" / "raw" / "air_cargo_data.csv"

df.to_csv(output_path, index=False, encoding="utf-8-sig")
