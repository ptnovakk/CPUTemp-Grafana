import time
from influxdb import InfluxDBClient

# Function to get CPU temperature
def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp = f.read()
        return float(temp) / 1000.0

# Function to log temperature data to InfluxDB
def log_temperature(client):
    while True:
        temp = get_cpu_temp()
        json_body = [
            {
                "measurement": "cpu_temperature",
                "fields": {
                    "value": temp
                }
            }
        ]
        client.write_points(json_body)
        print(f"Logged temperature: {temp}°C")
        time.sleep(1)  # Log temperature every second

if __name__ == "__main__":
    client = InfluxDBClient(host='localhost', port=8086, database='cpu_data')
    log_temperature(client)