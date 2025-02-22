random_set = {"Educative", 1488, 3.142, (True, False), 1488}
print(random_set)
print(len(random_set))

#set() constructor
empty_set = set()
print(empty_set)

"""
Set: Created using curly brackets {} and contains unique, unordered elements.

List: Created using square brackets [] and contains ordered mutable elements.

Tuple: Created using parentheses () and contains ordered immutable elements.

Dictionary: Created using curly brackets {} and contains key-value pairs.

"""
#Examples

test_set = {"Educative", 1408, 3.142, (True, False)}
test_lst = ["Educative", 1408, 3.142, (True, False)]
test_rev_lst = test_lst.append(2)
test_dict = {1: "Educative", 2: 1488, 3: 3.142, 4: (True, False)}

test_tup = ("Educative", 1408, 3.142, (True, False))
test_rev_tup = test_tup.index(1408)

print(test_set)

print(test_lst)
print(test_dict)
print(test_tup)
print(test_rev_tup)

#Adding Elements
empty_set.add(1)
print(empty_set)

#Update Elements
empty_set.update([2,2,3,4,4,6])
print(empty_set)

#Deleting Elements
random_set.discard(1488)
print(random_set)

# Iterating a set

odd_lst = [1,3,5,7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if(num%2 == 0):
        odd_lst.append(num)

print(odd_lst)

# Set Comprehension

square_set = {x**2 for x in range(1,10)}
print(sorted(square_set))

even_set = {x for x in range (2,10,2)}

print(sorted(even_set))

# Tuple of Star Wars characters and a number
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)

# Set of Star Wars characters and a number
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)

# Dictionary mapping numbers to Star Wars characters
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# Converting the tuple to a list
star_wars_tup = list(star_wars_tup)
print(star_wars_tup)

# Converting the set to a list
star_wars_list_from_set = list(star_wars_set)
print(star_wars_list_from_set)

# Converting the keys of the dictionary to a list
star_wars_list_from_keys = list(star_wars_dict.keys())
print(star_wars_list_from_keys)

# Converting the values of the dictionary to a list
star_wars_list_from_values = list(star_wars_dict.values())
print(star_wars_list_from_values)

# Converting the items (key-value pairs) of the dictionary to a list
star_wars_list_from_items = list(star_wars_dict.items())
print(star_wars_list_from_items)

# Converting the list to a tuple
star_wars_list = ["Anakin", "Darth Vader", 1000]
star_wars_tuple_from_list = tuple(star_wars_list)

# Pop usecase
traffic_light = {"Green": "Go", "Yellow": "Wait", "Red": "Stop"}
entry = traffic_light.popitem()
print(entry)

#List Comprehension
string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = []
for s in string_list:
    if len(s) < 5:
        result.append(len(s))

result = [s for s in string_list if len(s) < 5]
print(result)

my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
len_my_list = len(my_list)
my_tuple_from_my_list = (my_list[0],my_list[4],len_my_list)
print(my_tuple_from_my_list)
#Dynamic
my_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))
print(my_tuple)

test_list = [40, 35, 82, 14, 22, 66, 53]
k=2
# sorted_list = sorted(test_list)
# kth_max = sorted_list[-k]
# print(kth_max)

# test_list.sort(reverse=True)
# print(test_list)
# kth_max_desc = test_list[k-1]
# print(kth_max_desc)

test_list.sort()
kth_max = test_list[-k]
print(kth_max)

def count_low_high(num_list):
    if (len(num_list)==0):
        return None
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 ==0, num_list))
    return[len(low_list), len(high_list)]

num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(num_list))
