import shutil
from pathlib import Path

from git import Repo
from git.exc import GitCommandError


class RepositoryValidatorService:

    def validate_repository_accessible(
        self,
        repository_url: str
    ) -> bool:

        temp_path = Path(
            "temp_validation_repo"
        )

        try:

            Repo.clone_from(
                repository_url,
                temp_path,
                depth=1
            )

            return True

        except GitCommandError:

            return False

        finally:

            if temp_path.exists():

                shutil.rmtree(
                    temp_path,
                    ignore_errors=True
                )