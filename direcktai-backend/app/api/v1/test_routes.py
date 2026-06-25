from fastapi import APIRouter
from app.infrastructure.mongo import MongoManager
from app.models.requests.test_request import CreateTestRequest
from app.models.responses.test_response import CreateTestResponse
from app.services.test_service import TestService

router = APIRouter()
@router.post(
    "/tests",
    response_model=CreateTestResponse
)
async def create_test(
    request: CreateTestRequest):

    service = TestService(
        MongoManager.get_database()
        )
    result = await service.create_test(
        request.workspace_id,
        request.requirement
    )
    
    return CreateTestResponse(
        **result
    )