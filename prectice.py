class person: 
  def __init__(self, n, o):
    self.name = n
    self.occ = o
  def info(self):
    print(f"{self.name} is a {self.occ}")

a = person("Arafat", "Engineer")
b = person("Shifa", "Also Engineer")
c = person("Anamul", "Web developer")
d = person("Yasin", "App developer")
a.info()
b.info()
c.info()
d.info()
