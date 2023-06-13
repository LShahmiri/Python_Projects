# Dctionary Application
# Dictionary Data
dictionary = {'rich': 'having a lot of money or valuable possessions', 'affluent': 'having a lot of money or owning a lot of things: ',
              'advantaged': 'having a better standard of living, more opportunities to succeed, etc. than other people: '}


def search_word(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return 'word is not in dictionary'


def add_word(word, definition):
    dictionary[word] = definition
    return 'word added to the dictionary'


def remove_word(word):
    if word in dictionary:
        del dictionary[word]
        return 'word is deleted'
    else:
        return 'word not found'


# Example usage
print(search_word("rich"))
print(search_word("bazillionaire"))

print(add_word("bazillionaire", "someone who is extremely rich "))
print(search_word("cat"))

print(remove_word("affluent"))
print(search_word("affluent"))
