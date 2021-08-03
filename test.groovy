Active choice reactive parameter
Name hostnames

Properties properties = new Properties()
File propertiesFile = new File('/mnt/aedstspidoplrs01/Cisco_Firewalls.properties')
def stream = propertiesFile.newDataInputStream()
properties.load(stream)

Enumeration e = properties.propertyNames();

List<String> list = Collections.list(e);

return list


---------------------------------------------------------


Active choice reactive parameter

Name access_list_name

Properties properties = new Properties()
File propertiesFile = new File('/mnt/aedstspidoplrs01/Cisco_Firewalls.properties')
def stream = propertiesFile.newDataInputStream()
properties.load(stream)

Enumeration e = properties.propertyNames();

List<String> list = Collections.list(e);

return list


refernced parameter: hostnames 

-----------------------------------------------------------

