#Compount data structures
#Dictionary of dictionaries

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(elements['hydrogen'])
print(elements['helium']['weight'])

#Adding elements to compound DS

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements['helium'])

#Quiz: Flying Circus Records

"""A regular flying circus happens twice or three times a month. For each month, information about the amount of money taken at each
event is saved in a list, so that the amounts appear in the order in which they happened. The months' data is all collected ' \
'in a dictionary called monthly_takings.

For this quiz, write a function total_takings that calculates the sum of takings from every circus in the year. Here's a sample ' \
'input for this function:"""

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(monthly_takings):
    #total is used to sum up the monthly takings
    total = 0
    for month in monthly_takings.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        print(monthly_takings[month])
        total = total + sum(monthly_takings[month])
    return total
print(total_takings(monthly_takings))
