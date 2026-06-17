class WorkspaceRepository:

    def __init__(self, db):
        self.collection = db.workspaces

    async def create(self, workspace):
        await self.collection.insert_one(
            workspace
        )

    async def get(self, workspace_id):
        return await self.collection.find_one(
            {"workspace_id": workspace_id}
        )