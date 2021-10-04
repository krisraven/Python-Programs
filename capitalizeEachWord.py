# Make each word i na string capital without using an inbuilt method

def capitalLetters(string):
    sentence = ""
    words = []
    st = string.split()
    for i in st:
        il = list(i)
        il[0] = il[0].upper()
        words.append(''.join(il))
    return " ".join(words)

print(capitalLetters("hi i love coding in python. do you?"))
