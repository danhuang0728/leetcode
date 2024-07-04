roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = str("LVIII")
sum = 0
for i in range(0,len(s)-1):
    if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
        sum = sum - roman_numerals[s[i]]
    if roman_numerals[s[i]] >= roman_numerals[s[i+1]]:
        sum = sum + roman_numerals[s[i]]
                    
print(sum + roman_numerals[s[-1]])
