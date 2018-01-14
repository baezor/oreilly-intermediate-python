# find the longest palindrome in all the scrabble words

import scrabble

longest = ""

# Solution1
#for word in scrabble.wordlist:
#    is_palindrome = True
#    for index in range(len(word)):
#        if word[index] != word[-(index + 1)]:
#            is_palindrome = False
#    if is_palindrome and len(word) > len(longest):
#        longest = word

# Solution 2
#for word in scrabble.wordlist:
#    if list(word) == list(reversed(word)) and len(word) > len(longest):
#        longest = word

#Solution 3
for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word

print(longest)