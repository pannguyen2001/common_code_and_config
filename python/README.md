# Install and config

## 1. Install and setup .venv using uv, pyproject.toml or poetry

1. uv init: crate project.toml
2. uv sync: create uv.loc, .venv based on pyproject.toml
3. activate .venv: (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& <absolute_path_to_folder>\.venv\Scripts\Activate.ps1)
3. uv add <package name>: install package
