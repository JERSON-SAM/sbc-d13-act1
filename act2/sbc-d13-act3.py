# Input word from user
word = input("Enter a word: ")
subwords = []
if word == " ":
    subwords.append(word[:6] + '#' * 3)
    subwords.append(word[-3:])
else:
    subwords.extend([word[:2], '##' + word[2:]] if len(word) > 3 else [word])

print("Subword Tokenization:", subwords)
