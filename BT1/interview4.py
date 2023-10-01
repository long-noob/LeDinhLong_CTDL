def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase for case insensitivity
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the sorted characters of the words are the same
    return sorted(word1) == sorted(word2)

word1 = "ngu"
word2 = "ung"
result = are_anagrams(word1, word2)

if result:
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')
