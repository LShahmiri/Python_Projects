import random
import string
# Generate a password
password=''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))
# print the result
print('Generated password: ', password)