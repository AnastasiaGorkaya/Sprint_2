class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
        
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        EmployeeSalary.hourly_payment = new_hourly_payment

    def salary(self):
        hourly_payment = EmployeeSalary.hourly_payment
        salary = self.hours * hourly_payment
        return salary