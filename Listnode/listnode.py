#!/usr/bin/python
#-*-coding:utf-8-*-

'''
python 链表
属性；链表头：head；链表长度：length
'''
class Node:
	'''
	数据结构，定义节点：data,next
	data:节点保存的数据
	next:指向下一个节点数据地址
	'''
	def __init__(self,data,pnext=None):
		self.data = data
		self.next = pnext
		
	def __repr__(self):
		'''
		定义Node的字符输出
		'''
		return "{!r}".format(self.data)
		
	def __str__(self):
		return "{}".format(self.data)
		
class ChainTable():
	def __init__(self):
		'''
		初始化链表头节点和长度
		'''
		self.head = None
		self.length = 0
	
	def isEmpty(self):
		return self.length==0
		
	def append(self,dataOrNode):
		'''
		链表元素的添加，链表尾部添加
		'''
		item = None
		if isinstance(dataOrNode,Node):
			item = dataOrNode
		else:
			item = Node(dataOrNode)
			
		# 如果没有头节点，指定头节点
		if not self.head:
			self.head = item
			self.length +=1
		else:
			node = self.head  # 指向当前节点
			while node.next:
				node = node.next # 下一个节点便成为当前节点
			#此时，节点以指向链表尾部，可以添加节点
			node.next = item
			self.length +=1
			
	def delete(self,index): # 删除指定节点
		'''
		要删除一个节点，只需把删除节点前一个地址节点指向其后一个数据节点
		node.previous.next = node.next
		'''
		if self.isEmpty():
			print("Chain Table is empty")
			return
		
		if index< 0 or index > self.length:
			print("Error: out of index")
			return
		
		j =0
		node = self.head
		prev = self.head
		while j < index:
			prev,node = node,node.next
			j +=1
		
		prev.next = node.next
		self.length -=1
		
	def insert(self,index,dataOrNode):
				
			
		