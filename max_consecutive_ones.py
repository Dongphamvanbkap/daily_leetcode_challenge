a = [1,1,0,1,1,1]


def findMaxConsecutiveOnes(nums=[]):
    count = 0
    max_con_ones = 0
    for i in nums:
        if i == 1:
            count += 1
            max_con_ones = max(max_con_ones, count)
        else:
            count = 0
    return max_con_ones

print(findMaxConsecutiveOnes(a))