
'''
  This script gives unique mac-address,ip,hostname and vendor from dhcplog and saves this information in "nodes.csv" file

'''
print(__doc__)
test=[]
items=[]
from vendors import vendors
from mac import delimit
with open('dhcplog.log','r') as log1:
#split the whole log file into a single list, each line of texts is a single item
  x=log1.read().splitlines()
  for i in range(len(x)):
#passing each line of text from dhcplog.log to "delimit" function, gives back tuple "test" = (mac, ip and hostname) or "None"
    test = delimit(x[i])
#Tuple type is returned or returns "None", choose Tuple and proceed
    if type(test) == tuple:
      v=test[0]
#an unwanted line is removed.
      if v[0] != '(':
#collecting first 8 characters(comprises of OUI) 
        z=v[0:8]
#passing this OUI to "vendors" function in module "vendors", gives back vendor name
        brand=vendors(z)
#using .join to convert tuple("test") seen above to strings separated by ',' + adding 'brand'. Appending an empty list named items[]
        items.append(','.join(test)+","+brand)
#Converting tuple to string. This is a required because open() method requires string as argument.
node1=str('\n'.join(items))
#At the end of writing the captured information, give a next line('\n') in the file for brevity
with open('nodes.csv','w') as n:
  n.write(node1+'\n')
