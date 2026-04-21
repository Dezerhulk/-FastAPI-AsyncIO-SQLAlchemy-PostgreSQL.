from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TaskState(str, Enum):
    pending = "pending"
    processing = "processing"
    done = "done"
    error = "error"


class TaskCreate(BaseModel):
    data: str = Field(..., min_length=1, max_length=1000)


class TaskStatus(BaseModel):
    id: str
    status: TaskState
    result: Optional[str] = None


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=100)


class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=100)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserInfo(BaseModel):
    username: str
