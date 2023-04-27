# Craet two list to be combined
names = ['lida', 'vida', 'leila']
age = [35, 31, 40]
height = [175, 164, 170]

# Use zip to combine the two lists into a single iterable
person_data = zip(names, age, height)
person_dict = {}

# itrate over the resulting iterable and add each person to the dictionary
for person in person_data:
    # Unpack the person data into sequence variables
    name, age, height = person

    # Add the person to the dictionary
    person_dict[name] = {'age=': age, 'height=': height}

# Print out the resulting dictionary
print(person_dict)
