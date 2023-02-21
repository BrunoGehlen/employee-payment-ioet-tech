from constants import hour_costs


class PaymentRates:
    """
    Calculates the hourly rates for each type of work hour period (regular, evening, and dawn),
    based on whether the period is on a weekend or not.

    Attributes:
    -----------
    rates : dict
        A dictionary containing the hourly rates for each period and weekend status.
        The keys are period names and the values are dictionaries with boolean keys representing
        weekend status (True for weekends, False for workdays) and values representing the hourly rates.
    """

    def __init__(self) -> None:
        self.rates = {
            'regular_work_hours_period': {
                True: hour_costs.WEEKEND_REGULAR_HOURS_RATE,
                False: hour_costs.WORK_DAY_REGULAR_HOURS_RATE
            },
            'evening_work_hours_period': {
                True: hour_costs.WEEKEND_EVENING_HOURS_RATE,
                False: hour_costs.WORK_DAY_EVENING_HOURS_RATE
            },
            'dawn_period': {
                True: hour_costs.WEEKEND_DAWN_HOURS_RATE,
                False: hour_costs.WORK_DAY_DAWN_HOURS_RATE
            }
        }