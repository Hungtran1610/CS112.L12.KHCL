gen1 = input().strip()
gen2 = input().strip()

dictA = {}
for i in range(0, len(gen2)-1):
    if (gen2[i] + gen2[i+1]) not in dictA:
        dictA[gen2[i]+gen2[i+1]] = 1
    else:
        dictA[gen2[i]+gen2[i+1]] += 1

res = 0
for i in range(0, len(gen1)-1):
    if (gen1[i] + gen1[i+1]) in dictA:
        res += 1

print(res)