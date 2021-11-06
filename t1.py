#string : ABCDABCABA
#Output: ABCD
#used: append() join()

string = 'ABCDABCABA'
l1=[]
#for i in string:
#	if i not in l1:
#		l1.append(i)
#print(l1)
#print("".join(l1))
l2=[l1.append(i) for i in string if i not in l1]
print(''.join(l1))



