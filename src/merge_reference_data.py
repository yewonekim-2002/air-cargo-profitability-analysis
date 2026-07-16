import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

cargo_path = (
    BASE_DIR
    / "data"
    / "featured"
    / "cargo_2024_featured.csv"
)

route_path = (
    BASE_DIR
    / "data"
    / "reference"
    / "route_master.csv"
)

cargo_df = pd.read_csv(cargo_path)
route_df = pd.read_csv(route_path)

merged_df = cargo_df.merge(
    route_df,
    on="country",
    how="left"
)


print(merged_df.head())

output_path = (
    BASE_DIR
    / "data"
    / "processed"
    / "cargo_with_route.csv"
)

merged_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print(f"Saved to: {output_path}")