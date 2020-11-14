arr = [3,1,7,11]

n = len(arr)
i = 0
condition = False
while i >= 0 and i <= n - 2:
	j = i + 1
	while j < n:
		if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
			condition = True
			break
		else:
			j += 1
	if condition == True:
		break
	else:
		i += 1			

print(condition)			
