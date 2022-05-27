# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    a = sorted(word.lower().replace(" ", ""))
    b = sorted(anagram.lower().replace(" ", ""))
    return(a == b)

print(find_anagram("ELbow", 'below'))
print(find_anagram("hello", "check"))
print(find_anagram("Dormitory", "Dirty Room"))