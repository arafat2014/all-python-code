class person:
  name = "Arafat"
  occupation = "Software Engineer"
  def info(self):
    print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
a.name = "Anamul"
a.occupation = "Web developer"
a.name = "Anamul"
a.occupation = "Web developer"

a.info()
b.info()