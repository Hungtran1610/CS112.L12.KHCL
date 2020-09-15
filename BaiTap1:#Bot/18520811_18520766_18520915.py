n = int(input())

data = list(map(int, input().split()))


max_so_far = - 1
max_ending_here = 0
start = 0
end = 0
s = 0

for i in range(0,n):   
    data[i] = int(data[i]) #convert str to int
    max_ending_here += data[i] 

    if max_so_far < max_ending_here:
        max_so_far = max_ending_here 
        start = s 
        end = i 

    if max_ending_here < 0:
        max_ending_here = 0
        s = i+1

print (start+1, end+1, max_so_far)