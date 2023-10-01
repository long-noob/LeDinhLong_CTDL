def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

   return sorted(word1) == sorted(word2)

word1 = "ngu"
word2 = "ung"
result = are_anagrams(word1, word2)

if result:
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')
