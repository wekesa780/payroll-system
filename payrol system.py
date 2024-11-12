
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("Subclasses must implement this method")



class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)  
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary



class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)  
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate



class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)  
        self.commission = commission

    def calculate_payroll(self):
        
        return self.weekly_salary + self.commission


# Example usage
if __name__ == "__main__":

    salaried_employee = SalaryEmployee(emp_id=1, name="Alice", weekly_salary=1000)
    hourly_employee = HourlyEmployee(emp_id=2, name="Bob", hours_worked=40, hourly_rate=15)
    commission_employee = CommissionEmployee(emp_id=3, name="Charlie", weekly_salary=800, commission=200)

    
    print(f"{salaried_employee.name}'s weekly payroll: ${salaried_employee.calculate_payroll()}")
    print(f"{hourly_employee.name}'s weekly payroll: ${hourly_employee.calculate_payroll()}")
    print(f"{commission_employee.name}'s weekly payroll: ${commission_employee.calculate_payroll()}")