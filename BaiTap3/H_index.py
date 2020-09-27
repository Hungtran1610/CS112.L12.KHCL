n = int(input())
if n > 0:
    a = list(map(int, input().split()))

sum = 0

if not a:
    print(0)
sum  = max([min(i + 1, c) for i, c in enumerate(sorted(a, reverse=True))])
    
print(sum)