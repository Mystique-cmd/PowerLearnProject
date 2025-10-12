# 🌱 Smart Greenhouse Simulator & Dashboard

This project simulates a **smart greenhouse monitoring system** that generates synthetic sensor data, makes automated decisions (watering, shading, risk alerts), logs results to a CSV file, and visualizes everything in a **Streamlit dashboard**.

---

## 🚀 Features

- **Sensor Simulation**  
  Randomly generates values for:
  - Temperature (°C)  
  - Humidity (%)  
  - Light (lux)  
  - Soil Moisture (%)  
  - CO₂ (ppm)  

- **Decision Engine**  
  - Watering recommendations (`Start watering`, `Light watering`, `Skip watering`, `No watering`)  
  - Shading control (`Open shades`, `Close fully`, etc.)  
  - Risk assessment with critical flagging  

- **Data Logging**  
  - Logs all sensor readings and AI decisions into `greenhouse_log.csv`  
  - Includes recommendations and critical alerts  

- **Dashboard (Streamlit)**  
  - Interactive table of sensor data & decisions  
  - Soil moisture trend line chart  
  - Risk alert frequency bar chart  

---

## 📂 Project Structure

. ├── greenhouse_log.csv # Auto-generated log file ├── app.py # Main script (this code) └── README.md # Project documentation

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/smart-greenhouse.git
   cd smart-greenhouse
## Creating a virtual environment( Recommendation )
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

## Install Dependencies
pip install -r requirements.txt


