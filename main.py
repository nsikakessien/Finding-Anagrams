# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    a = sorted(word.lower())
    b = sorted(anagram.lower())
    return(a == b)

print(find_anagram("ELbow", 'below'))
print(find_anagram("hello", "check"))