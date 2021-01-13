for i in range(3, -1, -1):
    print(i)

g = 7
num = 10
while True:
    if num < g:
        print('low')
    elif num == g:
        print('true')
        break
    elif num > g:
        print('over')
        break
    num += 1
