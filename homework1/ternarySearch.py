def ternarySearch(a, k):
	la = len(a)
	m1 = int(la / 3)
	m2 = 2 * m1
	if k == a[m1]:
		return True
	elif k == a[m2]:
		return True
	elif la == 0:
		return False
	elif la == 1:
		if k == a[0]:
			return True
		elif k != a[0]:
			return False
	elif la == 2:
		if k == a[0]:
			return True
		elif k == a[1]:
			return True
		else:
			return False
	elif k < a[m1]:
		return ternarySearch(a[0:m1], k)
	elif k > a[m1] and k < a[m2]:
		return ternarySearch(a[m1:m2], k)
	else:
		return ternarySearch(a[m2:], k)

print ternarySearch([2,3,4,5,6], 1)
