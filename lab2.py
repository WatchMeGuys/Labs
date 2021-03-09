import random
import math
print("Hello, ab(user)")
print("""乁༼☯‿☯✿༽ㄏ""")
i=0
while i<99:
   print ("""\n___________________________________________________________________________________________________________________________
   1.сложение   2.вычитание   3.умножение   4.деление   5.степень   6.модуль   7.случайное   8.факториал   9.аркос   0.Выход\n""")
   sign = input("Введите числовое обозначение операции: ")
   if sign == '1': #+
     p1 = float(input("Первое число: "))
     p2 = float(input("Второе число: "))
     print (p1, " + ",p2, " = ", p1+p2 )
   elif sign == '2': #-
     s1 = float(input("Уменьшаемое: "))
     s2 = float(input("Уменьшитель: "))
     print (s1, " - ",s2, " = ", s1-s2 )
   elif sign == '3': #*
     m1 = float(input("Умножаемое: "))
     m2 = float(input("Умножатель: "))
     print (m1, " * ",m2, " = ", m1*m2 )
   elif sign == '4': #/
     d1 = float(input("Дивидент: "))
     d2 = float(input("Дивайдер: "))
     print (d1, "/",d2, " = ", d1/d2 )
   elif sign == '5': #degree
     deg1 = float(input("Число: "))
     deg2 = float(input("Степень: "))
     print (deg1, "^",deg2, " = ", pow(deg1,deg2))
   elif sign == '6': #module
     mod = float(input("Число: "))
     print ("|",mod,"| "" = ", abs(mod))
   elif sign == '7': #random
     print ("Границы: ")
     r1 = int(input("Левое: "))
     r2 = int(input("Правое: "))
     print ("Рандом [",r1,";",r2,"] = ",random.uniform(r1, r2))
   elif sign == '8': #factorial
     F = int(input("Число: "))
     print (F,"! = ",math.factorial(F))
   elif sign == '9': # acos
     X = float(input("Дайте число (-1;1): "))
     print("acos(X) = ",math.acos(X), "радиан")
   elif sign=='0':
    break