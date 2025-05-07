nums = [110,35,41,7000,90]
nums.sort()
print(nums)

words = ["this is a very long string", "omg", "z"]
words.sort(key=len , reverse=True)
print(words)


my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]
def sort_tuple (tuple_value) :
    return tuple_value[1]
my_list.sort(key=sort_tuple)
print(my_list)

list = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(list)
print(list)
print(sorted_list)