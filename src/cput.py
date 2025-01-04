import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
import os

# Function to get CPU temperature
def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp = f.read()
        return float(temp) / 1000.0

# Function to log temperature data to InfluxDB
def log_temperature(client):
    while True:
        temp = get_cpu_temp()
        point = Point("cpu_temperature").field("value", temp)
        client.write_api(write_options=WritePrecision.NS).write(bucket=influxdb_bucket, org=influxdb_org, record=point)
        print(f"Logged temperature: {temp}°C")
        time.sleep(1)  # Log temperature every second

if __name__ == "__main__":
    influxdb_url = os.getenv('INFLUXDB_URL')    # Set the environment variables prior to running the script!
    influxdb_token = os.getenv('INFLUXDB_TOKEN')
    influxdb_org = os.getenv('INFLUXDB_ORG')
    influxdb_bucket = os.getenv('INFLUXDB_BUCKET')

    client = InfluxDBClient(url=influxdb_url, token=influxdb_token)
    log_temperature(client)