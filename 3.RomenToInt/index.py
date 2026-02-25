symbol_dict = {
    "I": 1, 
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

toInt = input("Enter Roman Numeric: ")

result = 0
i = 0
size = len(toInt)

while i < size:
    
    # Eğer son karakterse direkt ekle ve çık
    if i == size - 1:
        result += symbol_dict[toInt[i]]
        break
    
    current = symbol_dict[toInt[i]]
    next_val = symbol_dict[toInt[i + 1]]
    
    # Subtractive case
    if current < next_val:
        result += (next_val - current)
        i += 2
    else:
        result += current
        i += 1

print(result)

print("******************** Leetcode Solution ********************")

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and symbol_dict[s[i]] < symbol_dict[s[i+1]]:
                result -= symbol_dict[s[i]]
            else:
                result += symbol_dict[s[i]]
        return result
