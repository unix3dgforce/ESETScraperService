import dataclasses
from datetime import datetime

from core.models import LogLevel

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


@dataclasses.dataclass
class LogMessageModel:
    level: LogLevel
    text: str
    time: datetime
