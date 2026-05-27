import os
from pathlib import Path


def create_file(folder_path: str = "", file_name: str = ""):
    """Create file or folder if not exist"""
    file_path = os.path.join(folder_path, file_name)
    file_path = Path(file_path)
    file_path.parent.mkdir(exist_ok=True, parents=True)
    return file_path
