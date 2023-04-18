col = int(input())
first_term, second_term, third_term, fourth_term = 0, 0, 0, 0
for i in range(col):
    cords = input().split(sep=" ")
    if int(cords[0]) > 0 and int(cords[1]) > 0:
        first_term += 1
    elif int(cords[0]) < 0 and int(cords[1]) > 0:
        second_term += 1
    elif int(cords[0]) < 0 and int(cords[1]) < 0:
        third_term += 1
    elif int(cords[0]) > 0 and int(cords[1]) < 0:
        fourth_term += 1
print('Первая четверть:', first_term)
print('Вторая четверть:', second_term)
print('Третья четверть:', third_term)
print('Четвертая четверть:', fourth_term)
