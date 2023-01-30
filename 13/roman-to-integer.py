class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
                res += roman_map[s[i]] - 2 * roman_map[s[i - 1]]
            else:
                res += roman_map[s[i]]
        return res

      
'''
The code logic is as follows:

Initialize a dictionary roman_map to store the mapping between the Roman numeral characters and their corresponding integer values.

Initialize a variable res to store the final integer value.

Iterate over the input string s and for each character s[i]:

a. If i is greater than 0 and the value of the current character s[i] is greater than the value of the previous character s[i - 1], it means that the current character is used for subtraction (e.g. IV for 4, IX for 9). In this case, add roman_map[s[i]] - 2 * roman_map[s[i - 1]] to res.

b. If i is equal to 0 or the value of the current character s[i] is not greater than the value of the previous character s[i - 1], add roman_map[s[i]] to res.

Return res as the final result. 

The calculation roman_map[s[i]] - 2 * roman_map[s[i - 1]] is used to subtract the value of the previous character (s[i-1]) twice to account for it being added and then subtracted again. This ensures that the correct integer value is computed for the Roman numeral.
'''
