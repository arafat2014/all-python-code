class person:
  name = "Arafat"
  occupation = "Software Engineer"
  age = 25
  city = "Dhaka"
  def info(self):
    print(f"{self.name} is a {self.occupation} his age is {self.age} he lives is {self.city}")

a = person()
b = person()
a.name = "Anamul"
a.occupation = "Web developer"
a.age = 26
a.city = "Tangail"

b.name = "Yasin"
b.occupation = "App developer"
b.age = 24
b.city = "Chadpur"

a.info()
b.info()