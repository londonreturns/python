def frequency_of_words(words):
    if words == []:
        return {}
    current_word = words[0]
    freq = words.count(current_word)
    rest = []
    for word in words:
        if word != current_word:
            rest.append(word)
    word_freq = {current_word: freq}
    rest_freq = frequency_of_words(rest)
    
    for key, value in word_freq.items():
        rest_freq[key] = value
        
    return rest_freq
    


try:
    filename = 'temp.txt'
    with open(filename, 'r') as file1:
        line = file1.readline()
        words = line.split(' ')
    print(words)
    print(frequency_of_words(words))
except FileNotFoundError:
    print('file not found')