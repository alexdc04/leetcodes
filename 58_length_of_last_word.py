 def lengthOfLastWord(self, s: str) -> int:
        
        words = s.split()
        return len(words[-1])

# IMPROVEMENTS: rsplit function exists and maxsplit = 1 can be used to only split one word, but this is otherwise optimal as far as I am aware
