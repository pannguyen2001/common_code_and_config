from typing import Dict, Optional, Union

import polars as pl
import pyarrow.parquet as pq

from .base_strategy import ReadDataStrategy


class ReadParquetFileStrategy(ReadDataStrategy):
    def __init__(self, file_path: str = "") -> None:
        super().__init__(file_path)

    def load(self, *args, **kwargs) -> Optional[Union[Dict, pl.DataFrame]]:
        return pl.scan_parquet(self.file_path, *args, **kwargs).collect()
