def RepresentsInt(s):
    try:
        int(s)
        return True
    except:
        return False

number_list = []
index_list = []

for i in range(100):
    buffer = input()
    number_list.append(buffer)


for i in range(100):

    if RepresentsInt(number_list[i]):
        if int(number_list[i]) <= 10:
            index_list.append(i)
    else:
        if float(number_list[i]) <= 10:
            index_list.append(i)

for i in index_list:
    print("A[{}] = {}".format(int(i), float(number_list[int(i)])))


