name = input()
salary = float(input())
total_sales = float(input())


salary += total_sales * 0.15

print('TOTAL = R$ {}'.format(format(salary, "0.2f")))
