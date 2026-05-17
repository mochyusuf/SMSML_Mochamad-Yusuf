import pandas as pd
import requests
import time

# Load data
df = pd.read_csv("data_rumah_preprocessing.csv")
payload = {
    "dataframe_split": {
        "columns": list(df.columns),
        "data": df.values.tolist()
    }
}

url = "http://127.0.0.1:8000/predict"
headers = {"Content-Type": "application/json"}

print("Loop data ke Exporter")
for i in range(100): 
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Request {i+1} - Status: {response.status_code}")
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")