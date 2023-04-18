text = input().split()
for i in range(0, len(text) - 1, 2):
    text[i], text[i + 1] = text[i + 1], text[i]
    i += 1
print(' '.join(text))
