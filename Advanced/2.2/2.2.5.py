text = input().split()
d = {}
col = 1
for i in text:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(len(d.keys()))