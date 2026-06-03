import datetime
import os
from enum import Enum
from pathlib import Path

import pytz
from dotenv import load_dotenv

from utils.create_file import create_file

# # ========== Load environment variables from .env file ==========
load_dotenv()
BASE_FOLDER: str = os.path.dirname(os.path.abspath(__file__))
LOG_FOLDER: str = os.getenv("LOG_FOLDER") or BASE_FOLDER
ERROR_LOG_FOLDER: str = os.getenv("ERROR_LOG_FOLDER") or BASE_FOLDER
DATA_FOLDER: str = os.getenv("DATA_FOLDER") or BASE_FOLDER
REPORT_FOLDER: str = os.getenv("REPORT_FOLDER") or BASE_FOLDER


# ========== Timezone config ==========
class DatetimeEnum(str, Enum):
    DATE_FORMAT_TYPE_1 = "%Y-%m-%d"
    DATE_TIME_FORMAT_TYPE_1 = "%Y-%m-%d %H:%M:%S"
    DATE_TIME_FORMAT_TYPE_2 = "%Y-%m-%d %H-%M-%S"


local_timezone = pytz.timezone("Asia/Ho_Chi_Minh")
date_today = datetime.datetime.now().strftime(DatetimeEnum.DATE_FORMAT_TYPE_1.value)
datetime_today_type_1 = datetime.datetime.now().strftime(
    DatetimeEnum.DATE_TIME_FORMAT_TYPE_1.value
)
datetime_today_type_2 = datetime.datetime.now().strftime(
    DatetimeEnum.DATE_TIME_FORMAT_TYPE_2.value
)
