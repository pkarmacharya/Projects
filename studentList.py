import json

studentList = []

def getUserInput():
    userInput = {
        "Name" : {   
            "First Name" : input("Enter first name: "),
            "Last Name" : input("Enter last name: ")
        },
        "Address" : {
            "Street" : input("Enter street address: "),
            "City" : input("Enter city: "),
            "State" : input("Enter state: "),
            "Zip" : input("Enter zip: ")
        }
    }
    return userInput

Student = getUserInput()
studentList.append(Student)


try:
    with open('Student.json', 'r') as outfile:
        output = json.load(outfile)
    output.append(Student)
    with open('Student.json', 'w') as outfile:
        json.dump(output, outfile)
except FileNotFoundError:
    with open('Student.json', 'w') as outfile:
        json.dump(studentList, outfile)
    

