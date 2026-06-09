import os
from copy import copy
from string import Template
from typing import Dict, List, Union

import openpyxl
import polars as pl
from loguru import logger

from utils.logger_wrapper import logger_wrapper

from .base_strategy import WriteDataStrategy

write_successfully_template = Template(
    """Write data to parquet file successfully. File: ${file_path}."""
)


class WriteToParquetStrategy(WriteDataStrategy):
    def __init__(self, df: Union[[Dict, List[Dict]], pd.DataFrame], file_path: str):
        super().__init__(df, file_path)

    @logger_wrapper
    def write_data(
        self,
        *args,
        **kwargs,
    ) -> None:
        pl.write_parquet(self.file_path, mkdir=True, *args, **kwargs)

        logger.success(
            f"Write data to parquet file successfully. File: ${self.file_path}."
        )
