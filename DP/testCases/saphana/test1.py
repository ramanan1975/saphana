# Import your dependencies
from hdbcli import dbapi
from utilities.saphanaReadConfig import ReadConfig
from utilities.logger import LogGen

dbhostname      =   ReadConfig.getdbhostname()
dbportnumber    =   ReadConfig.getdbportnumber()
dbusername      =   ReadConfig.getdbusername()
dbpassword      =   ReadConfig.getdbpassword()
logger          =   LogGen.loginfo()


#Open the database conenciton
conn = dbapi.connect(address=dbhostname, port=dbportnumber,user=dbusername, password=dbpassword)

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# disconnect from server
conn.close()
#------------------END--------------