import sys
import os
import logging.handlers
sys.path.insert(0, os.path.join(os.getcwd(), '..'))
import common.variables as variables

LOG_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), variables.LOG_DIRECTORY)
LOG_FILE = os.path.join(LOG_DIRECTORY, variables.LOG_SERVER_NAME)

LOGGER = logging.getLogger('server')
LOGGER.setLevel(logging.DEBUG)

FORMAT = logging.Formatter('%(asctime)-10s %(levelname)-10s %(filename)-10s %(message)s')

STDERR_HANDLER = logging.StreamHandler(sys.stderr)
STDERR_HANDLER.setLevel(logging.INFO)
STDERR_HANDLER.setFormatter(FORMAT)

FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(LOG_FILE, encoding='utf-8', interval=1, when='S')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMAT)

LOGGER.addHandler(STDERR_HANDLER)
LOGGER.addHandler(FILE_HANDLER)

if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
    LOGGER.warning('Внимание')
