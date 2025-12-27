# numerator = 10
# denominator = 3

# if numerator % denominator == 0:
#     print(f"remainder is zero")

# if denominator != 0:
#     if numerator % denominator == 0:
#         print(f"remainder is zero")
# print("Denominator is zero, and cannot perform modulus operation")

# Replace or with and operator to see short-circuit evaluation in action to identify execution flow
# if denominator != 0 or numerator % denominator == 0:
#     print(f"either the denominator or remainder is zero")

# if denominator != 0 and numerator % denominator == 0:
#     print(f"remainder is zero")
# elif denominator != 0:
#     print("Denominator is not zero, but remainder is also not zero")
# else:
#     print("Denominator is zero, and cannot perform modulus operation")

# Check if a number is positive and even
# number = 10

# # Write your code here
# if number > 0 and number % 2 == 0:
#     print("number is even.")
# else:
#     print("number is either less than 0 or not an even number.")

# Loan approval based on age and income

customer_age = 19
annual_income = 60000
monthly_income = annual_income / 12
has_default = True
if (customer_age >= 18 and customer_age <= 70) and  (monthly_income >= 3000 or annual_income >= 50000) and (not has_default):
    print("Loan Approved")
else:
    print("Loan Denied")