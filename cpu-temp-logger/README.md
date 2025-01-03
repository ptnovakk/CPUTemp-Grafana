# CPU Temperature Logger

This project logs CPU temperature data into an InfluxDB database. It consists of a Python script that reads the CPU temperature and sends the data to InfluxDB for storage and analysis.

## Project Structure

```
cpu-temp-logger
├── src
│   ├── cput.py          # Main logic for logging CPU temperature data
│   └── influxdb_client.py # Handles connection to InfluxDB
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd cpu-temp-logger
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure InfluxDB:**
   Ensure you have an InfluxDB instance running. Update the connection settings in `src/influxdb_client.py` as needed.

## Usage

To start logging CPU temperature data, run the following command:
```
python src/cput.py
```

The script will log the CPU temperature every second and store the data in the configured InfluxDB database.

## Notes

- Ensure that the user running the script has permission to read the CPU temperature.
- You may need to adjust the logging interval in `src/cput.py` based on your requirements.
- For more advanced configurations, refer to the InfluxDB documentation.