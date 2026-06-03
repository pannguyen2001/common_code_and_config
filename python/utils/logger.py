import sys

from loguru import logger

from configs.constants import (
    ERROR_LOG_FOLDER,
    LOG_FOLDER,
    date_today,
    datetime_today_type_2,
)

from .create_file import create_file

# Log
log_file: str = create_file(LOG_FOLDER, f"{date_today}.log")
# Debug
error_log_file: str = create_file(ERROR_LOG_FOLDER, f"{datetime_today_type_2}.log")

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
    format="<level>{level.icon}</level><level> {level}</level>[<green>{time:YYYY-MM-DD HH:mm:ss}</green>][<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>]\n{message}",
    backtrace=True,
    diagnose=True,
)

logger.add(
    log_file,
    rotation="1 week",
    retention="1 month",
    level="DEBUG",
    format="<level>{level.icon:<2}</level>[{time:YYYY-MM-DD HH:mm:ss}][{name}:{function}:{line}]\n{message}",
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

# # Serialize log for send to email, slack,...
# logger.add(
#     "./logs/serialize_log.log",
#     rotation="1 week",
#     retention="1 month",
#     level="INFO",
#     backtrace=True,
#     diagnose=True,
#     mode="w",
#     serialize=True,
# )
