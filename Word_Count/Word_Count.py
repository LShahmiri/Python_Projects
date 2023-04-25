sentence = input('Enter your sentence: ') 
# split the sentence to the list of words
words=sentence.split()
# Create a empty dictionary to store words count
word_count = {}
# Loop over each word and update the word counts
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Print word count dictionary
print (word_count)
