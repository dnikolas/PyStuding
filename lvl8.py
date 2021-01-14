e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f['walrus'])
f2e = {}
for e, f in e2f.items():
    f2e[f] = e
print(f2e.values())
sqr = {key: key*key for key in range(10)}
print(sqr)
