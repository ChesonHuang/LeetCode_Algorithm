def findNumber(n,*args):
	m1,m2,m3,x1,x2 =0,0,0,0,0
	for i in range(n):
		if args[i] > m3:
			m1 = m2
			m2 = m3
			m3 = args[i]
		elif args[i] > m2:
			m1 =m2
			m2 = args[i]
		elif args[i] > m1:
			m1 = args[i]
		elif args[i] < x2:
			x1 = x2
			x2= args[i]
		elif args[i] < x1:
			x1 = args[i]
	return max(m1*m2*m3,x1*x2*m3)

if __name__=='__main__':
	r=findNumber(5,2,1,-3,1,-1)
	print(r)
