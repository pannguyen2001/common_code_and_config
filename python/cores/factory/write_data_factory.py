from typing import Optional

from cores.strategy.write_data.base_strategy import WriteDataStrategy
from utils.logger_wrapper import logger_wrapper


class WriteDataStrategyFactory:
    def __init__(self) -> None:
        self.strategy = {}

    @logger_wrapper
    def register(self, file_type: str, strategy: WriteDataStrategy) -> None:
        file_type = file_type.lower()
        self.strategy[file_type] = strategy

    @logger_wrapper
    def get_strategy(self, file_type: str) -> Optional[WriteDataStrategy]:
        if file_type not in self.strategy.keys():
            raise ValueError(
                f"[{self.__class__.__name__}] Invalid strategy: {file_type}."
            )
        return self.strategy.get(file_type)
