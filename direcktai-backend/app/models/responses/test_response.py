from pydantic import BaseModel


class CreateTestResponse(BaseModel):

    test_id: str

    title: str

    steps: list[str]