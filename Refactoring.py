# Define the remove_duplicates function
def remove_duplicates(org_list):
    new_list = []
    for i in org_list:
        if i not in new_list:
            new_list.append(i)
          #  print(new_list)
    return new_list

list = [1,3,4,5,3,4,1]
print(remove_duplicates(list))

# Using sets instead of lists to store unique elements




