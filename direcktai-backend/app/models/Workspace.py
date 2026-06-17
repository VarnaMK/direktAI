from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class WorkspaceCreateRequest(BaseModel):
    application_url: str
    repository_url: str


class Workspace(BaseModel):
    workspace_id: str
    application_url: str
    repository_url: str
    local_repo_path: str
    created_at: datetime