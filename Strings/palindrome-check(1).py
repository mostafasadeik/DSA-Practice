# Strings (Palindrome Check)
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# For example
# "racecar", "level"

# Approach
# 1. Make two pointers, one at the start and one at the end of the string.
# 2. Compare the characters at the two pointers.
# 3. If they are the same, move the pointers towards the center.
# 4. If they are not the same, return False.
# 5. If the pointers cross each other, return True.


def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


# Test cases
print(isPalindrome("racecar"))  # True
print(isPalindrome("level"))    # True
print(isPalindrome("hello"))    # False