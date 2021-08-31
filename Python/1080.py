values = []

for i in range(100):
    values.append(int(input()))

precessor = 0
pos = 0

for i in range(100):
    if values[i] > precessor:
        precessor = values[i]
        pos = i + 1

print(precessor)
print(pos)
