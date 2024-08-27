my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# inserting 15 to the second position
my_list.insert(1, 15)
print(my_list)

list_two = [50, 60, 70]

my_list.extend(list_two)
my_list.sort()
print(my_list)

print(my_list[3])