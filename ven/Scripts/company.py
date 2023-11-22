from employee import employee,salariedemployee,hourlyemployee,comissionemployee

class Company:
    def __init__(self):
        self.employees=[]
    
    def addemployees(self,new_employee):
        self.employees.append(new_employee)

    def printemployees(self):
        for emp in self.employees:
            print(emp.fname)

    def payemployess(self):
        for emp in self.employees:
            print(emp.fname,f'--> Amount : ${emp.CalPayCheck():,.2f}')

def main():
    companyobj=Company()
    employeeobj1= salariedemployee('Sarah','Hess',500000)
    companyobj.addemployees(employeeobj1)
    employeeobj2= hourlyemployee('Gokul','c',4,3)
    companyobj.addemployees(employeeobj2)
    employeeobj3= comissionemployee('Chirag','R',900000,50000)
    companyobj.addemployees(employeeobj3)
    companyobj.printemployees()
    companyobj.payemployess()

main()