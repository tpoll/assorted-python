# This program is a word frequency analyzer you can interact with it a
#and find interesting things about words!

text = open("book.txt", "r")
full_text = text.read()
text_wordlist = full_text.split()
word_dictionary = {}

def is_in(word, word_dictionary):
  for key in word_dictionary:
    if word in word_dictionary:
      return False
  return True

for word in text_wordlist:
  if is_in(word, word_dictionary):
    word_dictionary[word] = 1
  else:
    word_dictionary[word] += 1
    

max_word = max(word_dictionary, key=word_dictionary.get)
print max_word  
print word_dictionary[max_word]
