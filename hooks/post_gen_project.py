#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")
        remove_file("scripts/gen_ref_pages.py")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/deploy_dev.yml")
            remove_file(".github/workflows/deploy_prod.yml")
            remove_file(".github/scripts/versioning_script.sh")
     
    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")
    
    if "{{cookiecutter.tox}}" != "y":
        remove_file("tox.ini")
