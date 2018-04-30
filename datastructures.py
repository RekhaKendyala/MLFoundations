 # Define the remove_duplicates function
#original_list = []
def remove_duplicates(org_list):
    new_list = []
    for item in org_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

dup_list = ['a', 'b', 'c', 'a', 'b', 'd', 'd']
print(remove_duplicates(dup_list))

#Sets - Collection of unique elements
# To print all perfect squares less than 2000 added to a set
squares = set()
# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers
def squares_set(limit):
    square = 1
#    squares = set()
    while square**2 < limit:
        squares.add(square**2)
        square+=1
    return squares

#print(squares_set(2000))

#Dictionaries - Key,value pair data structure

test_dict = {'a':1, 'b':2, 'c':3}
print(test_dict['a'])
print(test_dict['d']) # this will throw a key error as 'd' is not an element
print(test_dict.get('d', 'No such element!')) #.get() returns the value  like [], however, get() will return None if the eklement does not exist in the dict.
#We can change the return text - instead of None get() will now return the above message


