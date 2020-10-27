import pandas as pd
import os
from ast import literal_eval
import re
from collections import OrderedDict
import json
import sys
import json2html
import html.parser
import io
import pymongo
from pymongo import MongoClient
import pandas
import yaml
import shutil

input_file = sys.argv[1]
ip_file = '../../reports/ips'
ip_list = list()
with open(ip_file) as f:
  for line in f:
    ip_list.append(line)

def genericFormatter(commandOutputList):
      commandOutputFrmt = "<table><tr>"
      if not isinstance(commandOutputList, str):      
         for data in commandOutputList:
               commandOutputFrmt = commandOutputFrmt+"<td style='width:1px;white-space:nowrap;'>"+ data +"</td>"
      else:
         commandOutputFrmt = commandOutputFrmt+"<td style='width:1px;white-space:nowrap;'>"+ commandOutputList +"</td>"
      commandOutputFrmt = commandOutputFrmt + "</tr></table>"
      return commandOutputFrmt

with open(input_file, 'rb') as f:
    data = yaml.load(f.read())  

dbname=data["db_name"]
dbcol=data["collection_name"]
dbhost=data["db_host"]
dbport=str(data["db_port"])
build_number=str(data["build_number"])
#ip=str(data["IP_Address"])


with open('/root/migrationpod/configuration/trigger_usecase.yml', 'rb') as file:
    data_usecase = yaml.load(file.read())  
build_number_usecase=str(data_usecase["build_number_usecase"])

docs = pandas.DataFrame(columns=[])
client = MongoClient("mongodb://"+dbhost+":"+dbport+"/")
db = client[dbname]
collection_cmdbFact = db[dbcol]

print('Total Record for the collection: ' + str(collection_cmdbFact.count()))
doclist=[]
for ip_address in ip_list:
      ip=ip_address.strip()
      cursor = collection_cmdbFact.find({"IP_Address":ip},{"_id":0})
      #count= collection_cmdbFact.find({"IP_Address":ip},{"_id":0}).count()
      #print(count)
      mongo_docs = list(cursor)
      doclist.append(mongo_docs)
      
docs = pandas.DataFrame(columns=[])
object_list=[]
for num1, doc in enumerate(doclist):
   for num, jsonObject in enumerate(doc):
      jsonFrmObject={}
      print(jsonObject)
      for json_key in jsonObject:
          commandOutputList = jsonObject[json_key]
          final_value = genericFormatter(commandOutputList)
          jsonFrmObject[json_key] = final_value  
      object_list.append(jsonFrmObject)

df = pd.DataFrame(object_list)
df.style.set_caption(dbname)
html_output = df.to_html()
html_output=html_output.replace('&lt;', '<')
html_output=html_output.replace('&gt;', '>')
html_file= open("../../reports/Automation_Report_"+build_number+".html","w")
html_file.write(html_output)
html_file.close()
     
	 
shutil.copy("../../reports/Automation_Report_"+build_number+".html", '/var/lib/jenkins/workspace/Trigger_UseCase/trigger_usecase/reports/Automation_Report_'+dbname+'_'+build_number_usecase+'.html')
