myDict1 = {
    "Sam" : "BMW",
    "Kevin" : "Toyota",
    "Matt" : "Audi",
    "Jen" : "Toyota",
    "Lulu" : "Toyota",
    "Brian" : "BMW",
    "Saurab" : "Audi",
    "Kobe" : "BMW",
    "Chris" : "BMW",
    "Bipul" : "Honda"
}

#myDict2 = {
#    "BMW": 0}

myDict2 = {}

for x in myDict1:
    if myDict1[x] in myDict2:
        myDict2[myDict1[x]] = myDict2[myDict1[x]] + 1
    elif myDict1[x] not in myDict2:
        myDict2[myDict1[x]] = 1
    
print(myDict2)

"""
for x in myDict2:
    print(x)
    
for x in myDict2.values():
    print(x)
    
for x in myDict2:
    print(myDict2[x])
    
for x, y in myDict2.items():
    print(x,y)
"""
