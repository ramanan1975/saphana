import logging

class LogGen:
    @staticmethod
    def loginfo():
        logging.basicConfig(filename="C:\MyProject\DP\Logs\DebugLog.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m:%d:%y %I:%M:%S %p' )
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def logwarn():
        logging.basicConfig(filename="C:\MyProject\DP\Logs\DebugLog.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m:%d:%y %I:%M:%S %p' )
        logger=logging.getLogger()
        logger.setLevel(logging.WARN)
        return logger

    @staticmethod
    def logerror():
        logging.basicConfig(filename="C:\MyProject\DP\Logs\DebugLog.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m:%d:%y %I:%M:%S %p' )
        logger=logging.getLogger()
        logger.setLevel(logging.ERROR)
        return logger

    @staticmethod
    def logfatal():
        logging.basicConfig(filename="C:\MyProject\DP\Logs\DebugLog.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m:%d:%y %I:%M:%S %p' )
        logger=logging.getLogger()
        logger.setLevel(logging.FATAL)
        return logger

    @staticmethod
    def logcritical():
        logging.basicConfig(filename="C:\MyProject\DP\Logs\DebugLog.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m:%d:%y %I:%M:%S %p' )
        logger=logging.getLogger()
        logger.setLevel(logging.CRITICAL)
        return logger