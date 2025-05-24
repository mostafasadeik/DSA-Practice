# Strings (Caesar Cipher Encryptor)
# Problem:
# Given a string and a number, return the string after applying a Caesar cipher to it.
# A Caesar cipher works by shifting each letter in the string by the given number.
# For example, if the string is "abc" and the number is 2, the result would be "cde".

# Approach:

def caesarCipherEncryptor(string ,key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return ''.join(newLetters)


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key 
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# Test cases
print(caesarCipherEncryptor("xyz", 2))