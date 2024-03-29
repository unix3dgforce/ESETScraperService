from typing import Any, Callable
from loguru import logger

from core.interfaces import ILogService
from core.models import LogLevel

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class LoguruLoggingService(ILogService):
    def __init__(self, configuration: dict[Any: Any]):
        self._logger_id = logger.configure(**configuration)

    @property
    def get_current_logger(self):
        return logger

    @classmethod
    def add_logger_sink(cls, func: Callable, **kwargs):
        logger.add(func, **kwargs)

    @classmethod
    def log(cls, level: LogLevel, message: str, exception: Exception = None):
        match level:
            case LogLevel.Critical:
                logger.critical(message)
            case LogLevel.Debug:
                logger.debug(message)
            case LogLevel.Error:
                logger.error(message)
            case LogLevel.Info:
                logger.info(message)
            case LogLevel.Trace:
                logger.trace(message)
            case LogLevel.Warning:
                logger.warning(message)


