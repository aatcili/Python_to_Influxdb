import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from time import time, sleep

bucket = "mybucket"
org = "my_org"
token = "my_token"
# Store the URL of your InfluxDB instance
url="http://localhost:9000"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

end_time = time() + 300 # time() is calculated in seconds
y_seconds = 5 # time to sleep in seconds
while time() < end_time:
    # time to add data to database
    p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.1 + np.random.randn())
    sleep(y_seconds)
    write_api.write(bucket=bucket, org=org, record=p)


# Now we are done. You can check the data on your influxdb database now