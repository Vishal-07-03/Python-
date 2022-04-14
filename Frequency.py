a="Mississipi"
d={}
for char in set(a):
    d[char]=a.count(char)
sv= {k: v for k, v in sorted(d.items(), key = lambda v: v[1], reverse=True)}
for key, value in sv.items():
    print(key, '=', value)
