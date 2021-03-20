#Задача 1##
n = int(input("Введите число n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)


#Задача 2##
r = "4729461084"
a = list(r)
sum = 0
for i in range (len (a)):
     sum = sum + i
print('4729461084=',sum)

#Задача 3##
1 метод
a = "пять "
c = a+a+a+a+a
b = c.split()
d = len(b)
print(d)
2 медот
a = "семь "
c = a*7
print(c)
b = c.split()
d = len(b)
print(d)