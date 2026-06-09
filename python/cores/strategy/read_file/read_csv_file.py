from typing import Dict, List, Optional, Union

import polars as pl

from .base_strategy import ReadDataStrategy


class ReadCSVFileStrategy(ReadDataStrategy):
    def __init__(self, file_path: str = "") -> None:
        super().__init__(file_path)

    def load(self, *args, **kwargs) -> Optional[Union[Dict, pl.DataFrame]]:
        return pl.scan_csv(
            self.file_path,
            has_header=True,
            infer_schema_length=0,
            encoding="utf8-lossy",
            *args,
            **kwargs,
        ).collect()
