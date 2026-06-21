import os

from git import Repo


class RepositoryService:

    def clone_repository(
        self,
        repository_url: str,
        local_path: str
    ):

        os.makedirs(
            os.path.dirname(
                local_path
            ),
            exist_ok=True
        )

        Repo.clone_from(
            repository_url,
            local_path
        )