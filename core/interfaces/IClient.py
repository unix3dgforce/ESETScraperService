import abc

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class IClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        """Connect client to service"""

    @abc.abstractmethod
    def disconnect(self):
        """Disconnect client to service"""
