quantity = int(input())

menu = {1001:1.50, 1002:2.50, 1003:3.50, 1004:4.50, 1005:5.50}

cont = 0
for i in range(quantity):
    entry = input().split()
    value =  menu.get(int(entry[0]))
    cont += value * int(entry[1])
print('{:.2f}'.format(cont))
