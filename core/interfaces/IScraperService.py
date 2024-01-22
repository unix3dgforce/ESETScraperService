from __future__ import annotations

import abc
from .IService import IService

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class IScraperService(IService):
    @abc.abstractmethod
    async def run(self, **kwargs):
        """Run scraper"""
