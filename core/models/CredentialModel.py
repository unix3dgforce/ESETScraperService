from pydantic.dataclasses import dataclass


@dataclass
class CredentialModel:
    username: str
    password: str
