import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Load featured dataset
featured_path = (
    BASE_DIR
    / "data"
    / "featured"
    / "cargo_2024_featured.csv"
)

cargo_df = pd.read_csv(featured_path)

# Extract unique countries
countries = sorted(cargo_df["country"].unique())

# Create empty route master template
route_master = pd.DataFrame({
    "country": countries,
    "airport": "",
    "iata": "",
    "distance_km": None,
    "region": ""
})

# Save template
output_path = (
    BASE_DIR
    / "data"
    / "reference"
    / "route_master.csv"
)

route_master.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print(route_master)
print(f"\nSaved to: {output_path}")