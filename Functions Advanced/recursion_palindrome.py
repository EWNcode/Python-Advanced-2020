"""
Write a recursive function called palindrome which will receive a word and an index (always 0). Implement the function,
so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not
a palindrome using recursion.

"""


def palindrome(word, index):
    stop = len(word) // 2
    if index == stop:
        return f'{word} is a palindrome'
    if word[index] == word[len(word)-1-index]:
        return palindrome(word, index+1)
    else:
        return f'{word} is not a palindrome'

print(palindrome("abcba", 0))
print(palindrome("peter", 0))