import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "data" / "raw" / "cargo_2024.csv"

df = pd.read_csv(input_path)

print(df.head())

print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)

df = df.rename(columns={
    "arrBaggage": "arrival_cargo_tons",
    "depBaggage": "departure_cargo_tons",
    "baggage": "total_cargo_tons"
})

cargo_columns = [
    "arrival_cargo_tons",
    "departure_cargo_tons",
    "total_cargo_tons"
]

for col in cargo_columns:
    df[col] = (
        df[col]
        .str.replace(",", "", regex=False)
        .astype(int)
    )

print(df.info())

region_mapping = {
    "동북아": "Northeast Asia",
    "동남아": "Southeast Asia",
    "미주": "Americas",
    "유럽": "Europe",
    "중동": "Middle East",
    "대양주": "Oceania"
}

country_mapping = {
    "한국": "South Korea",
    "일본": "Japan",
    "중국": "China",
    "홍콩": "Hong Kong",
    "대만": "Taiwan",
    "미국": "United States",
    "캐나다": "Canada",
    "멕시코": "Mexico",
    "영국": "United Kingdom",
    "프랑스": "France",
    "독일": "Germany",
    "이탈리아": "Italy",
    "네덜란드": "Netherlands",
    "벨기에": "Belgium",
    "스페인": "Spain",
    "스위스": "Switzerland",
    "터키": "Turkey",
    "아랍에미리트": "United Arab Emirates",
    "카타르": "Qatar",
    "사우디아라비아": "Saudi Arabia",
    "싱가포르": "Singapore",
    "태국": "Thailand",
    "베트남": "Vietnam",
    "말레이시아": "Malaysia",
    "인도네시아": "Indonesia",
    "필리핀": "Philippines",
    "인도": "India",
    "호주": "Australia",
    "뉴질랜드": "New Zealand",
    "몽골": "Mongolia",
    "러시아": "Russia",
    "우즈베키스탄": "Uzbekistan",
    "카자흐스탄": "Kazakhstan",
    "키르기스스탄": "Kyrgyzstan",
    "괌": "Guam",
    "마카오": "Macau"
}

country_mapping.update({
    "노르웨이": "Norway",
    "룩셈부르크": "Luxembourg",
    "브라질": "Brazil",
    "스웨덴": "Sweden",
    "아제르바이잔": "Azerbaijan",
    "오스트리아": "Austria",
    "칠레": "Chile",
    "투르크메니스탄": "Turkmenistan",
    "페루": "Peru",
    "하와이": "Hawaii"
})

df["region"] = df["region"].replace(region_mapping)
df["country"] = df["country"].replace(country_mapping)


print(df.head())

output_path = BASE_DIR / "data" / "processed" / "cargo_2024_processed.csv"

df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print(f"Processed data saved to: {output_path}")