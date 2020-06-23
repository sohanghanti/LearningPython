# import logging
from Logging import Logger

# the level mentioned in the below statement as a parameter will indicate that all the logs which are equal
# and above the value mentioned( e.g. level= DEBUG) will be logged
# logs can be taken into the txt file as per the first parameter mentioned below, else logs will be shown in the output
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='report.html')
# log = logging.getLogger()
# logging.disable(logging.CRITICAL)
# by above statement all the logs which are and below CRITICAL level will be disabled
# five levels of logs are there:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

log = Logger.setLog(r'C:\pyCharmProjects\Project_Structure\report.html')

log.info('\nstart of program\n')


def factorial(num):
    log.info('\n start of factorial(%s)\n' % num )
    total = 1
    for i in range(1, num + 1):
        total = total * i
        log.debug('\n i is %s, total is %s\n' % (i, total))

        log.debug('\n return value is %s\n' % total)
    return total


f = factorial(5)
print(f)
log.info('\n End of program\n')
