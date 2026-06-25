import json

from app.services.llm_service import (
    LLMService
)

from app.agents.agent_models import (
    RequirementAnalysis,
    ApplicationDiscovery,
    StepGeneration
)


class StepGenerationAgent:

    def __init__(self):

        self.llm = LLMService()

    def execute(

        self,

        requirement_analysis: RequirementAnalysis,

        application_discovery: ApplicationDiscovery

    ):

        prompt = f"""
You are a Senior QA Architect.

Generate test steps.

Goal:

{requirement_analysis.goal}

Application Pages:

{application_discovery.pages}

Application Navigation:

{application_discovery.navigation_paths}

Application Actions:

{application_discovery.actions}

Return ONLY valid JSON.

Format:

{{
    "steps": []
}}
If application structure is unavailable,
generate high-level generic steps only.
Do not assume page names.
Do not assume navigation paths.
"""
        print("\nStep Generation Agent Running...")
        result = (
            self.llm.invoke(
                prompt
            )
        )

        data = json.loads(
            result
        )

        return StepGeneration(
            **data
        )