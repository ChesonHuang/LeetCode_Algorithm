#!/usr/bin/python
#coding:utf-8
'''
题目要求：
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串
如：输入'hello world'---> 输出5
'''
def lengthOfLastWord(s):
	# 解法一：直接用内置函数split()
	# res = s.split()
	# if not res:
	# 	return 0
	# return len(res[-1])
	
	# 解法二：遍历所有的字符，遇到空格，就判断后面是否还有字符，如果没有，返回目前结果，否则，就置1
	count =0
	flag = False # 用来判定后面是否有字符
	for x in s:
		if x == ' ':
			flag = True
		else:
			if flag:    # 说明之前的是空字符
				count = 1
			else:
				count +=1
	return count
		
	