d={}
import collections
d=dict(collections.Counter('Mississippi'))
sv= {k: v for k, v in sorted(d.items(), key = lambda v: v[1], reverse=True)}
for key, value in sv.items():
    print(key, '=', value)
