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
    
    async def update_local_repo_path(self, workspace_id: str, local_repo_path: str):
        await self.collection.update_one(
            {
                "workspace_id": workspace_id
            },
            {
                "$set": {
                    "local_repo_path": local_repo_path
                }
            }
        )