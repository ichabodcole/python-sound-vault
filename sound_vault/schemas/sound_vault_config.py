from typing import List, Optional
from pydantic import BaseModel


class SoundVaultEntry(BaseModel):
    id: str
    name: str
    file_name: str
    format: str
    description: str
    tags: List[str] = []
    source: Optional[str] = None
    license: Optional[str] = None
    is_modified: Optional[bool] = False


class SoundVaultConfig(BaseModel):
    format_version: str
    last_updated: int
    sounds_dir: str
    sounds: List[SoundVaultEntry]
