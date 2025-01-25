def cube(x):
    return x*x*x

l  = [2,4,6,7]

newl = list(map(cube, l))
print(newl)