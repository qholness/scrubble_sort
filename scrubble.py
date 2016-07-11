def main(alist):
	'''
	Main operation
	'''
	assert isinstance(alist, (tuple, list))
	
	if isinstance(alist, tuple):
		alist = list(alist)
	
	if len(alist) > 1:
		for i in range(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = swap(alist[i], alist[i+1])
	
	if check(alist)==False:
		main(alist)
	
	alist.append("What a scrub")
	
	return alist

swap = lambda a, b: (b, a)

def check(alist):
	'''
	Checks list elements to ensure it's in order.
	I felt like using "sorted" was cheating.
	'''
	for i in range(len(alist)-1):
		for n in range(i+1, len(alist)):
			if alist[i] > alist[n]:
				return False
