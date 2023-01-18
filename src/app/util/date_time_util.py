from datetime import datetime

class DateTimeUtil:
    @staticmethod
    def string_to_date(date_str: str, format: str = '%Y-%m-%dT%H:%M:%S') -> datetime:
        return datetime.strptime(date_str, format)

    @staticmethod
    def date_to_iso_string(date: datetime) -> str:
        return date.isoformat()

    @staticmethod
    def date_to_string(date: datetime, format: str = '%Y-%m-%dT%H:%M:%S') -> str:
        return date.strftime(format)
