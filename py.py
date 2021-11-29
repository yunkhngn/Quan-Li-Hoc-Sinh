def checkIfStringIncludeANumber(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return True
    return False
string = input("Enter a string: ")
print(checkIfStringIncludeANumber(string))
