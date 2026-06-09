import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Union

import pandas as pd

from utils.logger import logger
from utils.logger_wrapper import logger_wrapper


class WriteDataStrategy(ABC):
    def __init__(
        self, df: Union[[Dict, List[Dict]], pd.DataFrame], file_path: str
    ) -> None:
        self.df = df
        self.file_path = file_path

        if self.df is None or self.df.empty:
            logger.warning(f"[{self.__class__.__name__}] data is empty")
            return
        if not os.path.exists(self.file_path):
            logger.info(
                f"[{self.__class__.__name__}] file/folder is not exists. Create new: {self.file_path}."
            )
            output_file = Path(self.file_path)
            output_file.parent.mkdir(exist_ok=True, parents=True)

    @abstractmethod
    @logger_wrapper
    def write_data(
        self,
        *args,
        **kwargs,
    ) -> None:
        """Write data to file or database.

        Args:
            df (Union[[Dict, List[Dict]], pd.DataFrame]): data needs writing.
            file_name (str): file path locates.
        """
        logger.info(
            f"[{self.__class__.__name__}] Write data to file: {self.file_path}."
        )
        pass

    @logger_wrapper
    def run(
        self,
        *args,
        **kwargs,
    ) -> None:
        """Run function to write data.

        Args:
            df (Union[[Dict, List[Dict]], pd.DataFrame]): data needs writing.
            file_path (str): file path locates.
        """

        self.write_data(self.df, self.file_path, *args, **kwargs)
