import sys
import pymongo
from pymongo import errors
import json
from pymongo import MongoClient


def insert_data():

    fileName = sys.argv[1]
    db_name = sys.argv[4]
    collection_name = sys.argv[5]
    ip_address = sys.argv[6] 
    with open('/root/migrationpod/configuration/linux_server_discovery.yml','a') as f:
        f.write('IP_Address: '+ip_address+' \n')
    f.close()
    
    db = client[db_name]
    collection_cmdbFact = db[collection_name]

    with open(fileName) as f:
      file_data = json.load(f)

   # Insert the data into db
    existCount =  collection_cmdbFact.find({'IP_Address':ip_address},{'_id':0,'IP_Address':1}).count()
   
    if existCount == 0:
        record_id = collection_cmdbFact.insert_one(file_data)    
        print("record inserted")
    else:
        recordUpdate = collection_cmdbFact.update({'IP_Address':ip_address},file_data)
        print("record updated")
  
    client.close()

if __name__ == '__main__':
  
    hostname = sys.argv[2]
    mongodb_port = int(sys.argv[3])
  
    try:   
      client = MongoClient(hostname,mongodb_port)
      insert_data()
  
    except pymongo.errors.ServerSelectionTimeoutError:
      print("Could not connect to MongoDB") 
    except FileNotFoundError:
      print("File does not exist.")
