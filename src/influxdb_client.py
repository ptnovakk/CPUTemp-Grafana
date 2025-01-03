import influxdb

class InfluxDBClient:
    def __init__(self, host='localhost', port=8086, database='cpu_data'):
        self.client = influxdb.InfluxDBClient(host=host, port=port, database=database)
        self.database = database
        self.create_database()

    def create_database(self):
        if self.database not in self.client.get_list_database():
            self.client.create_database(self.database)

    def write_data(self, temperature):
        json_body = [
            {
                "measurement": "cpu_temperature",
                "tags": {
                    "host": "rpi"
                },
                "fields": {
                    "value": temperature
                }
            }
        ]
        self.client.write_points(json_body)