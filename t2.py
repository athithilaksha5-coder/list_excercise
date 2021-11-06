# String : Nov1 Nov2 Nov3 Nov4 Nov5
# Output: Nov 1 Nov 2 Nov 3 Nov 4 Nov 5

string = 'Nov1 Nov2 Nov3 Nov4 Nov5'

#s=''
l=string.split()
print(l)
#for i in string:
	
#	if i!=' ':
#		s+=i
#	
#	if i==' ':
#		l.append(s)
#		s=''
#else:
#	l.append(s)
#	#print(s)
#	print(l)

s1=''
for i in l:
	s1+=i[:3]+' '+i[3]+' '

else:
	print(s1)

	
