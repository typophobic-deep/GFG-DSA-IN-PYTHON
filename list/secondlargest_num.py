class Solution:

	def print2largest(self,arr, n):
		lar=arr[0]
		slar=None
	
		for x in arr[1:]:
		    if x>lar:
		        slar=lar
		        lar=x
		    elif x!=lar:
		        if slar==None or slar<x:
		            slar=x
		            
        if slar==None:
            return -1           
		return slar          


