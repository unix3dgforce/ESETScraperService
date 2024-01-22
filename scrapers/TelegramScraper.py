import re
import datetime

from telethon.sync import TelegramClient
from telethon.tl.custom import Message

from core.interfaces import ILogService
from core.models import CredentialModel
from clients import TGClient
from exceptions import NotFoundCredentialsException
from exceptions.scraper.telegram import MessageEmptyException
from .BaseScraper import BaseScraper

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class TelegramScraper(BaseScraper):
    def __init__(self, client: TGClient, patterns: list[str], logger: ILogService):
        super().__init__(logger)
        self._client = client
        self._patterns: list[re.Pattern] = self._compile_patterns(patterns)

    def _compile_patterns(self, patterns: list[str]) -> list[re.Pattern]:
        _result = []
        for pattern in patterns:
            if not isinstance(pattern, str):
                continue

            _result.append(re.compile(pattern, re.MULTILINE))
        self.logger.debug(f'Compile of search patterns done. Number of search patterns: {len(_result)}')

        return _result

    async def processing_data(self, data: Message):
        if not data.message:
            raise MessageEmptyException

        _result = []

        for pattern in self._patterns:
            _result.append([
                CredentialModel(
                    username=match.group(1),
                    password=match.group(2))
                for match in pattern.finditer(data.text.replace('\n', ' '))
            ])

        if not _result:
            raise NotFoundCredentialsException

        # TODO: Return DTO model
        self.logger.debug(f'{_result}')
        return

    async def get_data(self):
        async for message in await self._client.get_messages(offset_date=datetime.date.today(), reverse=True):
            try:
                await self.processing_data(message)
            except (MessageEmptyException, NotFoundCredentialsException):
                continue

    async def run(self):
        await self.get_data()
