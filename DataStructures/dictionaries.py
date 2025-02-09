# First Example
country_capitals_dict = {
    "USA":"WashingtonDC",
    "India" : "NewDelhi",
    "Thailand":"Bangkok"
}
print(country_capitals_dict)

#Add another country to the dict
country_capitals_dict["Malaysia"] = "Kualalampur"
print(country_capitals_dict)

#change value in an existing dict
country_capitals_dict["USA"] = "Dallas"
print(country_capitals_dict)

#Removing entries using del
# del country_capitals_dict["USA"]
# print(country_capitals_dict)

# Using pop() and popitem()
# usa = country_capitals_dict.pop("USA")
# print(usa)
# print(country_capitals_dict)

# last_added = country_capitals_dict.popitem()
# print(last_added)
# print(country_capitals_dict)

#Dictionary length
print(len(country_capitals_dict))

#checking <key> existence - retruns True or False
print("India" in country_capitals_dict)
print("Canada" in country_capitals_dict)

second_country_capital_dict = {"Russia": "Moscow",
                               "Kuwait": "KuwaitCity"}
country_capitals_dict.update(second_country_capital_dict)
print(country_capitals_dict)

# Dictionary Comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n*2:house + "!" for(n, house) in houses.items()}
print(houses)
print(new_houses)

# Filtering with Dict Comprehension
squares = {x:x**2 for x in range(1,6) if x%2==0}
print(squares)

#Nested Dictionary
nested_dict = {x:{y:y**2 for y in range(1,4)} for x in range(1,4)}
print(nested_dict)

# Invert keys and values of a dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value:key for key, value in original_dict.items()}
print(inverted_dict)
# Output: {1: 'a', 2: 'b', 3: 'c'}

def update_phone_book(phone_book, new_entries):
    phone_book.update(new_entries)


phone_book = {"Spiderman": 123456, "Hulk": 654321}
new_entries = {"Thor": 789123, "Hulk": 111111}
update_phone_book(phone_book, new_entries)
print(phone_book)

#Create new squares dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16}
new_squares = {x*2:y+1 for x,y in squares.items()} #Your code here
print(new_squares) 