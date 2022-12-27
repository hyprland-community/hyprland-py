l = []

for i in range(10):
    l.append((print,i))

for t in l:
    t[0](t[1])