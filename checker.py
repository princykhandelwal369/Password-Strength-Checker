#List of symbols
symbols="!@#$%^&*()_-+={ }[]:;'<>,.?/~`"

while True:
    password=input("Enter password: ")

    #Conditions
    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False
    #We originally define them as False. If proven true, we change it to True



    #Checking each condition
    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_number=True
        elif char in symbols:
            has_symbol=True

    missing=False
    score=0
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1
    if len(password) >= 8:
        score += 1

    #Printing the results
    if len(password)<8:
        print("Password is Short!")
        missing=True
    if not has_upper:
        print("Missing Uppercase Letter")
        missing=True
    if not has_lower:
        print("Missing Lowercase Letter")
        missing=True
    if not has_number:
        print("Missing Number")
        missing=True
    if not has_symbol:
        print("Missing special character")
        missing=True
    if score <= 2:
        print("Weak Password")
    elif score == 3 or score==4:
        print("Medium Password")
    else:
        print("Strong Password")
        break

    
