def wave(word):
    wave = []
    for i in range(0, len(word)):
        if word[i].isalpha():
            wave.append(word[: i] + word[i].upper() + word[i+1:])
    return wave