import abc
from typing import TypeVar
from core.interfaces import IScraper, ILogService

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'

T = TypeVar('T')
M = TypeVar('M')


class BaseScraper(IScraper):
    def __init__(self, logger: ILogService):
        self.logger = logger

    @abc.abstractmethod
    async def get_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def processing_data(self, data: T) -> M:
        raise NotImplementedError
