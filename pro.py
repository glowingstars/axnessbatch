def third(elem):
	return elem[1]
s=[(2, 1), (1, 3), (4, 2), (0, 0)]
s.sort(key=third)
print(s)