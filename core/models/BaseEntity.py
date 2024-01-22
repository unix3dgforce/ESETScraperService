import uuid
from dataclasses import dataclass, field

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


@dataclass
class BaseEntity:
    """A base class for all entities"""
    id: uuid.UUID = field(default_factory=lambda: globals()['BaseEntity'].next_id(), kw_only=True)

    @classmethod
    def next_id(cls) -> uuid.uuid4:
        """Generates new UUID"""
        return uuid.uuid4()
