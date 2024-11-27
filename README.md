# Python template - Cookiecutter

This is a Cookiecutter template that is used by the Giorgio Armani - Data Strategy and Analytics team to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/)
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [tox-uv](https://github.com/tox-dev/tox-uv)
- Containerization with [Docker](https://www.docker.com/)



## Getting Started

In order to keep the project aligned with possible updates on the template, it is adviced to use [cruft](https://github.com/cruft/cruft) instead of cookiecutter to create an instance of the template.

1. Install cruft:
    `pip install cruft`

2. Create a repository from template: `cruft create https://github.com/ga-data-strategy-analytics/cookiecutter-python-uv-template.git` and configure the project

3. Configure git and create a branch to push on the related data collection repository:
    ```bash
    cd <PROJECT_NAME>
    git init
    git checkout -b <BRANCH_NAME>
    git add .
    git commit -m "Initial setup from template"
    git remote add origin git@github.com:<GITHUB_AUTHOR_HANDLE>/<PROJECT_NAME>.git
    git fetch
    git branch --set-upstream-to=origin/<BRANCH_NAME> <BRANCH_NAME>
    git merge origin/<BRANCH_NAME> --allow-unrelated-histories
    git push -u origin <BRANCH_NAME>
    ```

4. Finally, install the environment and the pre-commit hooks with
    ```bash
    make install
    ```

5. You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

## Update repo from template

If you want to update an already existing repo in a local folder, and reflect the latest updated made on the template, use the following commands (make sure you use the same configurations set for the repo you are working on):
```
cd <PROJECT_NAME>
cruft update
make uv-lock
make check
git add .
git commit -m "Refactor from template"
git push
```

## Acknowledgements

This project is partially based on [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv)
repository.
