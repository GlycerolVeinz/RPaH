a = int(input('lengt of a side='))

for i in range(a):
    for j in range(a):
        print([i,j],end=' ')
    print('\n')
print()

for i in range(a):
    for j in range(a):
        if i == j:
            print('1',end=' ')
        elif i+j == a-1:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
print()

for i in range(a):
    for j in range(a):
        if i == j:
            print('1',end='')
        elif i<j:
            print('1',end='')
        else:
            print(' ',end='')
    print()
print()

for i in range(a):
    for j in range(a):
        if (i == 0) or (j == 0):
            print('1',end='')
        elif (i == a-1) or (j == a-1):
            print('1',end='')
        elif i == j:
            print('1',end='')
        elif i+j == a-1:
            print('1',end='')
        else:
            print(' ',end='')
    print()


