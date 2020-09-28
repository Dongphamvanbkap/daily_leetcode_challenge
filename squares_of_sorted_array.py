a = [-4,-1,0,3,10]
n = len(a)

i = -1
while i + 1 < n and a[i+1] < 0:
	i += 1

j = n
while j - 1 >= 0 and a[j-1] >= 0:
	j -= 1

v = []

while i >= 0 or j < n:
	if i >= 0 and j < n:
		ii = a[i] * a[i]
		jj = a[j] * a[j]
		if ii < jj:
			v.append(ii)
			i -= 1
		else:
			v.append(jj)
			j += 1
	elif i >= 0:
		v.append(a[i] * a[i])
		i -= 1
	else:
		v.append(a[j] * a[j])
		j += 1
print(v)


