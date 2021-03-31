import pickle
def stroka(a):
    return list(map(str, input('Введите слова через запятую\n').split(',')))
def same_stroka(a):
    print('Пожалуйста, введите список из', len(a), 'слов')
    c = list(map(str, input('Введите слова через запятую\n').split(',')))
    for i in range(100):
        if (len(c) != len(a)):
            print('Введите', len(a), 'cлов!')
            del c[-len(c):]
            c = list(map(str, input('Введите слова через запятую\n').split(',')))
        else:
            break;
    return c
def conjunction(a,b):
    return dict(zip(a, b))
x=[]
x=stroka(x)
print(x)

b=same_stroka(x)
print(b)

z=conjunction(x,b)
print(z)

f=open('for7.txt','r+')
lines=f.readlines()
f.seek(0)
f.write(str(z))
for line in lines: # write old content after new
    f.write(line)
f.close()
