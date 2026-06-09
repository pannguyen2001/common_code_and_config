from pathlib import Path


def create_file(
    folder_path: str = "./",
    file_name: str = "file.txt",
) -> str:
    """Create file if it does not exist."""

    file_path = Path(folder_path) / file_name

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.touch(exist_ok=True)

    return str(file_path)
