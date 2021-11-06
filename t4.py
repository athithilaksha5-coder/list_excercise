#string = 'Monday Tuesday Wendesday Thursday Friday Saturday Sunday'
#output = Saturday Sunday

string = 'Monday Tuesday Wendesday Thursday Friday Saturday Sunday'
l =string.split()
print(l)
	
for j in l:
	if j[0]=='S':
		print(j,end=' ')
		
	