import math

from traitlets import This

# trafficlight = "not working"

# if trafficlight == "Green":
#     print("Go!")
# elif trafficlight == "Yellow":
#     print("Caution!")
# elif trafficlight == "Flashing Red":
#     print("Stop!")
# elif trafficlight == "Flashing Yellow":
#     print("Proceed with Caution!")
# elif trafficlight == "flashing Green":
#     print("Go Quickly!")
# elif trafficlight == "flashing Yellow":
#     print("Slow down and proceed with Caution!")
# elif trafficlight == "Red":
#     print("Stop!")
# # Lights not working
# else:
#     print("Stop!")

# num = 7
# Practice based on common Python patterns
# if num == 0:
#     print("Zero")
# elif num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:
#     print("Three")
# elif num == 4:
#     print("Four")
# elif num == 5:
#     print("Five")
# elif num == 6:
#     print("Six")
# elif num == 7:
#     print("Seven")
# elif num == 8:
#     print("Eight")
# elif num == 9:
#     print("Nine")
# else:
#     print("Number out of range  0-9.")

# match num:
#     case 0:
#         print("Zero")
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case 6:
#         print("Six")
#     case 7:
#         print("Seven")
#     case 8:
#         print("Eight")
#     case 9:
#         print("Nine")
#     case _:
#         print("Number out of range 0-9.")

# Air Quality Index (AQI) levels
AQI = 75

if AQI > 0 and AQI <= 50:
  print("Green/Good")
elif AQI > 50 and AQI <= 100:
  print("Yellow/Moderate")
# elif AQI > 100 and AQI <= 150:
#   print("Orange/Unhealthy for sensitive groups.")
# elif AQI > 150 and AQI <= 200:
#   print("Red/Unhealthy")
# elif AQI > 200 and AQI <= 300:
#   print("Purple/Very Unhealthy")
# elif AQI > 300:
#   print("Maroon/Hazardous")
# else:
#   print("Incorrect Value")

# Comparing Floating Point Numbers

# a = 0.1 + 0.2
# b = 0.52


# Direct comparison (may fail due to precision issues)
# if a == b:
#     print("a and b are equal (direct comparison)")
# else:
#     print("a and b are not equal (direct comparison)")

# Using math.isclose for comparison

# print(math.isclose(a, b))
# print(math.isclose(a, b , rel_tol=1e-9))
# print(math.isclose(a, b , abs_tol=1e-12))
# if math.isclose(a, b):
#     print("a and b are equal (using math.isclose)")
# else:
#     print("a and b are not equal (using math.isclose)")

"""
challenge
This is a simple problem related to the conditional statements. The price variable has already been created. You must use it in your code and assign it a new value based on the discount. If you feel stuck, you can always refer to the solution review in the next lesson.
"""

price = 50

# Write your code here
if price >= 300:
    discount = 0.30
elif price >= 200:
   discount = 0.20
elif price >=100:
    discount = 0.1
else:
    discount = 0.05

price = price-(price*discount)
print(f"price = {price}")