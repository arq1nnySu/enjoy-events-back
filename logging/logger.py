import logging
import logging.config
import loggly.handlers

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('EnjoyEvents')

logger.info('Info')
logger.error('Error')
logger.warning('Warning')
