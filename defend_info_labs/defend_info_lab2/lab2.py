equivalent = {
    'А': 1,
    'Б': 2,
    'В': 3,
    'Г': 4,
    'Д': 5,
    'Е': 6,
    'Ё': 7,
    'Ж': 8,
    'З': 9,
    'И': 10,
    'Й': 11,
    'К': 12,
    'Л': 13,
    'М': 14,
    'Н': 15,
    'О': 16,
    'П': 17,
    'Р': 18,
    'С': 19,
    'Т': 20,
    'У': 21,
    'Ф': 22,
    'Х': 23,
    'Ц': 24,
    'Ч': 25,
    'Ш': 26,
    'Щ': 27,
    'Ъ': 28,
    'Ы': 29,
    'Ь': 30,
    'Э': 31,
    'Ю': 32,
    'Я': 33,
    ' ': 34,
    '0': 35,
    '1': 36,
    '2': 37,
    '3': 38,
    '4': 39,
    '5': 40,
    '6': 41,
    '7': 42,
    '8': 43,
    '9': 44,
}

string = "ХЛОПНУ БУРГЕР ЗА ЗДОРОВЬЕ СОБЯНИНА"

p = 5
q = 11
euler = (p-1)*(q-1)
n = p*q
e = 23
open_key = (e, n)
d = 0.1
k = 1
while d != int(d):
    d = (k*euler + 1)/e
    k += 1

closed_key = (d,n)

def cipher(string, equivalent, open_key):
    symbols_codes = []
    cipher_symbols_codes = []
    for letter in string:
        print(equivalent[letter], letter)
        symbols_codes.append(equivalent[letter])

    for number in symbols_codes:
        cypher = (number**open_key[0])%open_key[1]
        cipher_symbols_codes.append(cypher)
    return cipher_symbols_codes

def uncipher(cipher_symbols_codes, closed_key, equivalent):
    new_symbols_codes = []
    new_string = ''
    for number in cipher_symbols_codes:
        cypher = (number**closed_key[0])%closed_key[1]
        new_symbols_codes.append(cypher)

    for code in new_symbols_codes:
        for key, value in equivalent.items():
            if code == value:
                new_string += key
                print(int(code), key)

    return new_string

cipher_symbols_codes = cipher(string, equivalent, open_key)
new_string = uncipher(cipher_symbols_codes, closed_key, equivalent)
print(new_string)
