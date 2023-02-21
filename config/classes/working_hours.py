from datetime import time


class WorkingHours:
    """
    Represents the time periods for different work shifts.

    Attributes:
        periods (dict): A dictionary that maps the names of the work shift periods to tuples
            that represent the start and end times of those periods.
            Valid names for the periods are: "dawn_period", "regular_work_hours_period",
            and "evening_work_hours_period".
    """
    def __init__(self) -> None:
        """
        Initializes a new instance of the WorkingHours class with default values for the periods.
        """
        self.periods = {
            "dawn_period": (time(hour=0, minute=1), time(hour=9, minute=0)),
            "regular_work_hours_period": (time(hour=9, minute=1), time(hour=18, minute=0)),
            "evening_work_hours_period": (time(hour=18, minute=1), time(hour=23, minute=59)),
        }
