import datetime
import os
from pathlib import Path

import pytz
from dotenv import load_dotenv
from utils.create_file import create_file

# # ========== Load environment variables from .env file ==========
# load_dotenv()

# # Access environment variables
# database_url = os.getenv('DATABASE_URL')
# api_key = os.getenv('API_KEY')
# debug_mode = os.getenv('DEBUG')

# print(f"Database URL: {database_url}")
# print(f"API Key: {api_key}")
# print(f"Debug Mode: {debug_mode}")

# ========== Timezone config ==========
local_timezone = pytz.timezone("Asia/Ho_Chi_Minh")
date_format = "%Y-%m-%d"
datetime_format = "%Y-%m-%d %H:%M:%S"

# ========== Logging config ===========
today = datetime.datetime.now().strftime(date_format)
log_file = f"{today}.log"
log_folder = "./logs"
output_log_file = create_file(log_folder, log_file)

# Debug
error_log_file = "tracking_error.log"
error_log_file = create_file(log_folder, error_log_file)

# ========== Database config ===========
# Test database
db_folder: str = "./database/test"
raw_db_file_path: str = create_file(db_folder, "raw.db")
brozen_db_file_path: str = create_file(db_folder, "brozen.db")
silver_db_file_path: str = create_file(db_folder, "silver.db")
golden_db_file_path: str = create_file(db_folder, "golden.db")
test_db_file_path: str = create_file(db_folder, "test.db")

# ========== Data ==========
data_folder: str = "./data/test"
raw_data_folder: str = create_file(data_folder, "raw")
brozen_data_folder: str = create_file(data_folder, "brozen")
silver_data_folder: str = create_file(data_folder, "silver")
golden_data_folder: str = create_file(data_folder, "golden")

# ========== Report ==========
report_folder_path: str = "./reports"
report_file_name: str = "report.xlsx"
report_folder: str = create_file(report_folder_path, report_file_name)
