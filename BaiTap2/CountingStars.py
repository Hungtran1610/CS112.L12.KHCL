import math

def lis(arr, n):
    temp_list = [1 for x in range(0,n)]
    i,j = 1,0
    while i<len(arr) and j<len(arr):
        if arr[j][1]<arr[i][1]:
            if temp_list[j]+1>temp_list[i]:
                temp_list[i] = temp_list[j]+1
        j=j+1
        if j==i:
            j,i=0,i+1
    return max(temp_list)

def line_function(x, y, angle):
    return y - math.tan(angle)*x

def translating(x, y, angle):
    k = y/math.tan(angle) - x
    return math.tan(angle)*k

m = int(input())
x, y = (input().split())
alpha1 = math.atan(eval(x))
alpha2 = math.atan(eval(y))
alpha3 = alpha2 - alpha1
coordinates = [] 
for i in range(0,m):
    x, y = (input().split())
    if line_function(float(x), float(y), alpha1) < 0:
        continue
    if line_function(float(x), float(y), alpha2) > 0:
        continue
    y_ = translating(float(x), float(y), alpha2 - alpha1)
    coordinates.append((float(x), float(y), y_))

coordinates.sort(key=lambda tup: tup[2], reverse=True)
final = lis(coordinates, m)

print(final)