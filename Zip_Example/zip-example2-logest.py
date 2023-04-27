import itertools
# Creat three list of different length to be combilned
names = ['lida', 'vida', 'leila']
ages = ['35', '31']
heights = [175, 164, 170]

# Use zip_longest to combine the three lists into a single iterable
person_data = itertools.zip_longest(names, ages, heights, fillvalue=None)

# Create a dictionary to hold the personla data
person_dict = {}


# Iterate over the resulting iterable and add each person to the dictionary
for person in person_data:
    # Unpack the person data into seprate variables
    name, age, heghit = person

    # Add the person to the dictionary
    person_dict[name] = {'age': age, 'height': heghit}
# print out the resulting dictionary
print(person_dict)
