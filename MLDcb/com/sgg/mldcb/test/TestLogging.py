import logging
import logging.config

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("demo")
logger.info('Start reading database')
# read database here

records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here

logger.info('Finish updating records')