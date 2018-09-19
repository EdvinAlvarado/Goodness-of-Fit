
E = [15, 2.7, 15, 3]
OGlist = E
print("list is %s\n" %E)

# def addtill5(l):
# 	lst = []
# 	counter =[]
# 	#avoids changing the original list
# 	for i in l:
# 		lst.append(i)
# 	for i in range(len(lst)):
# 		print(i)
# 		print('list value is %s' %lst[i])
# 		if (lst[i] < 5.) and (i < len(lst)-1):
# 			lst[i] += lst[i+1]
# 			lst.insert(len(lst)+n,lst[i+1])
# 			n+=1
# 			lst.pop(i+1)
# 			# break
# 		elif (lst[i] < 5.) and (i == len(lst)-1):
# 			lst[i] += lst[i-1]
# 			lst.pop(i-1)
# 			# break
# 		print("step list %s\n" %lst)
# 	lst = lst[:len(lst)-1]
# 	return lst

# def addtill5(l):
# 	lst = []
# 	addlist = []
# 	counter = []
# 	comcounter = []
# 	#avoids changing the original list
# 	for i in l:
# 		lst.append(i)
# 	for i in range(len(lst)):
# 		print(i)
# 		print('list value is %s' %lst[i])
# 		if (lst[i] < 5) and (i < len(lst)-1):
# 			addlist.append(lst[i]+lst[i+1])
# 			counter.append(i)
# 			comcounter.append(i+1)
# 			# break
# 		elif (lst[i] < 5) and (i == len(lst)-1):
# 			addlist.append(lst[i]+lst[i-1])
# 			counter.append(i)
# 			comcounter.append(i-1)
# 			# break
# 		print("add list %s" %addlist)
# 		print("counter %s" %counter)
# 		print("complementary counter %s" %comcounter)
# 		print("step list %s\n" %lst)
# 	print("--------------------\n")
# 	for i in range(len(addlist)):
# 		lst[counter[i]] = addlist[i]
# 		print('adding to list %s' %lst)
# 	n=0
# 	for i in comcounter:
# 		del lst[i-n]
# 		n+=1
# 		print('removing from list %s' %lst)
# 	print('\nfinal result: %s' %lst)
# 	return lst

def addtill5(l):
	lst = []
	#avoids changing the original list
	for i in l:
		lst.append(i)
	for i in range(len(l)):
		print('\nOG list %s' %i)
		print('+++++++++++++++++++++')
		for i in range(len(lst)):
			print('new list %s' %i)
			print('list value is %s' %lst[i])
			if (lst[i] < 5.) and (i == 0):
				lst[i] += lst[i+1]
				lst.pop(i+1)
				print("%s" %lst)
				break
			elif (lst[i] < 5.) and (i < len(lst)-1) and (i != 0):
				#won't work if the adjacent values are identical
				#it seems to sum the former instead of the latter when both are equal.
				lst[i] += min(lst[i+1],lst[i-1])
				lst.pop(lst.index(min(lst[i+1],lst[i-1]))) 
				print("%s" %lst)
				break
			elif (lst[i] < 5.) and (i == len(lst)-1):
				lst[i] += lst[i-1]
				lst.pop(i-1)
				print("%s" %lst)
				# break
			else:
				print("%s" %lst)
			print('-------------------')
		print('+++++++++++++++++++++')
	return lst


newE = addtill5(E)
# print(OGlist)
# print(newE)

# for i in range(len(E)):
# 	print(i)
# 	if i < len(E)-1:
# 		print(E[++i])







