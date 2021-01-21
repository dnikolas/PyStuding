import os

ff = os.listdir(r'C:\Temp')
print(ff)

with open('today.txt', 'at') as f:
    f.writelines(ff)
