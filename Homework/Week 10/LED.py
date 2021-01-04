n = int(input())

x = n // 3
r = n % 3

if(r == 0):
    print(x * 7)
elif(r == 1):
    print((x - 1) * 7 + 4)
elif(r == 2):
    print(x * 7 + 1)