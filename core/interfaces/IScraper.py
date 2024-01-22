import abc

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class IScraper(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def run(self, **kwargs):
        """Run scrapper"""
