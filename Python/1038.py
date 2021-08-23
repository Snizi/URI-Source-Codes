x, y = map(int, input().split())

menu = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

sum = 0

for key in menu:
    if x == key:
        sum = menu[key] * y
        print('Total: R$ {:.2f}'.format(sum))
        break
