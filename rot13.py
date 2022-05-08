"""rot13
ROT13 é uma cifra simples de substituição de letras que substitui uma letra pela letra 13 letras depois dela no alfabeto. ROT13 é um exemplo da cifra de César.

Crie uma função que receba uma string e retorne a string criptografada com Rot13. Se houver números ou caracteres especiais incluídos na string, eles devem ser retornados como estão. Apenas letras do alfabeto latino/inglês devem ser deslocadas, como na "implementação" original do Rot13.

Observe que usar encodeé considerado trapaça.
"""


def rot13(message):
    my_dict = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w",
               "k": "x", "l": "y", "m": "z", "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g",
               "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"}
    m1 = ""
    for x in message:
        if (x.lower() in my_dict) == False:
            m1 = m1 + x
        elif x.isupper() == True:
            m1 = m1 + my_dict[x.lower()].upper()
        elif x.isupper() == False and x.lower() in my_dict != False:
            m1 = m1 + my_dict[x]

    return m1

print(rot13("casa"))