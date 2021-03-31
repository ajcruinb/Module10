"""
Program: employee.py
Author: AJ Crusinberry
Last date modified: 3/30/2021
Program description:
Declares a Employee class and create and prints an object from that class.
"""


class Employee:
    """Employee Class"""
    # Constructor
    def __init__(self, lname, fname, add, phone, salaried, s_date, rate):
        """
        :param lname: Employee's Last Name
        :param fname: Employee's First Name
        :param add: Employee's Address
        :param phone: Employee's Phone Number
        :param salaried: Boolean Is employee salaried
        :param s_date: Employee's start date
        :param rate: Employee's Rate of Pay
        """
        self._last_name = lname
        self._first_name = fname
        self._address = add
        self._phone_number = phone
        self._salaried = salaried
        self._start_date = s_date
        self._salary = rate

    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self, fname):
        self._first_name = fname

    def set_address(self, add):
        self._address = add

    def set_phone_number(self, phone):
        self._phone_number = phone

    def set_salaried(self, salaried):
        self._salaried = salaried

    def set_salary(self, rate):
        self._salary = rate

    def set_start_date(self, s_date):
        self._start_date = s_date

    def display(self):
        """
        :return: a string with the employee information
        """
        sp = ' '
        nl = '\n'
        for i in range(0, len(self._address)):
            if self._address[i] == ':':
                res = i
        if self._salaried:
            salary_string = 'Salaried employee: $' + str(self._salary) + '/year'
        else:
            salary_string = 'Hourly employee: $' + str(self._salary) + '/hour'
        return str(self._first_name) + sp + str(self._last_name) + nl + str(self._address[0:res]) + nl + str(self._address[res+2:]) + nl + str(salary_string) + nl + 'Start date: ' + str(self._start_date) + nl

    def __str__(self):
        """
        :return: a string with the employee information
        """
        sp = ' '
        nl = '\n'
        for i in range(0, len(self._address)):
            if self._address[i] == ':':
                res = i
        if self._salaried:
            salary_string = 'Salaried employee: $' + str(self._salary) + '/year'
        else:
            salary_string = 'Hourly employee: $' + str(self._salary) + '/hour'
        return str(self._first_name) + sp + str(self._last_name) + nl + str(self._address[0:res]) + nl + str(self._address[res+2:]) + nl + str(salary_string) + nl + 'Start date: ' + str(self._start_date) + nl

    def __repr__(self):
        """
        :return: a string with the employee information
        """
        sp = ' '
        nl = '\n'
        for i in range(0, len(self._address)):
            if self._address[i] == ':':
                res = i
        if self._salaried:
            salary_string = 'Salaried employee: $' + str(self._salary) + '/year'
        else:
            salary_string = 'Hourly employee: $' + str(self._salary) + '/hour'
        return str(self._first_name) + sp + str(self._last_name) + nl + str(self._address[0:res]) + nl + str(self._address[res+2:]) + nl + str(salary_string) + nl + 'Start date: ' + str(self._start_date) + nl


# Driver
emp = Employee('Ruiz', 'Matthew', '123 Fake Street: Des Moines, Iowa', '555-555-5555', True, '05-10-2010', '80,000')
emp.set_first_name('Matt')
print(emp.display())
print(emp.__str__())
print(emp.__repr__())

emp.set_salaried(False)
emp.set_salary('45.00')
print(emp.display())
print(emp.__str__())
print(emp.__repr__())
del emp  # clean up!
