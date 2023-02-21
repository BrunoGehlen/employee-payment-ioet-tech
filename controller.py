from models.payment import Payment
from models.work_entry import WorkerEntry
from models.worker import Worker


class WorkerController:
    """
    A controller responsible for handling dependency injection of worker, worker entry and payment models.

    Attributes:
        work_entry_model (WorkerEntry): A model for a worker's work entry.
        payment_model (Payment): A model for calculating worker's payment.
        worker_model (Worker): A model for a worker.
        workers (list): A list of worker models.
        
    Methods:
        make_worker(worker): Create a worker model based on provided data.
        make_workers(workers): Create a list of worker models based on provided data.
        present(): Prints out the amount to be paid to each worker.
    """
    
    def __init__(self, workers) -> None:
        self.work_entry_model: WorkerEntry = WorkerEntry
        self.payment_model: Payment = Payment
        self.worker_model: Worker = Worker
        self.workers = self.make_workers(workers)
        
    def make_worker(self, worker):
        """
        Create a worker model based on provided data.
        
        Args:
            worker (dict): A dictionary containing worker name and service hours.
            
        Returns:
            Worker: A worker model instance.
        """

        for worker_name, service_hours in worker.items():
            return self.worker_model(
                name=worker_name,
                service_hours=service_hours,
                work_entry_model=WorkerEntry,
                payment_model=Payment
            )

    def make_workers(self, workers):
        return [
            self.make_worker(worker_data) for worker_data in workers
        ]

    def present(self):
        """
        Prints out the amount to be paid to each worker.
        """
        for worker in self.workers:
            print(f"The amount to pay {worker.name}  is: {worker.get_payment()} USD")








