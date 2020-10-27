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
'''
json_body =[{'measurement': 'linux_discovery', 
             'tags': {'host': 'Azure', 'region': 'us-eat'},
             'time': '2019-11-10T23:00:00Z', 
             'fields': {
                  'IP_Address': '172.17.0.5', 
                  'hostname': 'e68839da4e0d', 
                  'OS_Info': '', 
                  'Kernel_Version': '4.18.0-193.28.1.el8_2.x86_64', 
                  'Total_Processor': '4', 
                  'RUNNING_SERVICE_INFO': '', 
                  'TOTAL_RUNNING_SERVICE_INFO': 0, 
                  'ACTIVE_USER_INFO': ''
             }
            }
           ]
'''
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
