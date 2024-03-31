#1
#word = input()
#lm = word.split()
#ml = []
#for i in lm:
#	ml.append(len(i))
#print(ml)
#2
#word = input()
#lm = ""
#for i in word:
#	if ord(i) > 96 and ord(i) < 123:
#		lm += chr(ord(i) - 32)
#	elif ord(i) > 65 and ord(i) < 91:
#		lm += chr(ord(i) + 32)
#	else:
#		lm += i
#print(lm)
#3
#num = ""
#count = []
#count_even = []
#while num != "stop":
#	num = input()
#	if num.isdigit() and int(num)%2 == 0:
#		count.append(int(num))
#	if num.isdigit() and int(num)%2 != 0:
#		count_even.append(int(num))
#count.sort()
#count_even.sort()
#print(count , " " , count_even)
#4
sent = input()
num = int(input())
ml = sent.split()
res = []
for i in ml:
	if len(i) >= num:
		res.append(i)
res.sort()
print(res)

