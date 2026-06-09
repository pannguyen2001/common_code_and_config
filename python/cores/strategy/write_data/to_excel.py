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
    """Write data to excel file successfully. Sheet name: ${sheet_name}. File: ${file_path}."""
)


class WriteToExcelStrategy(WriteDataStrategy):
    def __init__(self, df: Union[[Dict, List[Dict]], pl.DataFrame], file_path: str):
        super().__init__(df, file_path)

    @logger_wrapper
    def write_data(
        self,
        *args,
        **kwargs,
    ) -> None:
        pl.write_excel(self.file_path, *args, **kwargs)

        logger.success(
            f"Write data to excel file successfully. Sheet name: ${kwargs.get('sheet_name')}. File: {self.file_path}."
        )
