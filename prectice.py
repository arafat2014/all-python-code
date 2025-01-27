def asset(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this fincation")
  return mfx
@asset
def hello():
    print("Hello world")
@asset
def add(a, b):
  print(a+b)
  
hello()
add(1,3)