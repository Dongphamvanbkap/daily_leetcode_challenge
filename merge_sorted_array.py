nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

n = len(nums1) - 1
i = n - len(nums2)
j = len(nums2) - 1


while i >= 0 or j >= 0:
	if i >= 0 and j >= 0:
		if nums2[j] >= nums1[i]:
			nums1[n] = nums2[j]
			n -= 1
			j -= 1
		else:
			nums1[n] = nums1[i]
			n -= 1
			i -= 1
	elif i >= 0:
		nums1[n] = nums1[i]
		n -= 1
		i -= 1
	else:
		nums1[n] = nums2[j]
		n -= 1
		j -= 1

print(nums1)