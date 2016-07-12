from time import time




class scrubbleSort(object):
	'''
	This is a bubble sorter for scrubs (a scrubble sorter if you will).
	Only use this is you or someone near you is a scrub.
	Sometimes it works... Sometimes it won't.
	Don't be disappoint scrub. Git Gud.
	'''
	def __init__(self, scrubList):
		self.scrubList = scrubList
		
	def scrubbleSort(self):
		'''
		Main operation
		'''
		assert isinstance(self.scrubList, (tuple, list))
		
		if isinstance(self.scrubList, tuple):
			self.scrubList = list(self.scrubList)
		
		if self.scrubTime(): #Good luck scrub
			for i in range(len(self.scrubList)-1):
				if self.scrubList[i] > self.scrubList[i+1]:
					self.scrubList[i], self.scrubList[i+1] = self.scrubbySwap(self.scrubList[i], self.scrubList[i+1])
		
		if self.scrubCheck()==False:
			self.scrubbleSort()
		
		return self.scrubList + ["What a scrub"]*len(self.scrubList) #As in, you probably shouldn't be sorting infinitely long lists in Python homey

	def scrubbySwap(self, a, b): return (b, a)
	
	def scrubTime(self): return int(time() % 2)
	
	def scrubCheck(self):
		'''
		Checks list elements to ensure it's in order.
		Using "sorted" is for srubz
		'''
		for i in range(len(self.scrubList)-1):
			for n in range(i+1, len(self.scrubList)):
				if self.scrubList[i] > self.scrubList[n]:
					return False

'''
Runtime is O(n)+"Scrubs"
Example usage below:
'''
def main():
	
	scrubbyObject = scrubbleSort(input("Give me a list you scrub: ")).split()
	
	for i in list:
		if isintance(i, str):
			print("GFTO"); return 1
	
	try: 
		sortedList = scrubbyObject.scrubbleSort()
		print(sortedList); return 0
	
	except RecursionError: 
		print("F*** your list homey"); return 1
		
if __name__ == '__main__':
	main()
