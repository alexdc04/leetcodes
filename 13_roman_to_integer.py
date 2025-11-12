class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # roman numeral values
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'end': 0}

        # previous character
        ch_next = 'end'

        # ignore flag
        ignore = 0

        # sum
        total = 0

        # iterate through characters
        for ch_index in range(0, len(s)):
            if (ignore == 1):
                ignore = 0
                continue

            ch = s[ch_index]

            # char lookahead
            if (ch_index + 1 < len(s)):
                ch_next = s[ch_index + 1]
            else:
                ch_next = 'end'

            if ((ch == 'I' and (ch_next == 'V' or ch_next == 'X')) or 
            (ch == 'X' and (ch_next == 'L' or ch_next == 'C')) or 
            (ch == 'C' and (ch_next == 'D' or ch_next == 'M'))):
                ignore = 1
                total += (romans[ch_next] - romans[ch])
                continue
            else:
                ignore = 0
                total += romans[ch]

        return total

# IMPROVEMENTS: Solid runtime, can be slightly optimized without the ignore flag and using a while loop and manually incrementing a value by 1 or 2 depending on if subtraction is needed
