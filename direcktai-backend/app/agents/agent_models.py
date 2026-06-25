from pydantic import BaseModel


class RequirementAnalysis(BaseModel):

    title: str

    goal: str

    business_context: str


class ApplicationDiscovery(BaseModel):

    pages: list[str]

    navigation_paths: list[str]

    actions: list[str]

    locators: dict


class StepGeneration(BaseModel):

    steps: list[str]