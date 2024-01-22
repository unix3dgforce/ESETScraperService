from __future__ import annotations
import re
import datetime
import pytz
from dataclasses import dataclass, field, fields

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


@dataclass
class TelegramScraperConfiguration:
    limit_days: int
    patterns: list[re.Pattern] | list[str] = field(default_factory=list)
    timezone: datetime.tzinfo | str = field(default=None)

    @classmethod
    def create_from_dict(cls, dict_) -> TelegramScraperConfiguration:
        class_fields = {f.name for f in fields(cls)}
        return TelegramScraperConfiguration(**{k: v for k, v in dict_.items() if k in class_fields})

    @property
    def offset_date(self) -> datetime.datetime:
        return datetime.datetime.today() - datetime.timedelta(days=self.limit_days)

    def __post_init__(self):
        self._validate_limit_days()
        self._validate_timezone()
        self._compile_patterns()

    def _validate_limit_days(self):
        pass

    def _validate_timezone(self):
        if isinstance(self.timezone, str):
            self.timezone = pytz.timezone(self.timezone)

    def _compile_patterns(self):
        _result = []
        for pattern in self.patterns:
            if not isinstance(pattern, str):
                continue

            _result.append(re.compile(pattern, re.MULTILINE))

        self.patterns = _result
