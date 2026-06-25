import uuid
from datetime import datetime, UTC
from app.repositories.test_repository import TestRepository
from app.models.documents.test_document import TestDocument
from app.services.openai_service import OpenAIService

class TestService:

    def __init__(
        self,
        database
    ):

        self.repository = (TestRepository(database))

        self.openai_service = (OpenAIService())

    async def create_test(
        self,
        workspace_id: str,
        requirement: str
    ):

        generated = (
            self.openai_service
            .generate_steps(
                requirement
            )
        )

        test_id = str(
            uuid.uuid4()
        )

        document = TestDocument(
            test_id=test_id,
            workspace_id=workspace_id,
            requirement=requirement,
            title=generated["title"],
            steps=generated["steps"],
            created_at=datetime.now(UTC)
        )

        await self.repository.create(
            document.model_dump()
        )

        return {
            "test_id": test_id,
            "title": generated["title"],
            "steps": generated["steps"]
        }