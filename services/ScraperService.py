from core.interfaces import IScraperService, IScraper, ILogService

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class ScraperService(IScraperService):
    def __init__(self, scrapers: dict[str, IScraper], logger: ILogService):
        self._scrapers = scrapers
        self._logger = logger

    def run(self):
        pass
