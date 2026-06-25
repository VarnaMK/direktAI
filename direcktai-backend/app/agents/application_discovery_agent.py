from app.services.mcp_service import (
    MCPService
)

from app.agents.agent_models import (
    ApplicationDiscovery
)


class ApplicationDiscoveryAgent:

    def __init__(self):

        self.mcp_service = (
            MCPService()
        )

    def execute(
        self,
        application_url: str
    ):
        print("\nDiscovery Agent Running...")
        result = (
            self.mcp_service
            .discover_application(
                application_url
            )
        )

        return ApplicationDiscovery(
            **result
        )