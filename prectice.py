l = [2,1,3,5,7,9,65]
def filter_funcation(a):
    return a>4
newlin = list(filter(filter_funcation, l))
print(newlin)