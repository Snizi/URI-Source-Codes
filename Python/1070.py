entry = int(input())

c = 0
for i in range(entry, entry*5):
    if c == 6:
        break
    else:
        if i % 2 != 0:
            c += 1
            print(i)
