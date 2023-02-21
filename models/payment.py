from config.classes.payment_rates import PaymentRates


class Payment(PaymentRates):
    """
    Class that calculates the payment for a worker based on their working hours.
    
    Args:
        PaymentRates: Inherits the rates to be applied to each type of shift.
        working_hours (list): List of dictionaries with the working hours of the worker.

    Attributes:
        working_hours (list): List of dictionaries with the working hours of the worker.

    Methods:
        calculate_entry_payment(entry): Calculates the payment for a single shift based on its working hours and shift type.
        calculate_payment(): Calculates the total payment for all the shifts of the worker.
    """
    
    def __init__(self, working_hours):
        super().__init__()
        self.working_hours = working_hours

    def calculate_entry_payment(self, entry):
        """
        Calculates the payment for a single shift based on its working hours, shift type and if 
        it's weekend or regular day.

        Args:
            entry: A dictionary representing the work day entry, containing a
                boolean "is_weekend" field and a "working_hours" field with the
                number of working hours for each period.

        Returns:
            float: Total payment for the entry.
        """
        
        return sum([
            self.rates[period][entry['is_weekend']] * hours
            for period, hours in entry['working_hours'].items()
        ])

    def calculate_payment(self):
        """
        Calculates the total payment for all the shifts of the worker.

        Returns:
            float: Total payment.
        """
        return sum([
            self.calculate_entry_payment(entry) for entry in self.working_hours
        ])
