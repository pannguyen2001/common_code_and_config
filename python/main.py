from configs.constants import (
    ERROR_LOG_FOLDER,
    LOG_FOLDER,
    REPORT_FOLDER,
    DatetimeEnum,
    datetime_today_type_2,
)
from utils.cleanup_file_or_folder import cleanup_file_or_folder
from utils.create_file import create_file
from utils.logger import logger


def main():
    # Cleanup old files
    cleanup_file_or_folder(
        REPORT_FOLDER,
        days=3,
        dry_run=False,
        name_format=DatetimeEnum.DATE_FORMAT_TYPE_1,
    )
    cleanup_file_or_folder(
        LOG_FOLDER, days=3, dry_run=False, name_format=DatetimeEnum.DATE_FORMAT_TYPE_1
    )
    cleanup_file_or_folder(
        ERROR_LOG_FOLDER,
        minutes=10,
        dry_run=False,
        name_format=DatetimeEnum.DATE_TIME_FORMAT_TYPE_2,
    )

    # Create new report
    create_file(REPORT_FOLDER, f"{datetime_today_type_2}_report.csv")


if __name__ == "__main__":
    main()
