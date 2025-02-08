from collections import Counter
def muliple_values(lst):
    s_names=[]
    o_names=[]
    for name in lst:
        if name.startswith("S"):
           s_names.append(name)
           count_Snames = len(s_names)
        else:
            o_names.append(name)
    return count_Snames, o_names

names = ["Joseph", "Sasha", "Nathan", "Sera", "Tom", "Sienna"]
count_Snames, o_names = muliple_values(names)
print(count_Snames)
print(o_names)

# Using Collections
count_names_list = Counter(names)
print(f"Total number of names in original list is {count_names_list}")

# Using yield
def func():
    for i in range(4):
        yield i
    

gen_func = func()
print(next(gen_func))
print(next(gen_func))

# Using args
def add_num(*args):
    return sum(args)

print(add_num(10,20,30,40,50))
print(add_num(10,40))