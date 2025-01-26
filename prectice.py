def apply(fx, value):
  return 6 + fx(value)
dauble = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
print(dauble(5))
print(cube(5))
print(avg(3,5))
print(apply(cube, 2))