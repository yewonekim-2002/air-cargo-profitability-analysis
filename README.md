# ✈️ Air Cargo Profitability Analysis

A data analysis project exploring international air cargo flows using Incheon International Airport cargo data.

The project focuses on identifying major cargo destinations, regional cargo distribution, export/import trends, and business insights through Python, Pandas, and Power BI.

---

## 📌 Project Objectives

- Analyze international air cargo traffic.
- Identify major export and import destinations.
- Compare cargo volume across regions.
- Evaluate regional trade balance using net cargo flow.
- Build an interactive Power BI dashboard for business insights.

---

## 🛠️ Tech Stack

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Power BI
- Git & GitHub

---

## 📂 Project Structure

```
air-cargo-profitability-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── featured/
│   └── reference/
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   ├── collect_data.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── create_route_master.py
│   └── merge_reference_data.py
│
├── dashboard/
│
├── images/
│
├── requirements.txt
└── README.md
```

---

# 🔄 Data Pipeline

```
Raw Cargo Data
        │
        ▼
Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Route Reference Merge
        │
        ▼
Processed Dataset
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Power BI Dashboard
```

---

# 📊 Exploratory Data Analysis

## Analysis 1

### Business Question

Which countries receive the largest amount of cargo?

**Insight**

- The United States handled the largest cargo volume.
- China ranked second.
- Japan, Vietnam, and Germany were also among the major cargo destinations.

---

## Analysis 2

### Business Question

Which countries export the most cargo?

**Insight**

- The United States exported the highest cargo volume.
- China and Vietnam were also major outbound cargo destinations.

---

## Analysis 3

### Business Question

Which countries import the most cargo?

**Insight**

- The United States received the highest inbound cargo volume.
- China and Germany were among the largest import destinations.

---

## Analysis 4

### Business Question

Which countries are net exporters?

**Insight**

- Vietnam recorded the largest positive net cargo flow.
- Hong Kong and Austria also functioned as export-oriented destinations.

---

## Analysis 5

### Business Question

Which regions handle the largest cargo volume?

**Insight**

- Northeast Asia handled the largest cargo volume.
- Europe ranked second, followed by the Americas.
- Southeast Asia also played a significant role in international cargo transportation.

---

## Analysis 6

### Business Question

Which regions are net exporters and which are net importers?

**Insight**

- Northeast Asia recorded the highest positive net cargo flow.
- Southeast Asia and the Middle East were also net exporters.
- Europe recorded the largest negative net cargo flow, indicating import-oriented cargo movement.

---

## Analysis 7

### Business Question

Which countries are highly export-oriented?

**Insight**

- Austria showed the highest departure ratio.
- Hong Kong and Vietnam also demonstrated strong export-oriented characteristics.
- Departure ratio complements total cargo volume by highlighting trade direction rather than cargo scale.

---

# 📈 Dashboard (Coming Soon)

The Power BI dashboard will include:

- KPI Cards
- Top Cargo Destinations
- Export vs Import Comparison
- Cargo Volume by Region
- Net Cargo Flow
- Interactive Country Filters

---

# 📁 Dataset

Source:

- Incheon International Airport cargo statistics

Additional reference data:

- Airport information
- Region mapping

---

# 🚀 Future Improvements

- Monthly cargo trend analysis
- Route distance analysis
- Forecasting cargo demand
- Interactive Power BI dashboard
- Machine Learning for cargo prediction

---

# 👩‍💻 Author

**Yewon Kim**

Information & Communication Engineering

Aspiring Data Analyst
    
