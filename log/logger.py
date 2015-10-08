import logging
import logging.config
import loggly.handlers

def getLogger():
	logging.config.fileConfig('log/loggly.conf')
	return logging.getLogger('EnjoyEvents')

#logger.info("{event:'lolla'}")
#logger.error('"Error"')
#logger.warning('"Warning"')
