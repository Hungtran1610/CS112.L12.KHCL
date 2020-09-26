def SeaWeeds(x, k):
    n1 = 0
    n2 = x
    n3 = 0
    sum = 0
    for i in range(0,k*2+1):
        sum = n1 + n2
        n1 = n2
        n2 = sum
        n3 = n3 + 1
    return n1

n, k = map(int, input().split())
kq = SeaWeeds(n,k)
m = 1000000007
print(kq%m)