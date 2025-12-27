# num = 5

try:
    user_input = input("Enter a number: ")
    entered_value = int(user_input)
    if (entered_value > 5):
        print(f"Entered number {entered_value} is greater than 5.")
    elif (entered_value < 5):
        print(f"Entered number {entered_value} is less than 5.")
    else:
        print(f"Entered number {entered_value} is equal to 5.")
except ValueError:
    print(f"Enter a valid numeric value. Entered value is: {user_input}")


