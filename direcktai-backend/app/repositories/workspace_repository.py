class WorkspaceRepository:

    def __init__(self, db):
        self.collection = db.workspaces

    async def create(self, workspace: dict):
        await self.collection.insert_one(
            workspace
        )

    async def get_by_workspace(self, workspace_id: str):
        return await self.collection.find_one(
            {"workspace_id": workspace_id}
        )
    
    async def get_all(self):
        cursor = self.collection.find()
        return await cursor.to_list(length=None)