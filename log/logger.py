import logging
import logging.config
import loggly.handlers

def getLogger():
	logging.config.fileConfig('log/loggly.conf')
	return logging.getLogger('EnjoyEvents')
