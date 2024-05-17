print("Welcome to Password Complexity Checker!!!\nOptions:\n1. Check\t2. Exit\n")

def check(pas):
    sug = "Suggestions:"
    faults = 0
    
    if len(pas) < 8:
        faults += 1
        sug += f"\n{faults}. Password must contain at least 8 characters."
    
    if not any(c.islower() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 lowercase alphabet."
    
    if not any(c.isupper() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 uppercase alphabet."
    
    if not any(c.isdigit() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 numeric digit."
    
    if not any(not c.isalnum() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 special character."
    
    print(f"\nPassword Strength: {5 - faults} / 5")
    if faults:
        print(sug)
    print('\n')

while True:
    try:
        opt = int(input("Enter option: "))
        if opt == 1:
            pas = input("Enter password: ")
            check(pas)
        elif opt == 2:
            print("Thank you!!")
            break
        else:
            print("Invalid Option!")
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
