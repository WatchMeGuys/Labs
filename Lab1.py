X = int(input("Enter your случайное number ") )
Y = int(input("Enter the пограничное number "))
while X == Y :
     print ("Ваши numbers совпадают, type разные numbers. ")
     X = input("Enter your случайное number ")
     Y = input("Enter the пограничное number ")
     if X != Y:
        break
n = 3*Y
if X < Y:
     print ("Your случайное number is меньше than пограничное number.")
     print (X," < ",Y)
elif X > Y and X < n:
     print ("Your случайное number is больше than пограничное number.")
     print (X," > ",Y)
elif X >= n:
     print ("Your случайное number is больше than пограничное number in 3 раза or more.")
     print (X," > ",n)
     print (n," = 3 *", Y)
