# Get a list input from the user in the format of [num1, num2, num3, ...]
user_input = input("Enter a list of numbers separated by commas and enclosed in square brackets, e.g., [1, 2, 3]: ")

try:
    # Attempt to parse the user input as a list of numbers
    user_list = eval(user_input)

    # Ensure the input is a list
    if not isinstance(user_list, list):
        raise ValueError

    # Filter and print positive numbers
    positive_numbers = [num for num in user_list if num > 0]
    print("Positive numbers in the list:", positive_numbers)

except (SyntaxError, ValueError):
    print("Invalid input. Please enter a list in the format [num1, num2, num3, ...]")
