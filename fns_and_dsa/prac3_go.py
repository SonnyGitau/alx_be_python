# divide_numbers.py

def main():
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero divisor.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

    else:
        print(f"The result of dividing {num1} by {num2} is {result}")

if __name__ == "__main__":
    main()
