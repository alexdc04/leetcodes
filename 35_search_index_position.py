class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # this is a binary search problem; start at the middle index
        # rollover: since this method cuts down the nums list, it is necessary to keep track of how many elements have been removed
        ind = len(nums) // 2
        rollover = 0

        # the final step in this problem is when the length of nums has shrank to 1
        while (len(nums) > 1) :
            # if the target is in the larger half of the list, slice the list to be the middle to the end of it and add the amount of cut elements (or ind) to the rollover
            if (target > nums[ind]):
                nums = nums[ind:len(nums)]
                rollover += ind

            # no rollover necessary in the opposite case; slice list to be the beginning to the middle
            elif (target < nums[ind]):
                nums = nums[0:ind]

            # target found; add the ind plus the rollover
            else:
                return ind + rollover
            
            # find the midpoint of the next list
            ind = len(nums) // 2
            
        # this if/else only runs if the target is NOT found in the final list; if it's larger than the remaining value, add one to the ind and rollover, otherwise just return the ind and rollover
        if (target > nums[0]):
            return ind + rollover + 1
        else:

            return ind + rollover

# IMPROVEMENTS: cutting the list is not necessary; separate pointers can be used for the start, middle and ending, 
# where the start and end can move based on the middle of the list, where the middle is updated based on the new start/end values
