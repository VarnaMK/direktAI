import json

from app.services.llm_service import (
    LLMService
)

from app.agents.agent_models import (
    RequirementAnalysis
)


class RequirementAgent:

    def __init__(self):

        self.llm = LLMService()

    def execute(
        self,
        requirement: str
    ) -> RequirementAnalysis:
        print("\nRequirement Agent Running...")
        prompt = f"""
You are a QA Architect.

Analyze the requirement.

Return ONLY valid JSON.

Format:

{{
    "title": "",
    "goal": "",
    "business_context": ""
}}

Requirement:

{requirement}
"""

        result = (
            self.llm.invoke(
                prompt
            )
        )

        data = json.loads(
            result
        )

        return RequirementAnalysis(
            **data
        )