from pydantic import BaseModel

class WorkspaceCreateResponse(BaseModel):
    workspace_id : str
    status: str