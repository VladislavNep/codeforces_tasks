romans = {
    "I": 1,
    "V": 5,
    'X': 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def parse_roman(roman):
    result = 0
    for i, v in enumerate(roman):
        if i + 1 < len(roman) and romans[v] < romans[roman[i+1]]:
            result -= romans[v]
        else:
            result += romans[v]

    return result


print(parse_roman(input("Введите арабскую цифру \n")))
