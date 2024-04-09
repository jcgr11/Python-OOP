# McDonalds Employee Management System

from employees import EmployeeDatabase
from productivity import ProductivitySystem
from hr import PayrollSystem

# Setup systems and databases
productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees

# Simulate a work week for all employees with shift details, morning/day/night shift.
for employee in employees:
    employee.work(40)

# Calculate payroll for all employees for the week.
payroll_system.calculate_payroll(employees)
