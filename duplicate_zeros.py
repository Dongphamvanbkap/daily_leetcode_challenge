a = [1,0,2,3,0,4,5,0, 0, 0, 0, 0]
n = len(a)
i = 0
while i >= 0 and i < n:
	if a[i] == 0:
		for j in range(n-2, i, -1):
			a[j+1] = a[j]
		if i + 1 < n:				
			a[i+1] = 0
		i += 2
	else:
		i += 1	

print(a)		
			


