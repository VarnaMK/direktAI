from pydantic import BaseModel


class CreateTestRequest(BaseModel):

    workspace_id: str

    requirement: str