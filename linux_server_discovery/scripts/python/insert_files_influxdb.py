from influxdb import InfluxDBClient
import pandas as pd
from pandas import DataFrame
import json
import sys
import ast

client = InfluxDBClient(host='13.90.149.147', port=8086, username='grafana', password='grafana@123')
#client.create_database('pyexample1')
#client.get_list_database()
client.switch_database('pyexample1')
fileName = sys.argv[1]
with open(fileName) as f:
     d=json.load(f)
print("################################################################################")
print(type(d))
print(d)
json_body = [
    {
        "measurement": "linux_discovery",
        "tags": {
            "host": "Azure",
            "region": "us-east"
        },
        "time": "2011-11-10T23:00:00Z",
        "fields": d
    }
]


print("################################################################################")
print(json_body)
client.write_points(json_body)
#client.query("insert html_table,data="+filedata+",time=123")
results = client.query('SELECT * FROM "linux_discovery"')
print(results.raw)
#points = results.get_points(tags={'user':'Carol'})
#print(points)
#for point in points:
#    print("inside")
#    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
