import sys
import traceback
from functools import wraps
from typing import Callable

import snoop
from configs.constants import error_log_file, output_log_file
from loguru import logger

# ========== Format message ==========
"""
This message format is used for logging data pipeline, for clear phase and action. If not need clear so much, just simple create logger and use, no ned bind

[MESSAGE_LEVEL] [datetime] [file_execute - line] - [DATA_PIPELINE_PHASE] [Sub phase] message
Description:
MESSAGE_LEVEL: DEBUG, INFO, WARNING,ERROR, CRITICAL: upper case, bold
DATA_PIPELINE_PHASE: COLLECTION, INGESTION, COMPUTING, STORAGE, CONSUMPTION, MANAGEMENT, GOVERNANCE
SERCURITY
OTHER
COMMON
Sub phase: ex: in collection: validate source, ingestion: quality, computing: cleaning,...
Datetime: YYYY-MM-DD HH:MM:SS
Message: clear content: error, info, variable: a = 1, ... beautiful format, if dict, use json.dumps() python
Can sort, filter, pagination by datetime, level, data pipeline phase, sub phase
"""

# === Configure Loguru ===
# create log
logger.remove()
logger.level(name="DEBUG", color="<blue><bold>", icon="🔍")
logger.level(name="INFO", color="<green><bold>", icon="💡")
logger.level(name="SUCCESS", color="<cyan><bold>", icon="😀")
logger.level(name="WARNING", color="<yellow><bold>", icon="❕")
logger.level(name="ERROR", color="<red><bold>", icon="❌")
logger.level(name="CRITICAL", color="<white><bold>", icon="🚫")

logger.add(
    sys.stdout,
    colorize=True,
    level="DEBUG",
    format="<level>{level.icon}</level><level> {level}</level> [<level>{extra[project]}</level>][<level>{extra[phase]}:{extra[sub_phase]}</level>][<green>{time:YYYY-MM-DD HH:mm:ss}</green>][<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>]\n{message}",
    backtrace=True,
    diagnose=True,
)

logger.add(
    output_log_file,
    rotation="1 week",
    retention="1 month",
    level="DEBUG",
    format="<level>{level.icon:<2}</level>[{level}][{extra[project]}][{extra[phase]}:{extra[sub_phase]}][{time:YYYY-MM-DD HH:mm:ss}][{name}:{function}:{line}]\n{message}",
    backtrace=True,
    diagnose=True,
    mode="a",
)
# just for filter easier, can remove when complete debugging
logger.add(
    error_log_file,
    rotation="1 week",
    retention="1 month",
    level="WARNING",
    format="<level>{level.icon:<2}</level>[{level}][{extra[project]}][{extra[phase]}:{extra[sub_phase]}][{time:YYYY-MM-DD HH:mm:ss}][{name}:{function}:{line}]\n{message}",
    backtrace=True,
    diagnose=True,
    mode="w",
)

# Serialize log for send to email, slack,...
logger.add(
    "./logs/serialize_log.log",
    rotation="1 week",
    retention="1 month",
    level="INFO",
    backtrace=True,
    diagnose=True,
    mode="w",
    serialize=True,
)


logger = logger.bind(project="Prj1_MRDP")
common_phase_logger = logger.bind(phase="COMMON")
collection_phase_logger = logger.bind(phase="COLLECTION")
ingestion_phase_logger = logger.bind(phase="INGESTION")
computing_phase_logger = logger.bind(phase="COMPUTING")
storage_phase_logger = logger.bind(phase="STORAGE")
consumption_phase_logger = logger.bind(phase="CONSUMPTION")
management_phase_logger = logger.bind(phase="MANAGEMENT")
governance_phase_logger = logger.bind(phase="GOVERNANCE")

# Sub phase common
other_common_logger = common_phase_logger.bind(sub_phase="")
exception_alert_logger = common_phase_logger.bind(sub_phase="exception")
waring_alert_logger = common_phase_logger.bind(sub_phase="alert")


# ========== Logger wrapper ==========


def logger_wrapper(func: Callable) -> Callable:
    """
    Decorator to log exceptions and return None

    Args:
        func (Callable): input function

    Returns:
        Callable: function with logger
    """

    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            # return func(*args, **kwargs)
            result = func(
                *args, **kwargs
            )  # function should return True as default if has no return value
            if not result:
                waring_alert_logger.warning(f"[{func.__name__}] return None")
        except Exception as e:
            # tb = "".join(traceback.format_exception(None, e, e.__traceback__))
            exception_alert_logger.error(f"[{func.__name__}] {e}")
            return None

    return wrap
