import uuid, os
from datetime import datetime, UTC
from app.models.documents.workspace_document import WorkspaceDocument
from app.repositories.workspace_repository import WorkspaceRepository
from app.services.repository_service import RepositoryService
from app.services.repository_validator_service import RepositoryValidatorService
from app.services.framework_bootstrap_service import FrameworkBootstrapService

class WorkspaceService:
    def __init__(self, database):
        self.workspace_repository = (WorkspaceRepository(database))
        self.repository_service = (RepositoryService())
        self.repository_validator = (RepositoryValidatorService())
        self.framework_bootstrap_service = (FrameworkBootstrapService())

    async def create_workspace(self, application_url: str, repository_url :str):
        is_valid = (self.repository_validator.validate_repository_accessible(repository_url))
    
        if not is_valid:
            raise Exception("Repository is not accessible")

        workspace_id = str(
            uuid.uuid4()
        )

        local_repo_path = os.path.join(
            "generated",
            "repos",
            workspace_id
        )

        self.repository_service.clone_repository(
            repository_url,
            local_repo_path
        )
        self.framework_bootstrap_service.bootstrap(
            local_repo_path,
            workspace_id,
            application_url
        )

        document = WorkspaceDocument(
            workspace_id=workspace_id,
            application_url=application_url,
            repository_url=repository_url,
            local_repo_path=local_repo_path,
            created_at=datetime.now(UTC)
        )

        await self.workspace_repository.create(document.model_dump())

        return workspace_id