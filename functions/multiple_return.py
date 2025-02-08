def check_age(age):
    if age < 16 and age < 18:
        return f"{age} is too young to drive"
    elif age >= 18 and age < 78:
        return f"Age {age} is eligible to drive"
    else:
        return f"Age greater than or equal to {age} needs a yearly exam before driving"

print(check_age(79))