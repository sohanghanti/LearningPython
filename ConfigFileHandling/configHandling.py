from configparser import ConfigParser


cnf = ConfigParser()

cnf.read('Config.cfg')
print(type(cnf.get('Section1', 'username')))

