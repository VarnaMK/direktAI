from app.agents.requirement_agent import (
    RequirementAgent
)

from app.agents.application_discovery_agent import (
    ApplicationDiscoveryAgent
)

from app.agents.step_generation_agent import (
    StepGenerationAgent
)


class TestCreationService:

    def __init__(self):

        self.requirement_agent = (
            RequirementAgent()
        )

        self.discovery_agent = (
            ApplicationDiscoveryAgent()
        )

        self.step_agent = (
            StepGenerationAgent()
        )

    def create_test(
        self,
        requirement: str,
        application_url: str
    ):

        requirement_analysis = (
            self.requirement_agent.execute(
                requirement
            )
        )

        application_discovery = (
            self.discovery_agent.execute(
                application_url
            )
        )

        step_generation = (
            self.step_agent.execute(
                requirement_analysis,
                application_discovery
            )
        )

        return {

            "requirement_analysis":
                requirement_analysis,

            "application_discovery":
                application_discovery,

            "step_generation":
                step_generation
        }