class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        if (digits[-1] < 10):
            return digits
        else:
            for i in range(len(digits)):
                digits[-(i + 1)] = 0

                if (len(digits) < i + 2):
                    # print(digits)
                    digits.insert(-(i + 2), 0)
                    # print(digits)
       

                digits[-(i + 2)] += 1
                # print(digits[-(i + 2)])
                if (digits[-(i + 2)] < 10):
                    return digits

# Space complexity: O(1), time complexity O(N), no improvements found
                
