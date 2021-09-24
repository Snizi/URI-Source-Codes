divide = []

for i in range(2, 101):

    divide.append(1/i)
    

count = 0 

for i in divide:
    count += i
print('{:.2f}'.format(1+count))
