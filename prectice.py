class Employ:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def ShowDetails(self):
        print(f"The name of employ {self.name} and ID is {self.ID} ")
        
class progmeer(Employ):
    def __init__(self, language):
        self.language = language
        
    def ShowLanguage(self):
        print(f"The employ work om {self.language} language")
        
    
e = Employ("Sharif Arafat", 25)
e.ShowDetails()
b = progmeer("python")
b.ShowLanguage()

   