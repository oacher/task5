maximum = 0
k=0
n=0
x=1
try:
    x = abs(int(input("Введите десятичное целое число, чтобы найти среди его четных цифр максимальную  ")))
except ValueError:
        print("Ошибка")
else:
    if x == 0:
     print("максимальная среди четных цифр введеного числа это 0")
     exit()
    while x != 0:
     n = (x % 10)
     if (n % 2== 0) and (n >= maximum):
            maximum = n
            k+=1
     x = x // 10

if k > 0:
        print("цифра" , maximum , " максимальная среди четных цифр введеного числа")
if  x == 0 and k <= 0:
        print("В введеном числе нет четных цифр")
        

    
 
