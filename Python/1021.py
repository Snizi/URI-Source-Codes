a =  float(input())
n = [100,50,20,10,5,2]
m = [1,0.50,0.25,0.10,0.05,0.01]
print ("NOTAS:")
for x in n:
    qn = int(round(a,2)/x)
    print("{} nota(s) de R$ {:.2f}".format(qn,x))
    a -= qn*x
print ("MOEDAS:")
for y in m:
    qm = int(round(a,2)/y)
    print("{} moeda(s) de R$ {:.2f}".format(qm,y))
    a -= qm*y
