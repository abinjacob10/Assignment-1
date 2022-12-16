This script named script.sh analyzes each line of log from file named dhcplog.log and gives back unique (MAC address, IP, host and the vendor of host).
This information is at the end written to a nodes.csv file


Code structure: 
1) main code is "main.py", there are other modules namely "mac" and "vendor" 
2) In "mac" module is a function called "delimit" which takes at a time single line of log as an argument from dhcp.log, processes the passed line 
     ,if mac address is unique, function "delimit" returns a tuple of (mac,ip,hostname,vendor), if not unique, it returns "none".
3) Next, from the returned tuple, OUI of mac is extracted and passed to another function called "vendor" in module "vendor". This is done as described in next line.. 
     first six hexadecimals XX:XX:XX of mac adddress is extracted from the mac address. These six hexadecimals separated by delimiter ":" is called OUI.
4) Vendor function is used to perform a lookup based on the existing dictionary of "OUI" as key and "vendor" as "value". 
     Vendor function returns the "vendor" or "brand" name of the OUI that it found from the keys.
5) This returned brand is appended to the tuple in main.py.
6) Tuple is converted to string in main.py with a next line after each item(mac,ip,hostname, vendor).
7)  Finally this string of (mac,ip,hostname and vendor) is written to nodes.csv file.
