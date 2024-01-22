import functools
import types
from typing import AsyncIterator

from telethon import TelegramClient
from telethon.tl.custom import Message

from core.interfaces import ILogService, IClient
from core.models.configuration import TelegramClientCredentialModel
from .BaseClient import BaseClient

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


def processing(func):
    @functools.wraps(func)
    async def wrapped(client: IClient, *args, **kwargs):
        try:
            await client.connect()
            _instance = func(client, *args, **kwargs)
            if isinstance(_instance, types.AsyncGeneratorType):
                async for _ in _instance:
                    yield _
        finally:
            await client.disconnect()

    return wrapped


class DMTelegramClient(BaseClient):
    def __init__(self, configuration: dict[str, any], logger: ILogService):
        self._logger: ILogService = logger
        self._configuration: TelegramClientCredentialModel = TelegramClientCredentialModel(**configuration)
        self._client = TelegramClient(self._configuration.name, self._configuration.api_id, self._configuration.api_hash)

    async def connect(self):
        if not self._client.is_connected():
            await self._client.connect()

    async def disconnect(self):
        if self._client.is_connected():
            await self._client.disconnect()

    @processing
    async def get_message(self, **kwargs) -> AsyncIterator[Message]:
        async for message in self._client.iter_messages(self._configuration.channel_id, **kwargs):
            yield message

