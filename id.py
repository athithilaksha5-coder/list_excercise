import copy
old_list =[[10,20,30],[40,50,60],[70,80,90]]
new_list = copy.copy(old_list)

old_list.append([1,2,3])
old_list[1][1]='SHALLOW'

print("Old list: ",old_list)
print("New list: ",new_list)