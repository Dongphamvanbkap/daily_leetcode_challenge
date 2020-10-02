nums = [0, 1, 2, 2, 3, 0 ,4, 2]
val = 2

i =0
n = len(nums)
print(n)
k = 0

while i >= 0 and i < n:
	if nums[i] == val:
		i += 1
	else:
		nums[k] = nums[i]
		i += 1
		k += 1
print(k)
print(nums[:k])			