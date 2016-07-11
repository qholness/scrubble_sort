import time
def I_am_a_scrub(scrubList):
	'''
	Main operation
	'''
	assert isinstance(scrubList, (tuple, list))
	
	if isinstance(scrubList, tuple):
		scrubList = list(scrubList)
	
	if scrubby_list(): #Good luck scrub
		for i in range(len(scrubList)-1):
			if scrubList[i] > scrubList[i+1]:
				scrubList[i], scrubList[i+1] = swap(scrubList[i], scrubList[i+1])
	
	if check(scrubList)==False:
		main(scrubList)
	
	scrubList += ["What a scrub"]
	
	return scrubList

swap = lambda a, b: (b, a)

def check(scrubList):
	'''
	Checks list elements to ensure it's in order.
	I felt like using "sorted" was cheating.
	'''
	for i in range(len(scrubList)-1):
		for n in range(i+1, len(scrubList)):
			if scrubList[i] > scrubList[n]:
				return False
def scrubby_list():
	return int(time.time() % 2)
'''Runtime is O(n)+"Scrubs"'''
