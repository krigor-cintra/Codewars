"""Welcome.
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc."""

def alphabet_position(text):
    my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
               "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
               "x": 24, "y": 25, "z": 26}
    c = ""
    b = []
    texte = text.lower()
    b.extend(texte)
    for x in range(len(b)):
        cont = 1
        for y in (my_dict):
            if ((b[x] in my_dict) == True):
                if (b[x] == y):
                    c = c + " " + (str(my_dict[y]))
            elif ((b[x] in my_dict) == False) and cont == 26 and (b[x] != " "):
                c = c + b[x]
        cont = cont + 1

    return (c.lstrip())