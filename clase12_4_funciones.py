def greet(name):
    print(f"Hello, {name}!")
    
greet("Enzo")


#calculator function
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Calculator")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        option = input("Select an option: ")
        
        if option == "5":
            print("Goodbye")
            break
            
        if option in ["1","2","3","4"]:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            if option == "1":
                print(add(a,b))
            elif option == "2":
                print(substract(a,b))
            elif option == "3":
                print(multiply(a,b))
            elif option == "4":
                print(divide(a,b))
        
        else:
            print("Invalid option")
            
calculator()
    