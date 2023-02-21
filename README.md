# employee-payment-ioet-tech

The employee payment calculator is a command line application!

## Clone this repository
```cmd
git clone git@github.com:BrunoGehlen/employee-payment-ioet-tech.git
```

---

This task is complete
- [x] Developed in time!

- [x] Used Dependency Injection concepts

The project follows the Dependency Injection pattern, which helps to improve the code's flexibility and maintainability.

- [x] The project adheres to S.O.L.I.D. principles.

- [x] Well documented:

The project has been thoroughly documented to make it easy for anyone to understand and modify the code.


----
# Application Design

| Type     | Name         | Description                                                                                                  | Path                  |
|------------|--------------|--------------------------------------------------------------------------------------------------------------|-----------------------|
| Model      | Payment      | The Payment model calculates the total payment for the worker.                                             | models/payment.py     |
| Model      | WorkEntry    | The WorkEntry model receives the work hours and calculates the time that the worker spent working for each shift (dawn, regular hours, and night hours). | models/work_entry.py |
| Model      | Worker       | The Worker model uses both PaymentModel and WorkEntryModel to process worker data. Calling worker methods once can create the report over all their worked hours. | models/worker.py      |
| Module     | config       | The config module contains classes that tell the application how much a worker should be paid for each shift hour and define the time ranges for each shift. This module facilitates configuration and changes in the code. | config/classes/*      |
| Class      | WorkerController | The WorkerController class handles the dependency injection of the instantiation of Worker and presents the data to the user. This is the only module that imports the models, this avoid circular imports exceptions. | controller.py         |
| Module     | application.py | The application.py module starts the application, reads the file, and groups the worker data.              | application.py        |

----


# ACME Employee Payment Calculator

The ACME company offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Day           | Time           | Rate  |
| -------------|:--------------:| -----:|
| Monday - Friday | 00:01 - 09:00 | 25 USD|
|               | 09:01 - 18:00 | 15 USD|
|               | 18:01 - 00:00 | 20 USD|
| Saturday - Sunday | 00:01 - 09:00 | 30 USD|
|               | 09:01 - 18:00 | 20 USD|
|               | 18:01 - 00:00 | 25 USD|

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. 

## Input

The input should be a `.txt` file with at least five sets of data, where each set contains the name of an employee and the schedule they worked, indicating the time and hours. The following abbreviations should be used for entering data:

| Abbreviation | Day           |
| ------------ |:-------------:|
| MO           | Monday        |
| TU           | Tuesday       |
| WE           | Wednesday     |
| TH           | Thursday      |
| FR           | Friday        |
| SA           | Saturday      |
| SU           | Sunday        |

Here is an example of what the input file should look like:

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


## Output

The program will output the amount of money that the employee has to be paid based on the schedule they worked. The output will be formatted as follows:

The amount to pay [NAME] is: [AMOUNT] USD


## How to Run the Program

To run the program, you will need to have Python 3 installed on your computer. 

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project in your terminal.
3. Run the program by executing the following command: `python main.py /path/to/your/file.txt`


---

Happy calculating! 
