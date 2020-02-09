#-*-coding:utf-8-*-
class Solution:
	def __init__(self,string):
		self.string = string
		
	def method1(self):
		'''
		暴力法
		'''
		res =self.string[0]
		l = len(self.string)
		for i,x in enumerate(self.string):
			for j in range(i+1,l):
				if self._vaild(self.string,i,j):
					res = self.string[i:j+1] if j+1-i>len(res) else res
		return res
	def method2(self):
		
	def method3(self):
		
	def method4(self):
		
	def _vaild(self,s,left,right):
		while left <= right:
			if s[left] != s[right]:
				return False
			left +=1
			right -=1
		return True