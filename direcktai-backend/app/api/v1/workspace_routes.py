from fastapi import APIRouter
from app.infrastructure.mongo import MongoManager
from app.models.requests.workspace_request import WorkspaceCreateRequest
from app.models.responses.workspace_response import WorkspaceCreateResponse
from app.services.workspace_service import WorkspaceService
from fastapi import HTTPException

router = APIRouter()

@router.post(
    "/workspaces",
    response_model=WorkspaceCreateResponse
)
async def create_workspace(
    request: WorkspaceCreateRequest
):

    try:
        service = WorkspaceService(
            MongoManager.get_database()
        )

        workspace_id = (
            await service.create_workspace(
                str(request.application_url),
                request.repository_url
            )
        )

        return WorkspaceCreateResponse(
            workspace_id=workspace_id,
            status="created"
        )

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )