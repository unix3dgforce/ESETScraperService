from core.interfaces import ILogService
from .BaseScraper import BaseScraper

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class TelegramScraper(BaseScraper):
    def __init__(self, configuration: dict[str, any], logger: ILogService):
        super().__init__(logger)
        self._configuration = configuration
