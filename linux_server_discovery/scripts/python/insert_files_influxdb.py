from influxdb import InfluxDBClient
import pandas as pd
from pandas import DataFrame
import json
import sys
import ast

client = InfluxDBClient(host='13.90.149.147', port=8086, username='grafana', password='grafana@123', database='pyexample1')
fileName = sys.argv[1]
with open(fileName) as f:
     d=json.load(f)
json_body = [
    {
        "measurement": "linux_discovery",
        "tags": {
            "host": "Azure",
            "region": "us-east"
        },
        "fields": d
    }
]
client.write_points(json_body)
#results = client.query('SELECT * FROM "linux_discovery"')
#print(results.raw)
#points = results.get_points(tags={'user':'Carol'})
#print(points)
#for point in points:
#    print("inside")
#    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
