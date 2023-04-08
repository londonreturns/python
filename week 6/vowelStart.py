# returns set with only string that start with vowel

def onlyStartWithVowel(allSet):
    filteredSet = set()
    for word in allSet:
        if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
            filteredSet.add(word)
    return filteredSet


newSet = {"apple", "banana", "food", "onion"}

onlyVowel = onlyStartWithVowel(newSet)

print(onlyVowel)