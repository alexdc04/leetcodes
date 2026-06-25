class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for char_index in range(len(haystack)):
            # print(haystack[char_index:char_index + len(needle)])
            if haystack[char_index:char_index + len(needle)] == needle:
                return char_index
            
        return -1

# Time complexity: O(N), space complexity: O(1)
