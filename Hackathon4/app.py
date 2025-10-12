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