import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "data" / "processed" / "cargo_2024_processed.csv"

df = pd.read_csv(input_path)

print(df.head())

df["net_cargo_flow"] = (
    df["departure_cargo_tons"]
    - df["arrival_cargo_tons"]
)

def cargo_direction(flow):

    if flow > 0:
        return "Outbound"

    elif flow < 0:
        return "Inbound"

    else:
        return "Balanced"


df["cargo_direction"] = df["net_cargo_flow"].apply(cargo_direction)


df["departure_ratio"] = (
    df["departure_cargo_tons"]
    / df["total_cargo_tons"]
)

df["arrival_ratio"] = (
    df["arrival_cargo_tons"]
    / df["total_cargo_tons"]
)

print(df.head())
print(df.info())

output_path = BASE_DIR / "data" / "featured" / "cargo_2024_featured.csv"

df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print(f"Saved to: {output_path}")