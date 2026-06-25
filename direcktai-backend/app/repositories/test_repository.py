class TestRepository:

    def __init__(
        self,
        database
    ):

        self.collection = database.tests

    async def create(
        self,
        test_document: dict
    ):

        await self.collection.insert_one(
            test_document
        )

    async def get_by_id(
        self,
        test_id: str
    ):

        return await self.collection.find_one(
            {
                "test_id": test_id
            }
        )