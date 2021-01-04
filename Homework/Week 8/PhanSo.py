from math import gcd 

a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = 0
temp = c/d


while (a/b < temp): 
    a += 1
    b += 1
    count += 1
    
    ucln = gcd(a,b)
    a = a // ucln
    b = b // ucln
    
if (a/b > temp):
    print(0)
else:
    print(count)