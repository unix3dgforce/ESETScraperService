from pydantic.dataclasses import dataclass

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


@dataclass
class TelegramClientCredentialModel:
    name: str
    api_id: int
    api_hash: str
    channel_id: str
