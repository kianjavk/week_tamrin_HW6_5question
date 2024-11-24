import argparse


# Define the function for each operation
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


# Main function
def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Command-line calculator")

    # Define arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide"],
                        help="Operation to perform: add, subtract, multiply, divide")
    parser.add_argument("--round", type=int, default=None, help="Number of decimal places to round the result")

    # Parse the arguments
    args = parser.parse_args()

    # Perform the operation
    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operation == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operation == "divide":
        result = divide(args.num1, args.num2)

    # Handle rounding if specified
    if isinstance(result, (float, int)) and args.round is not None:
        result = round(result, args.round)

    # Print the result
    print("Result:", result)


if __name__ == "__main__":
    main()



# # Addition
# python calculator.py 10 5 add
#
# # Subtraction
# python calculator.py 10 5 subtract
#
# # Multiplication
# python calculator.py 10 5 multiply
#
# # Division
# python calculator.py 10 5 divide
#
# # Division by zero
# python calculator.py 10 0 divide
#
# # Round result to 2 decimal places
# python calculator.py 10 3 divide --round 2