class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = 0.1
        index = 0

        while index < len(nums):
            if nums[index] == prev_num:
                del nums[index]
                continue
            prev_num = nums[index]
            index += 1

        return len(nums)

# optimization: deleting each element doesn't need to happen, the elements can be shuffled around instead; keeping the list elements the same without recreating the list every single time
