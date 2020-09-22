import math

global maximum 

def _lis(arr , n ): 
    global maximum 
    if n == 1 : 
        return 1
    maxEndingHere = 1
    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i-1][1] < arr[n-1][1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
    maximum = max(maximum , maxEndingHere) 

    return maxEndingHere 

def lis(arr):
    global maximum 

    n = len(arr) 

    maximum = 1

    _lis(arr , n) 

    return maximum

m = int(input())
x, y = (input().split())
alpha1 = math.atan(eval(x))
alpha2 = math.atan(eval(y))
alpha3 = alpha2 - alpha1
coordinates = [] 
for i in range(m):
    x, y = (input().split())
    coordinates.append((int(x),int(y)))

# coordinates.sort(key=lambda tup: tup[1])
# final = lis(coordinates)

# print(final)

# print(coordinates)
# print(alpha1, alpha2)
# print(m)