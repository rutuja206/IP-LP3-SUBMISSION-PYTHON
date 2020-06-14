sent = "rutu hi hi hi "

# Seperate out each word
words = sent.split(" ")

# Convert all words to lowercase
words = map(lambda x:x.lower(), words)

# Sort the words in order
words.sort()
unique = []
total_words = len(words)
i = 0

while i < (total_words - 1):
   while i < total_words and words[i] == words[i + 1]:
      i += 1
   unique.append(words[i])
   i += 1

print(unique)