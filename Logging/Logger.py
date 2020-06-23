import logging


def setLog(filename):
    # level = ConfigReader.readConfigFile('Logs', 'LOG_LEVEL')
    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    log = logging.getLogger()
    return log