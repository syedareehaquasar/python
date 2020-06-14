n = int(input())
 
a = list(map(int,input().split()))
b = [-1 for i in range(n)]
 
for i in range(1,n):
 
	if a[i] != a[i-1]:
		b[i] = a[i-1]
 
 
MEX = 0
j = 0
# print(b)
l = []
while j <= n-1:
 
	if MEX < a[j]:
		l.append(MEX)
		MEX = MEX + 1
	elif MEX == a[j]:
		# print(j)
		MEX = MEX + 1
		j = j + 1
	elif MEX > a[j]:
		# print(MEX,"--")
		j = j + 1
	else:
		l.append(MEX)
		MEX = MEX + 1
while len(l) < n:
	l.append(MEX)
	MEX = MEX + 1
 
j = 0
for i in range(n):
 
	if b[i] == -1:
		b[i] = l[j]
		j = j + 1
print(*b)
