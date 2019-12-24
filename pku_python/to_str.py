#!/usr/bin/python
#-*-coding:utf-8-*-
'''
分别用栈和递归的方式实现进制转换
'''

class ToStr():
	def __init__(self,num,base):
		self.num = num
		self.base = base
		self.s =[]
	def stack(self):
		while self.num>0:
			mod = self.num % self.base
			self.num //= self.base
			self.s.append(mod)
		return self.s[::-1]
		
def backcall(num,base):
	if num <base:
		return num
	else:
		return backcall(num//base,base)
                
		
if __name__=='__main__':
	s = ToStr(10,8)
	print(s.stack())
	b = backcall(10,2)
	print(b)
