message = input().upper()
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inverted = letters[::-1]


def convertor(char):
    if char in letters:
        n = letters.index(char)
        return inverted[n]
    else:
        return " "

result = list(map(convertor, message))
print("".join(result).lower())
