class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # convert x to string
        x_str = str(x)

        # start and end index
        start_index = 0
        end_index = len(x_str) - 1
        
        # pointer for each end of x
        start_point = x_str[start_index]
        end_point = x_str[end_index]

        # check if start and end point are not equal
        while start_index != len(x_str) // 2 and start_index != end_index:
            print(x_str[start_index])
            if start_point != end_point:
                return False
            
            # increment start_index, decrement end_index and set start_point and end_point
            start_index += 1
            end_index -= 1

            start_point = x_str[start_index]
            end_point = x_str[end_index]

        # return true if number passes through the while loop
        return True

# IMPROVEMENTS: Optimal solution reverses string in-line (x_str[::-1] and returns if x is equal to this reversed string) and does not require pointers (more efficient in memory)
