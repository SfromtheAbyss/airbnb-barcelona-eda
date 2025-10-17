# 🏙️ Airbnb Exploratory Data Analysis (EDA) - Barcelona

**Author:** [Sorrow Grajales](https://github.com/SfromtheAbyss)  
**Date:** October 2025  
**Technologies:** Python, Pandas, Seaborn, Folium, Plotly  

---

## 📌 Project Description

This project performs an **Exploratory Data Analysis (EDA)** on the **Airbnb listings dataset in Barcelona**, aiming to understand the factors affecting prices, the geographic distribution of listings, and temporal trends in reviews.

The analysis is part of my portfolio as a **Junior Data Scientist**, demonstrating skills in data analysis, visualization, and communication of results.

---

## 🧱 Project Structure
```
airbnb-eda/
│
├── data/ # Datasets originales (no subidos por tamaño)
│ └── listings.csv
│
├── notebooks/
│ └── airbnb_eda_barcelona.ipynb # Notebook principal con el análisis
│
├── src/
│ └── utils.py # Funciones de limpieza y soporte
│
├── reports/
│ └── figures/ # Gráficos y visualizaciones exportadas
│ ├── distribucion_precios.png
│ ├── top20_barrios.png
│ ├── heatmap_correlacion.png
│ └── mapa_airbnb_bcn.html
│
├── requirements.txt
├── README.md
└── .gitignore
```
---

## 🔍 Key Insights

📊 **Price Distribution:**  
Most listings are priced between **€50 and €200 per night**, with outliers in premium neighborhoods such as Eixample and Sarrià.

📍 **Geographic Distribution:**  
The busiest neighborhoods are **Eixample, Ciutat Vella, and Gràcia**, concentrating most listings.

📈 **Temporal Trends:**  
The number of reviews steadily grew from 2014 to 2019, reflecting the rise of urban tourism in Barcelona, followed by a slight drop post-pandemic.

🧩 **Correlations:**  
There is a positive correlation between **annual availability and number of reviews**, while price shows low correlation with other variables.

---

## 📊 Key Visualizations

### 💸 Price Distribution
![Price Distribution](reports/figures/price_distribution.png)

### 🏘️ Top 20 Neighborhoods with Most Listings
![Top Neighborhoods](reports/figures/top20_neighborhoods.png)

### 🔥 Correlation Heatmap
![Correlation Heatmap](reports/figures/correlation_heatmap.png)

### ⏱️ Annual Trend of Reviews
![Annual Reviews Trend](reports/figures/annual_reviews_trend.png)

### 🌍 Interactive Map of Airbnb Listings in Barcelona
👉 [View Interactive Map](reports/figures/airbnb_bcn_map.html)

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```
git clone git@github.com:TU_USUARIO/airbnb-barcelona-eda.git
cd airbnb-barcelona-eda
```
### 2️⃣ Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Run the analysis
```
jupyter notebook notebooks/airbnb_eda_barcelona.ipynb
```
---

## 🧠 Technologies & Libraries

· Python 3.12

· Pandas – Data cleaning and manipulation

· NumPy – Numerical computations

· Matplotlib & Seaborn – Static visualizations

· Plotly – Interactive visualizations

· Folium – Geospatial interactive maps

· Jupyter Notebook – Reproducible analysis environment

## 💡 Next Steps

Model prices using Linear Regression and XGBoost

Add sentiment analysis of reviews (NLP)

Build an interactive dashboard with Streamlit

## 👤 Author

📌 Sorrow Grajales
📍 Barcelona, España
🔗 [LinkedIn](https://linkedin.com/in/sforsorrow)
💻 [GitHub](https://github.com/SfromtheAbyss)

---

### ✨ "Data tells stories. Our job is to learn how to listen."”
