from core.interfaces import IScraper, ILogService

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class BaseScraper(IScraper):
    def __init__(self, logger: ILogService):
        self.logger = logger
