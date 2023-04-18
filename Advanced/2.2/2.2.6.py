nums = [int(input()) for _ in range(int(input()))]
num_max = int(input())
res = 'НЕТ'
n = len(nums)
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            if nums[i] * nums[j] == num_max:
                res = 'ДА'
                break
print(res)
