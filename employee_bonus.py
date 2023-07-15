import csv

employee = open('EmployeePay.csv', 'r')
employee_file = csv.reader(employee, delimiter= ',')

next(employee_file)
for record in employee_file:
    print(record)
    
employee.close()