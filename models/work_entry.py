from config.classes.working_hours import WorkingHours
from utils.converter_tools import time_to_delta_time


class WorkerEntry(WorkingHours):
    """
    A class representing a worker's entry for a specific day, including their working hours.

    Inherits from `WorkingHours` class to make use of the predefined working periods.

    Attributes:
        is_weekend (bool): A boolean indicating whether the worker's entry is for a weekend day.
        start_work_hours (datetime.time): The start time of the worker's working hours.
        end_work_hours (datetime.time): The end time of the worker's working hours.

    Methods:
        calculate_working_hours(period): Calculates the number of working hours within a given period.
        working_hours: Returns the number of working hours for each part of the day.
        to_dict(): Returns a dictionary representation of the `WorkerEntry` object.

    Usage example:
        worker_entry = WorkerEntry(
            is_weekend=True,
            start_work_hours=datetime.time(hour=9, minute=0),
            end_work_hours=datetime.time(hour=17, minute=0)
        )
    """
    def __init__(self, is_weekend, start_work_hours, end_work_hours) -> None:
        super().__init__()
        self.start_work_hours = start_work_hours
        self.end_work_hours = end_work_hours
        self.is_weekend = is_weekend

    def calculate_working_hours(self, period):
        """
        Calculate the number of working hours within a given period.

        Args:
            period: A tuple containing the start and end times of the period.

        Returns:
            A float representing the number of working hours within the period.
        """
        start, end = period
        overlap = (
            min(
                time_to_delta_time(end).total_seconds(),
                time_to_delta_time(self.end_work_hours).total_seconds()) -
            max(
                time_to_delta_time(start).total_seconds(),
                time_to_delta_time(self.start_work_hours).total_seconds()
            )) / 3600

        return overlap if overlap > 0 else 0

    @property
    def working_hours(self):
        """
        Get the number of working hours for each part of the day.

        Returns:
            A tuple containing the number of working hours for the dawn period,
            regular work hours period, and evening work hours period, respectively.
        """

        return {
            period_name: self.calculate_working_hours(period)
            for period_name, period in self.periods.items()
        }

    def to_dict(self):
        """
        Serialize the model instance to type dict.
        """
        return {
            "is_weekend": self.is_weekend,
            "working_hours": self.working_hours
        }
