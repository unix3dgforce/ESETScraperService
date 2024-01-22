import datetime
from dataclasses import dataclass, field
from typing import Optional

from .CredentialModel import CredentialModel

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


@dataclass(frozen=True)
class CredentialRecordDTO:
    message_id: Optional[int] = field(default=None, kw_only=True)
    credentials: list[CredentialModel] = field(default_factory=list, kw_only=True)
    message_date: datetime.datetime = field(default=datetime.datetime.utcnow(), kw_only=True)
