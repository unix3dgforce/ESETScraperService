import re
from typing import Any

from telethon.tl.custom import Message

from clients import DMTelegramClient
from core.interfaces import ILogService
from core.models import CredentialModel, CredentialRecordDTO
from core.models.configuration import TelegramScraperConfiguration
from exceptions import NotFoundCredentialsException
from exceptions.scraper.telegram import MessageEmptyException
from .BaseScraper import BaseScraper

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class TelegramScraper(BaseScraper):
    def __init__(self, client: DMTelegramClient, configuration: dict[str, Any], logger: ILogService):
        super().__init__(logger)
        self._client = client
        self._configuration = TelegramScraperConfiguration.create_from_dict(configuration)

    def _compile_patterns(self, patterns: list[str]) -> list[re.Pattern]:
        _result = []
        for pattern in patterns:
            if not isinstance(pattern, str):
                continue

            _result.append(re.compile(pattern, re.MULTILINE))
        self.logger.debug(f'Compile of search patterns done. Number of search patterns: {len(_result)}')

        return _result

    async def processing_data(self, data: Message) -> CredentialRecordDTO:
        if not data.message:
            raise MessageEmptyException

        _result = []

        for pattern in self._configuration.patterns:
            _result.extend([
                CredentialModel(
                    username=match.group(1),
                    password=match.group(2))
                for match in pattern.finditer(data.text.replace('\n', ' '))
            ])

        if not _result:
            raise NotFoundCredentialsException

        return CredentialRecordDTO(
            message_id=data.id,
            credentials=_result,
            message_date=data.date
        )

    async def get_data(self, **kwargs) -> list[CredentialRecordDTO]:
        _result = []

        async for message in self._client.get_message(offset_date=self._configuration.offset_date, reverse=True):
            try:
                _result.append(await self.processing_data(message))
            except (MessageEmptyException, NotFoundCredentialsException):
                continue

        return _result

    async def run(self, **kwargs):
        await self.get_data(**kwargs)
