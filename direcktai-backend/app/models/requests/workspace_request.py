from pydantic import BaseModel
from pydantic import HttpUrl

class WorkspaceCreateRequest(BaseModel):
    application_url: HttpUrl
    repository_url: str
