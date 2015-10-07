import logging
import logging.config
import loggly.handlers

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('EnjoyEvents')

logger.info("{event:'lolla'}")
logger.error('"Error"')
logger.warning('"Warning"')
