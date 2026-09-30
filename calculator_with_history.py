HISTORY_FILE = "history.txt"


def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No history found.")
        else:
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No history found.")


def clear_history():
    with open(HISTORY_FILE, "w") as file:
        pass

    print("History cleared successfully.")


def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(expression + " = " + str(result) + "\n")


def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input format.")
        print("Please enter in the format: number operation number")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2

    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    if result.is_integer():
        result = int(result)

    print("Result:", result)

    save_to_history(user_input, result)


def main():
    print("--- Welcome to the Calculator with History ---")

    while True:
        user_input = input(
            'Enter an expression (or type "history", "clear", or "exit"): '
        )

        if user_input == "exit":
            print("Goodbye!")
            break

        elif user_input == "history":
            show_history()

        elif user_input == "clear":
            clear_history()

        else:
            calculate(user_input)


if __name__ == "__main__":
    main()
