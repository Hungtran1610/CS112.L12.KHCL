a, k, b, m, n = [int(x) for x in input().split()]


def S(x):
    return a * (x - x//k) + b * (x - x//m)


res = -1
low = 0
high = int(1e18)

# tìm kiếm nhị phân
while low <= high:
    mid = (low + high) //2
    if S(mid) >= n: 
        res = mid
        high = mid - 1
    else:                  
        low = mid + 1

print(res)