string = input("Enter Ваш text\n")
i = int(0)
l = int(len(string))
c = 'c'
b='с'
new_string = ""
print ('\n')
for i in range(0, l-1):
     if i != 2:
         new_string = new_string + string[i]
print(new_string)
if c or b in (string):
     print ("There is |C| in Ваш text")
else:
    print ("There is no any |C| in Ваш text")
print("String длина: ",l)