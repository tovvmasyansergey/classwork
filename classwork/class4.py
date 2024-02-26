#mstr = input("Enter a sentence: ")
#ml = mstr.split()
#
#maxword = ""
#for el in ml:
#	if len(el) > len(maxword):
#		maxword = el
#
#print(maxword)

mstr = input("Enter a sentence: ")
#tmp = ""
#for i in range(len(mstr) - 1, -1, -1):
#	tmp += mstr[i]
#print(tmp)
tmp = ""
for el in mstr:
	tmp = el + tmp
print(tmp)

#mstr = input("Enter a sentence: ")

#ml = mstr.split()

#for i in range(len(ml)):
#	if (len(ml[i]) % 2 == 0):
#		ml[i] = ml[i].lower()	
#	else:
#		ml[i] = ml[i].upper()	
#
#tmp = " ".join(ml)
#print(tmp)

