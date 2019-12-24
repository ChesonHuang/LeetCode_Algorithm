#!/usr/bin/python
#-*-coding:utf-8-*-
import heapq
class Solution:
	def findKthLargest(self,nums,k):
		# return sorted(nums)[-k]
		'''
		why below solution is error
		return nums.sort()[-k]
		'''
		return heapq.largest(k,nums)[-1]