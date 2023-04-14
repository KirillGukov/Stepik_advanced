num = 0
n = int(input())
k = int(input())
for i in range(1, n + 1):
    num = (num + k) % i
print(num + 1)
