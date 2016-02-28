def merge(a, b):
	la = len(a)
	lb = len(b)
	i = 0
	j = 0
	mergeList = a + b
	n = len(mergeList)
	newList = []
	while len(newList) < n:
		if i == la:
			for k in range(j, lb):
				newList.append(b[k])
			break
		if j == lb:
			for k in range(i, la):
				newList.append(a[k])
			break
		if a[i] < b[j]:
			newList.append(a[i])
			i = i + 1
			#print i
		else:
			newList.append(b[j])
			j = j + 1
			#print j
	return newList

array = [1,3,2,5,4]
array2 = [6,8,7,9]

print(merge(array,array2))
