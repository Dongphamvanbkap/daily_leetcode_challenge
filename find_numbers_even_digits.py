nums = [12,345,2,6,7896]


class Solution:
    def countNumberOfDigit(self, num):
        count = 0
        while num != 0:
            num = num // 10
            count += 1
        return count    
        
    def findNumbers(self, nums):
        count = 0
        for num in nums:            
            if self.countNumberOfDigit(num) % 2 == 0:
                count += 1
        return count        
        
Sol = Solution()
print(Sol.findNumbers(nums))       