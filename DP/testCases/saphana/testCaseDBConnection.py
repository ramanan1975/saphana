# Import your dependencies
import pytest
import dbapi
from hdbcli import dbapi
from utilities.saphanaReadConfig import ReadConfig
from utilities.logger import LogGen

dbhostname = ReadConfig.getdbhostname()
dbportnumber = ReadConfig.getdbportnumber()
dbusername = ReadConfig.getdbusername()
dbpassword = ReadConfig.getdbpassword()
logger = LogGen.loginfo()
logger.info(dbhostname)
logger.info(dbportnumber)
logger.info(dbusername)
logger.info(dbpassword)

class DBoperation:

    def DBConnection(self):
        # Open the database conenciton
        logger.info("SAP HANA DB Connection check is started")
        conn = dbapi.connect(address=dbhostname, port=dbportnumber, user=dbusername, password=dbpassword)
        # prepare a cursor object using cursor() method
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            try:
                sql = "SELECT SYSTEM_ID, DATABASE_NAME, VERSION FROM M_DATABASE"
                cursor.execute(sql)
                result = cursor.fetchall()
                logger.info("Connection to SAP HANA Database successful.")
                print("SID =", result[0][0])
                print("Database Name =", result[0][1])
                print("Version =", result[0][2])
                logger.info(print("ALL =", result))

            except Exception:
                print("Connection is not proper")

        logger.info("SAP HANA DB Connection check is over")
        # disconnect from server
        conn.close()

connection=DBoperation()
connection.DBConnection()
#print(connection.DBConnection())


#==================HTML report==========================
def pytest_Configure(config):
    config._metadata['DP Module Name'] = "SAP HANA on x64"
    config._metadata['Tester Name'] = "Ramanan Marimuthu"
    config._metadata['Test Module'] = "Regression"

#@pytest.mark.optionalhook

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

