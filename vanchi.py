## Given a,k,m  compute b = a^k (mod m)
## through iterated squaring
from sys import argv
a = int(argv[1])
k = int(argv[2])
m = int(argv[3])


b=1
pow=a
while (k>0):
   if k%2==1:
       b = (b*pow)%m
   pow = (pow*pow)%m
   k = k//2
print (argv[1],"^",argv[2],"=",b, "(mod",argv[3],")")

