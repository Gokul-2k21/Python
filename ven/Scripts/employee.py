class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

class salariedemployee(employee) :
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.Salary=salary
    
    def CalPayCheck(self):
        return self.Salary/12

class hourlyemployee(employee) :
    def __init__(self,fname,lname,weeklyhours,hourlyrate):
        super().__init__(fname,lname)
        self.weeklyhours=weeklyhours
        self.hourlyrate=hourlyrate
    
    def CalPayCheck(self):
        return self.weeklyhours * self.hourlyrate

class comissionemployee(salariedemployee):
    def __init__(self,fname,lname,salary,commision):
        super().__init__(fname,lname,salary)
        self.commision=commision

    def CalPayCheck(self):
        regularsal = super().CalPayCheck()
        return regularsal+self.commision