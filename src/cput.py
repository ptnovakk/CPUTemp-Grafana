from influxdb import InfluxDBClient
import time
import os

# Function to get CPU temperature
def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp = f.read()
        return float(temp) / 1000.0

# Function to log temperature data to InfluxDB
def log_temperature(client):
    while True:
        try:
            temp = get_cpu_temp()
            json_body = [
                {
                    "measurement": "cpu_temperature",
                    "tags": {
                        "host": "pi3"
                    },
                    "fields": {
                        "value": temp
                    }
                }
            ]
            client.write_points(json_body)
            print(f"Logged temperature: {temp}°C")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(1)  # Log temperature every second

if __name__ == "__main__":
    influxdb_host = os.getenv('INFLUXDB_HOST', 'localhost')
    influxdb_port = int(os.getenv('INFLUXDB_PORT', '8086'))
    influxdb_database = os.getenv('INFLUXDB_DATABASE', 'rpidata')
    influxdb_username = os.getenv('INFLUXDB_USERNAME')
    influxdb_password = os.getenv('INFLUXDB_PASSWORD')

    client = InfluxDBClient(host=influxdb_host, port=influxdb_port, 
                            username=influxdb_username, password=influxdb_password, 
                            database=influxdb_database)

    try:
        log_temperature(client)
    except KeyboardInterrupt:
        print("\nScript interrupted by user, exiting gracefully.")
    finally:
        # Any cleanup code, like closing connections, goes here if needed
        client.close()