from datetime import datetime
from pydantic import BaseModel

class WorkspaceDocument(BaseModel):
    workspace_id:str
    application_url :str
    repository_url :str
    local_repo_path: str
    created_at: datetime 