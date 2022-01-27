import log.client_log.client_log_config
# import common.decos
import logging


LOGER = logging.getLogger('client')

# @log
def my_fun():
    LOGER.debug('test1')
    LOGER.debug('test2')
    LOGER.debug('test3')

my_fun()