lst = [0, 1]

for i in range(40):
    lst.append(lst[-1] + lst[-2])
    
print lst
