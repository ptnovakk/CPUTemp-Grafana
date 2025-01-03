import sqlite3
import time

# Function to get CPU temperature
def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp = f.read()
        return float(temp) / 1000.0

# Function to manage database size
def manage_database_size(conn, max_rows=5000):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM cpu_temp")
    count = c.fetchone()[0]
    
    if count >= max_rows:
        # Find the timestamp of the oldest row that would be kept
        c.execute(f"SELECT timestamp FROM cpu_temp ORDER BY timestamp DESC LIMIT 1 OFFSET {max_rows - 1}")
        cutoff_time = c.fetchone()[0]
        
        # Delete rows older than the cutoff
        c.execute("DELETE FROM cpu_temp WHERE timestamp < ?", (cutoff_time,))
        conn.commit()

# Connect to SQLite database
conn = sqlite3.connect('rpi_data.db')
c = conn.cursor()

try:
    while True:
        temp = get_cpu_temp()
        c.execute("INSERT INTO cpu_temp (temperature) VALUES (?)", (temp,))
        conn.commit()
        
        # Manage database size
        manage_database_size(conn)
        
        print(f"Logged temperature: {temp}°C")
        time.sleep(1)  # Log temperature every second
except KeyboardInterrupt:
    print("Logging stopped by user")
finally:
    conn.close()