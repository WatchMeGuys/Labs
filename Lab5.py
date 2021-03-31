a=list(map(str,input('Введите слова через запятую\n').split(',')))
print(a)
print('Количество слов ', len(a), '\nПожалуйста, введите второй список из', len(a),'слов')
c=list(map(str,input('Введите слова через запятую\n').split(',')))
for i in range(100):
    if(len(c)!=len(a)):
        print('Введите', len(a),'cлов!')
        del c[-len(c):]
        c = list(map(str, input('Введите слова через запятую\n').split(',')))
    else:
        break;
print(c)
print('Ваш словарь -')
di=dict(zip(a,c))
print(di)

