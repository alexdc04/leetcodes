class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = list()

        for index in range(len(min(strs, key = lambda x: len(x)))):
            curr_letter = strs[0][index]
            for word in strs:
                if word[index] != curr_letter:
                    return "".join(prefix)
            prefix.append(strs[0][index])


        return "".join(prefix)
