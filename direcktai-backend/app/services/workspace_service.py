import uuid
from datetime import datetime, UTC
from app.models.documents.workspace_document import WorkspaceDocument
from app.repositories.workspace_repository import WorkspaceRepository

class WorkspaceService:
    def __init__(self, database):
        self.workspace_repository = (WorkspaceRepository(database))

    async def create_workspace(self, application_url: str, repository_url :str):
        workspace_id = str(uuid.uuid4())
        document = WorkspaceDocument(
            workspace_id = workspace_id,
            application_url =  application_url,
            repository_url = repository_url,
            local_repo_path = "",
            created_at =datetime.now(UTC)
        )
        await self.workspace_repository.create(document.model_dump())
        return workspace_id