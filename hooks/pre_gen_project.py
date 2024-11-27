from __future__ import annotations

import re
import sys

PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
project_name = "{{cookiecutter.project_name}}"
if not re.match(PROJECT_NAME_REGEX, project_name):
    print(
        f"ERROR: The project name {project_name} is not a valid Python module name. Please do not use a _ and use - instead"
    )
    # Exit to cancel project
    sys.exit(1)

PROJECT_SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_slug = "{{cookiecutter.project_slug}}"
if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(
        f"ERROR: The project slug {project_slug} is not a valid Python module name. Please do not use a - and use _ instead"
    )
    # Exit to cancel project
    sys.exit(1)

TARGET_PYTHON_VERSION_REGEX = r"^3\.(9|10|11|12)$"
target_python_version = "{{cookiecutter.target_python_version}}"
if not re.match(TARGET_PYTHON_VERSION_REGEX, target_python_version):
    print(
        f"ERROR: The target python version ({target_python_version}) is not a valid Python version."
    )
    # Exit to cancel project
    sys.exit(1)