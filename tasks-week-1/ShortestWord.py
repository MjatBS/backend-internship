def find_short(s):
    words = s.split(' ')
    l = len(words[0])
    for word in words:
        if len(word) < l:
            l = len(word)
    return l # l: shortest word length