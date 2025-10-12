import random
from collections import deque
import csv
import pandas as pd
import streamlit as st

headers = ["Hour", "Temperature", "Humidity", "Light", "soil_moisture", "CO2",
           "Watering", "Alert", "Shading", "Recommendation", "Critical Flag"]

with open("greenhouse_log.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)


def log_to_csv(hour, data, decision, filename="greenhouse_log.csv"):
    rows = [
        hour,
        data["temperature"],
        data["humidity"],
        data["light"],
        data["soil_moisture"],
        data["co2"],
        decision["watering"],
        decision["alert_triggered"],
        decision["shading"],
        decision["recommendation"],
        decision["critical_flag"]
    ]
    try:
        with open(filename, "x", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(rows)
    except FileExistsError:
        with open(filename, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(rows)
    
NUM_INTERVALS = 10
SOIL_HISTORY_WINDOW = 3

def generate_sensor_data():
    return {
        "temperature": random.randint(20, 42),
        "humidity": random.randint(15, 60),
        "light": random.randint(100, 1300),
        "soil_moisture": random.randint(20, 90),
        "co2": random.randint(900, 1300),
    }

def decide_watering( temp, humidity, soil):
    if soil <35 and (humidity < 40 or temp > 30):
        return "Start watering"
    elif 35 <= soil <= 50 and temp > 35:
        return "Light watering"
    elif soil > 70:
        return "Skip watering"
    return "No watering"

def decide_shading(light):
    if light < 300:
        return "Open shades"
    elif 300 <= light < 800:
        return "No action "
    elif 800 < light <= 1000:
        return " Close partially"
    elif light > 1000:
        return "Close fully"
    
def assess_risk(temp, humidity, co2, soil, light):
    conditions = [
        temp > 36,
        humidity < 25,
        soil < 30,
        co2 > 1200,
        light > 1100
    ]
    count = sum(conditions)
    return count >= 3, count

def moving_average(data, window):
    if len(data) < window:
        return sum(data) / len(data) 
    return sum(data[-window:]) / window

def recommend_watering(avg_moisture):
    if avg_moisture < 40:
        return " Recommend early irrigation next interval"
    elif avg_moisture >70:
        return " Hold watering for next interval"
    return "Moisture level acceptable"

def run_simulator():
    alert_streak = 0
    soil_history = deque(maxlen=SOIL_HISTORY_WINDOW)

    for hour in range (1, NUM_INTERVALS +1):
        data = generate_sensor_data()

        soil_history.append(data["soil_moisture"])

        watering = decide_watering(data["temperature"], data["humidity"], data["soil_moisture"])
        shading = decide_shading(data["light"])
        alert_triggered, risk_count = assess_risk(
            data["temperature"],
            data["humidity"],
            data["co2"],
            data["soil_moisture"],
            data["light"]
        )

        alert_streak = alert_streak + 1 if alert_triggered else 0
        critical_flag = alert_streak > 2
        avg_moisture = moving_average(list(soil_history), SOIL_HISTORY_WINDOW)
        recommendation = recommend_watering(avg_moisture)
    
        print(f"\n🌿 Interval {hour}")
        print(f"Sensors → Temp: {data['temperature']}°C, Humidity: {data['humidity']}%, "
              f"Light: {data['light']} lux, Soil: {data['soil_moisture']}%, CO₂: {data['co2']} ppm")
        print(f"🚿 Watering: {watering}")
        print(f"🌞 Shading: {shading}")
        print(f"⚠️ Alert: {'Yes' if alert_triggered else 'No'} ({risk_count}/5 conditions met)")
        if critical_flag:
            print("🔥 Critical Risk Flag: TRIGGERED")
        print(f"📊 Dashboard Recommendation: {recommendation}")

        decision = {
            "watering": watering,
            "shading": shading,
            "alert_triggered": "Yes" if alert_triggered else "No",
            "recommendation": recommendation,
            "critical_flag": "🔥 Critical" if critical_flag else "Normal"
        }

        log_to_csv(hour, data, decision)
def main():
    run_simulator()
    
    df = pd.read_csv("greenhouse_log.csv")
    df.columns = df.columns.str.strip()

    st.title("Smart Greenhouse Dashboard")
    df = pd.read_csv("greenhouse_log.csv")

    st.subheader("Sensor Data & AI Decisions")
    st.dataframe(df)

    st.subheader("Soil Moisture Trends")
    st.line_chart(df["soil_moisture"])

    st.subheader("Risk Alerts Over Time")
    st.bar_chart(df["Alert"].value_counts())
 

if __name__ == "__main__":
    main()
