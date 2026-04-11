HISTORY_FILE="history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("no history function")    
    else:
        for line in reversed(lines):
            print(line.strip()) 
        file.close()
def clear_history():
    file = open(HISTORY_FILE, "w")   
    file.close()
    print("history cleared successfully")   
def save_to_history(expression, result):
    file = open(HISTORY_FILE,'a') 
    file.wrrite(expression + "=" + str(result) + "\n")
    file.close()
def calculate(user_input):
    parts = user_input.split()    
    if len(parts) !=3:
        print("invalid input formot.please enter in the format numbar operation number") 
        return
    num1 = float (parts[0])
    op = parts[1]
    num2 = float(parts[2])
    if op == "+":
        result = num1 +num2
    elif op =="-":
        result = num1 - num2
    elif op =="*":
        result = num1 * num2
    elif op =="/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    if int(result) == result:
        result = int(result)
        print("result:",result)
        save_to_history(user_input .result)
def maim():
    print("---weloce to the calculater with history---")   
    while True:
        user_input = input("Enter an expression (or type \"history\" to view history, \"clear\" to clear history, or \"exit\" to quit):")  
        if user_input=="exit":
         print("good by!")
         break
        elif user_input=="history":
          show_history()
        elif user_input=="clear":
            clear_history()
    else:
            calculate(user_input)   