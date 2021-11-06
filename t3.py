# String : Nov1 Nov2 Nov3 Nov4 Nov5
# Output: Nov1 2021 Nov2 2021 Nov3 2021 Nov4 2021 Nov5 2021

string = 'Nov1 Nov2 Nov3 Nov4 Nov5'
l=string.split()
print(l)
	
s1='' 	

for j in l:
	s1+=j[:4]+' 2021 '
else:
	print(s1)
	

