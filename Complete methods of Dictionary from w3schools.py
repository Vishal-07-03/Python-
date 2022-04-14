car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print("clear(): \n", car)



car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.copy()
print("copy(): \n", x)



x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print("fromkeys(): \n", thisdict)



car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("model")

print("get(): \n", x)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()

print("items(): \n", x)



car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()

print("keys(): \n", x)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")

print("pop(): \n", car)



car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()

print("popitem(): \n", car)



car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("model", "Bronco")

print("setdefault(): \n", x)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})

print("update(): \n", car)



car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()

print("values(): \n", x)
