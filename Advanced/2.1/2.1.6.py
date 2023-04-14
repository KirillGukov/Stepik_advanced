text = input()
if len(text) == 5:
    print(int(text[::-1]))
else:
    print(int(text[0] + text[5:0:-1]))