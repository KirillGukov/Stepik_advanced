text = input().split(sep=" ")
count, pos = 0, 0
while pos <= len(text) - 2:
    if int(text[pos]) < int(text[pos + 1]):
        count += 1
    pos += 1
print(count)
