from datetime import datetime

from pydantic import BaseModel


class TestDocument(BaseModel):

    test_id: str

    workspace_id: str

    requirement: str

    title: str

    steps: list[str]

    created_at: datetime