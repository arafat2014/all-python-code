class Employee:
    companyName ="Apple"
    degignation = "Software Engineer"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        
    def showDetails(self):
        print(f"The Employ name is {self.name} and raise amount in {self.companyName} is {self.raise_amount} and job positiopn is {self.degignation}")
    
e1 = Employee("Arafat")
e1.raise_amount = 2.3
e1.showDetails()
e2 = Employee("Shifa")
e2.showDetails()
    


        
        
         
        