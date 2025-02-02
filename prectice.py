class Employee:
    companyName ="Apple"
    degignation = "Software Engineer"
    noOfEmploy = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmploy +=1
        
    def showDetails(self):
        print(f"The Employ name is {self.name} and the raise amount in {self.noOfEmploy} sized {self.companyName} is {self.raise_amount} and job positiopn is {self.degignation}")
    
e1 = Employee("Arafat")
e1.raise_amount = 2.3
e1.companyName ="Apple USA"
e1.showDetails()
e2 = Employee("Shifa")
e2.companyName ="Apple UK"
e2.showDetails()
    


        
        
         
        