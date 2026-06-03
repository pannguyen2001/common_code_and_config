import json
from typing import Dict, List, Optional, Union

import polars as pl

from .base_strategy import ReadDataStrategy


class ReadJsonFileStrategy(ReadDataStrategy):
    def __init__(self, file_path: str = "") -> None:
        super().__init__(file_path)

    def load(self, *args, **kwargs) -> Optional[Union[Dict, List]]:
        return pl.read_json(self.file_path, infer_schema_length=0, *args, **kwargs)
