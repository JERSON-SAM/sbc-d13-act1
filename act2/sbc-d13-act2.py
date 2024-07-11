user = input("Enter Sentence:")

def characters(user):
    tokens = ['"' + char + '"' for char in user]
    return '[' + ', '.join(tokens) + ']'

# Example usage:
result = characters(user)
print(result)
