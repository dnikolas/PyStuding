years = [1988, 1989, 1990, 1991, 1992, 1993]
print(years[3])

cheeze = ['edem', 'ros', 'moc']
print(cheeze[1].title())
cheeze[1] = cheeze[1].title()
del cheeze[2]
print(cheeze)

even = [n for n in range(0, 10) if n % 3 == 0]
two = [n for n in range(0, 10) if n % 2 == 0]
cell = [(e,t) for e in even for t in two]
for f1, f2 in cell:
    print(f'{f1} or {f2}')

