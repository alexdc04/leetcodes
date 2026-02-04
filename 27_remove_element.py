class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while val in nums:
            nums.remove(val)

        return len(nums)

# this was way easier than I thought it was, haha
