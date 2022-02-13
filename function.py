def cube(base, power):
    c = pow(base, power)
    return c
base_number=int(input("Suggest a base number: "))
index_number=int(input("Suggest a index number: "))
result = cube(base_number,index_number)
print(result)
