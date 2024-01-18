import datetime
from telethon import TelegramClient
from telethon.tl.custom import Message
from typing import AsyncIterator

from core.interfaces import ILogService
from core.models.configuration import TelegramClientCredentialModel
from .BaseClient import BaseClient

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class TGClient(BaseClient):
    def __init__(self, configuration: dict[str, any], logger: ILogService):
        self._logger: ILogService = logger
        self._configuration: TelegramClientCredentialModel = TelegramClientCredentialModel(**configuration)
        self._client = TelegramClient(self._configuration.name, self._configuration.api_id, self._configuration.api_hash)

    def connect(self):
        pass

    def disconnect(self):
        pass

    async def get_messages(self, **kwargs) -> AsyncIterator[Message]:
        async with self._client:
            async for message in self._client.iter_messages(self._configuration.channel_id, offset_date=datetime.date.today(), reverse=True):
                yield message
