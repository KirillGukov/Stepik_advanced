count = 0
for i in input():
    count += 1
price = count * 60
rub = price // 100
cop = price % 100
print(rub, 'р.', cop, 'коп.')
