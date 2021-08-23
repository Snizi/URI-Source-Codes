while 1:
    X = int(input())
    if X == 0:
        break
    else:
        r=""
        for i in range(1, X+1):
            r += str(i)+' '
        print(r[:-1])
