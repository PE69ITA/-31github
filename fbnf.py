class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or x % 10 == 0:
            return False

        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10

        return True
    
sol = Solution()
print(sol.isPalindrome(231))  # True