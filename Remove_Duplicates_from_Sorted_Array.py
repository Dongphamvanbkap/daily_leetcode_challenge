nums = [0,0,1,1,1,2,2,3,3,4]

n = len(nums)
i = 1
k = 0

while i > 0 and i < n:
	if nums[k] != nums[i]:
		k += 1
		nums[k] = nums[i]
		i += 1
	else:
		i += 1

print(k + 1)		

			
