from sys import stdin, stdout

string = stdin.readline().strip()
q = int(input())

array = [0]

for word in string:
    array.append(array[-1] + hash(word))
    
def check(start, end):
    return array[end] - array[start-1]

for _ in range(q):
    a, b, c, d = map(int, stdin.readline().split())
    if check(a,b) == check(c,d):
        print("YES")
    else:
        print("NO")