timur = input()
ruslan = input()
i = 0
game_rules = {'ножницы': ['бумага', 'ящерица'],
              'бумага': ['Спок', 'камень'],
              'камень': ['ящерица', 'ножницы'],
              'ящерица': ['Спок', 'бумага'],
              'Спок': ['ножницы', 'камень']}
if timur == ruslan:
    print('ничья')
elif ruslan == game_rules[timur][0] or ruslan == game_rules[timur][1]:
    print('Тимур')
else:
    print('Руслан')
