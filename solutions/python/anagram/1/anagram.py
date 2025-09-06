def find_anagrams(word, candidates):
    anagrams = []
    org_word = word.upper()
    word = list(word.upper())
    word.sort()
    for check_word in candidates:
        if len(check_word) != len(word) or org_word == check_word.upper():
            continue
        sorted_word = list(check_word.upper())
        sorted_word.sort()
        if sorted_word == word:
            anagrams.append(check_word)
    return anagrams