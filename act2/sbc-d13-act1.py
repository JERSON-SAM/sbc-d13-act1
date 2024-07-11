sentence = input("Enter Your Sentence:")

# Sentence tokenization
sentence_delimiters = '.!?'
sentences = []
current_sentence = []

for c in sentence:
    current_sentence.append(c)
    if c in sentence_delimiters:
        sentences.append(''.join(current_sentence).strip())
        current_sentence = []

# Append the last sentence if there's any remaining
if current_sentence:
    sentences.append(''.join(current_sentence).strip())

# Format each sentence with double quotes
sentences = [f'"{s}"' for s in sentences]

# Join the formatted sentences with commas and wrap in square brackets
result = f"[{','.join(sentences)}]"

print("Tokenized Sentences:")
print(result)
