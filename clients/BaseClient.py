import abc
from typing import TypeVar

from core.interfaces import IClient, ILogService

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'

T = TypeVar('T')


class BaseClient(IClient):
    @abc.abstractmethod
    async def connect(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def disconnect(self):
        raise NotImplementedError
