import time

f = open('today.txt', 'w')
n = time.time()
f.write(time.ctime(n))
f.close()
f = open('today.txt')
print(f.read())
f.close()
