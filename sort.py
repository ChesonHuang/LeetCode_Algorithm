#!/usr/bin/python
#-*-coding:utf-8-*-

import os

class Sort():
	def __init__(self):
		pass
	
	def selsort(self,array):
		print("origin data:",array)
		for i in range(len(array)):
			m = i
			for j in range(i+1,len(array)):
				if array[j]<array[m]:
					m = j
			if not m==i:
				tmp = array[i]
				array[i] = array[m]
				array[m] = tmp
		print("sorted data:",array)
		return array
	
	def insort(self,array):
		print("origin data:",array)
		for i in range(len(array)):
			tmp = array[i]
			for j in range(i-1,-1,-1):
				if tmp < array[j]:
					array[j+1] = array[j]
				else:
					array[j+1]= tmp
					break
			
		print("sorted data:",array)
		return array
		
	def bubsort(self,array):
		pass
		
if __name__=='__main__':
	s = Sort()
	#s.selsort([1,3,5,3,8])
	s.insort([1,3,5,3,8])