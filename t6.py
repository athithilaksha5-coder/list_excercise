#l =[10,20,25,30,32,8,12]
#OUTPUT: 10 5 5 2 -24 4


l =[10,20,25,30,32,8,12]

for i in range(len(l)-1):
	d=l[i+1]-l[i]
	if d<0:
		print(-(d))
	else:
		print(d)
	#print(d)
