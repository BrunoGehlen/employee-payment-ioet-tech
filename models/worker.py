from datetime import datetime
from typing import List


class Worker:
    """
    A class representing a worker and their work hours.

    Attributes:
        name (str): The name of the worker.
        service_hours (List[str]): A list of strings representing the worker's work schedule.
            Each string contains one or more work hour ranges for a given day, separated by commas.
            The day of the week is indicated by a two-letter code (e.g. 'MO' for Monday).
            Each range is indicated by two times separated by a hyphen (e.g. '09:00-17:00').
        work_entry (type): The model to use for representing individual work entries.
        payment (type): The model to use for calculating payment.

    Methods:
        make_work_entry(work_hours_str: str) -> dict:
            Converts a string representing work hours for a single day into a dictionary
            that can be used to create a work entry object.

            Args:
                work_hours_str (str): A string representing the worker's work hours for a single day,
                    formatted as a two-letter day code followed by one or more time ranges separated by commas.

            Returns:
                A dictionary containing the start and end times of each work period, as well as
                a boolean indicating whether the day is a weekend day.

        @property
        work_entries -> List[dict]:
            Converts the worker's work schedule into a list of work entry dictionaries.

            Returns:
                A list of dictionaries representing individual work entries for the worker.

        get_payment() -> float:
            Calculates the total payment for the worker based on their work schedule.

            Returns:
                A float representing the total payment due to the worker.
    """
    def __init__(self, name, service_hours, *args, **dependencies) -> None:
        self.work_entry = dependencies.pop("work_entry_model")
        self.payment = dependencies.pop("payment_model")
        self.name = name
        self.service_hours = service_hours

    def make_work_entry(self, work_hours_str):
        """
        Converts a string representing work hours for a single day into a dictionary
        that can be used to create a work entry object.

        Args:
            work_hours_str (str): A string representing the worker's work hours for a single day,
                formatted as a two-letter day code followed by one or more time ranges separated by commas.

        Returns:
            A dictionary containing the start and end times of each work period, as well as
            a boolean indicating whether the day is a weekend day.
        """

        is_weekend = work_hours_str[:2] in ["SA", "SU"]
        start_time_str, end_time_str = work_hours_str[2:].split('-')

        start_work_hours = datetime.strptime(
            start_time_str, '%H:%M').time()
        end_work_hours = datetime.strptime(
            end_time_str, '%H:%M').time()

        work_hours = {
            'start_work_hours': start_work_hours,
            'end_work_hours': end_work_hours
        }

        return self.work_entry(**work_hours, is_weekend=is_weekend).to_dict()

    @property
    def work_entries(self) -> List[dict]:
        """
        Returns a list of dictionaries representing work entries made by the worker.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary contains information of 
            the start and end times of the work and whether the work was performed on a 
            weekend or not.
        """
        return [
            self.make_work_entry(work_hours_str)
            for work_day in self.service_hours
            for work_hours_str in work_day.split(',')
        ]

    def get_payment(self):
        """
        Calculates the payment due to the worker for their work entries.

        Returns:
            float: The payment due to the worker, calculated based on the hours worked and the payment model 
            associated with the worker.
        """
        return self.payment(working_hours=self.work_entries).calculate_payment()
