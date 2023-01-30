[LeetCode Link](https://leetcode.com/problems/roman-to-integer/submissions/887770601/)

Consider the following test cases:

Input: "III"
Output: 3
Explanation: The Roman numeral "III" represents the integer 3 (1 + 1 + 1).

Input: "IV"
Output: 4
Explanation: The Roman numeral "IV" represents the integer 4 (5 - 1).

Input: "IX"
Output: 9
Explanation: The Roman numeral "IX" represents the integer 9 (10 - 1).

Input: "LVIII"
Output: 58
Explanation: The Roman numeral "LVIII" represents the integer 58 (50 + 5 + 3).

Input: "MCMXCIV"
Output: 1994
Explanation: The Roman numeral "MCMXCIV" represents the integer 1994 (1000 + 900 + 90 + 4).

In each of these test cases, the code uses the romanToInt function to convert the Roman numeral string to an integer. The function uses the dictionary roman_map to store the mapping between the Roman numeral characters and their corresponding integer values. It then uses a loop to iterate over the characters in the input string s. If the current character is used for subtraction (e.g. IV, IX), its value is subtracted from the result twice to cancel out its previous addition. If the current character is not used for subtraction, its value is simply added to the result. The final result is returned as the integer representation of the Roman numeral.




