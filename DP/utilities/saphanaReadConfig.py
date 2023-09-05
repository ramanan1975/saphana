import configparser

config=configparser.RawConfigParser()
config.read("C:\MyProject\DP\Configurations\saphanaConfig.ini")

class ReadConfig:
    @staticmethod
    def getdbhostname():
        hostname=config.get('login info','db_hostname')
        return hostname

    @staticmethod
    def getdbportnumber():
        portnumber=config.get('login info','db_portnumber')
        return portnumber

    @staticmethod
    def getdbusername():
        username=config.get('login info','db_username')
        return  username

    @staticmethod
    def getdbpassword():
        password=config.get('login info','db_password')
        return password


