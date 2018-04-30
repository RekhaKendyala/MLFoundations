"""Tuples are used to store related pieces of information.
Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indexes
(for example AngkorWat[0] and AngkorWat[1]). Unlike lists, tuples are immutable. You can't add and remove items from tuples, or ' \
sort them in place.
Why Tuples?
Why do we have tuples if they're like lists with less features? Tuples useful when you have two or more values that are so closely ' \
related that they will always be used together, like latitude and longitude coordinates.
Tuples can be used to assign multiple variables in a compact way:"""

dimensions = 52, 40, 100
length, width, height = dimensions #parentheses not required
length, width, height = 52, 40, 100 # Tuple unpacking - don't need to use dimensions - directly assign
print("The dimensions are {}x{}x{}".format(length, width, height))

world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}

#Returning Tuples
#A common use for tuples is to return multiple values from a function:

def first_and_last(sequence): #returns the first and last elements of a sequence"""
    return sequence[0], sequence[-1]

#The first_and_last function can be used like this:
print(first_and_last(["Spam", "egg", "sausage", "Spam"]))
#A function that returns a tuple can also be used to assign multiple variables:
start, end = first_and_last(["Spam", "egg", "sausage", "Spam"])
print(start)
print(end)

"""Write an hours2days function that takes one argument, an integer, that is a time period in hours. The function should return a tuple
of how long that period is in days and hours, with hours being the remainder that can't be expressed in days. For example, 39 hours
is 1 day and 15 hours, so the function should return (1,15)."""
def hours2days(time):
    #conversion = []
    days, hours = int(time/24), time%24
    return days, hours
print(hours2days(10000))

#default arguments

def print_list(l, numbered = True, bullet_character = '-'):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))
print_list(["cats", "in", "space"], False)
print_list(["cats", "in", "space"], True, '*')
print_list(["cats", "in", "space"])

def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list
#We can call the function like this:

print(todo_list("check the mail"))
print(todo_list("try new"))



