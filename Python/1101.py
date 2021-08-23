while 1:
    sum = 0
    M, N = input().split(' ')
    M = int(M)
    N = int(N)
    
    if M > N:
        stop = M
        if stop > 0 and N > 0:
            for i in range(N, stop+1):
                sum += i
                print(i, end=' ')
            print('Sum={}'.format(sum))
        else:
            break
    else:
        stop = N
        if stop > 0 and M > 0:
            for i in range(M, stop+1):
                sum += i
                print(i, end=' ')
            print('Sum={}'.format(sum))
        else:
            break
