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
json_body =[{'measurement': 'linux_discovery', 
             'tags': {'host': 'Azure', 'region': 'us-eat'},
             'time': '2019-11-10T23:00:00Z', 
             'fields': {
                  'IP_Address': ['172.17.0.5'], 
                  'hostname': ['e68839da4e0d'], 
                  'OS_Info': [], 
                  'Kernel_Version': ['4.18.0-193.28.1.el8_2.x86_64'], 
                  'Total_Processor': ['4'], 
                  'CPU_Processor_Model': [' Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz', ' Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz', ' Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz', ' Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz'], 
                  'CPU_Processor_Speed': [' 2095.078', ' 2095.078', ' 2095.078', ' 2095.078'], 
                  'CPU_Cache_Size': [' 36608 KB', ' 36608 KB', ' 36608 KB', ' 36608 KB'], 
                  'Memory_RAM_Info': ['              total        used        free      shared  buff/cache   available', 'Mem:           15Gi       4.9Gi       7.6Gi        41Mi       3.0Gi        10Gi', 'Swap:            0B          0B          0B', 'Total:         15Gi       4.9Gi       7.6Gi'], 
                  'MOUNT_POINT_TYPE': ['/dev/mapper/rootvg-varlv xfs      8.0G  7.3G  714M  92% /ansible_playbooks'], 
                  'BLOCK_DEVICES': ['NAME    FSTYPE LABEL UUID FSAVAIL FSUSE% MOUNTPOINT', 'sda                                      ', '├─sda1                                   ', '├─sda2                                   ', '├─sda14                                  ', '└─sda15                                  ', 'sdb                                      ', '└─sdb1                                   '], 'DISK_PARTATION_INFO': ['Filesystem                Size  Used Avail Use% Mounted on', 'overlay                   8.0G  7.3G  714M  92% /', 'tmpfs                      64M     0   64M   0% /dev', 'tmpfs                     7.8G     0  7.8G   0% /sys/fs/cgroup', 'shm                        64M  136K   64M   1% /dev/shm', '/dev/mapper/rootvg-varlv  8.0G  7.3G  714M  92% /ansible_playbooks', 'tmpfs                     7.8G     0  7.8G   0% /proc/acpi', 'tmpfs                     7.8G     0  7.8G   0% /proc/scsi', 'tmpfs                     7.8G     0  7.8G   0% /sys/firmware'], 'DISK_PARTATION_INF': ['/dev/mapper/rootvg-varlv on /ansible_playbooks type xfs (rw,relatime,seclabel,attr2,inode64,noquota)', '/dev/mapper/rootvg-varlv on /etc/resolv.conf type xfs (rw,relatime,seclabel,attr2,inode64,noquota)', '/dev/mapper/rootvg-varlv on /etc/hostname type xfs (rw,relatime,seclabel,attr2,inode64,noquota)', '/dev/mapper/rootvg-varlv on /etc/hosts type xfs (rw,relatime,seclabel,attr2,inode64,noquota)'], 
                  'RUNNING_SERVICE_INFO': [], 
                  'TOTAL_RUNNING_SERVICE_INFO': ['0'], 
                  'ACTIVE_USER_INFO': []
             }
            }
           ]
'''
[
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

'''
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
