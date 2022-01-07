from art import logo

print(logo)

#Add
def add(a, b):
    return a + b

#Substract
def substract(a, b):
    return a - b

#divide
def divide(a, b):
    return a / b

#multiple
def multiple(a, b):
    return a * b


operations = {
    "+" : add,
    "-" : substract,
    "*" : multiple,
    "/" : divide
}
check = ""
continue_calculation = True


while continue_calculation:
    if check == 'y':
        num1 = answer
    else:
        num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number?: "))

    calculation_function = operations[operation_symbol]

    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. : ")

    if check == 'n':
        continue_calculation = False
    

