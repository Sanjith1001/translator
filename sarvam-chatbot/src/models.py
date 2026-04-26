from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class User:
    user_id: str
    username: str
    email: str
    password_hash: str
    created_at: datetime
    preferred_language: Optional[str] = None
    is_active: bool = True


@dataclass(slots=True)
class Session:
    session_id: str
    user_id: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    primary_language: Optional[str] = None
    message_count: int = 0
    is_archived: bool = False


@dataclass(slots=True)
class Message:
    message_id: str
    session_id: str
    role: str
    content: str
    language_code: Optional[str] = None
    token_count: Optional[int] = None
    model_used: Optional[str] = None
    sequence_num: int = 1
