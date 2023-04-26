def is_palindrome(input_str):
    # Remove any white space from the input string
    input_str = input_str.replace(' ', '')

    # Convert the input string to lowercase
    input_str = input_str.lower()

    # Create an empty list to store characters
    char_list = []

    # Lopp through each character in the input string
    for char in input_str:
        # Append the character to the list
        char_list.append(char)

    # Create a new string  from the reversed list of characters
    reversed_str = ''.join(reversed(char_list))

    # Compare the original string  with the reversed string
    if input_str == reversed_str:
        return True
    else:
        return False


# An example
input_str = 'A man a plan a canal Panama'
if is_palindrome(input_str):
    print(input_str + ' is a palindrome')
else:
    print(input_str + ' is not a palindrome')
