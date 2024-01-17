from __future__ import annotations

import abc
from typing import TypeVar

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class IScraperService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        """Run scraper"""
