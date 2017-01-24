def romanToInt(s):
    numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
    sum = 0
    s = s[::-1]
    last = numerals[s[0]]
    for x in s:
        if numerals[x] < last:
            sum -= numerals[x]
        else:
            numerals[x] >= last
            sum += numerals[x]
        last = numerals[x]
    return sum


def romanToInt1(s):
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    s = s[::-1]
    last = numerals[s[0]]
    for x in s:
        if numerals[x] < last:
            sum -= numerals[x]
        else:
            sum += numerals[x]
        last = numerals[x]
    return sum

numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
print romanToInt('DCXXI')