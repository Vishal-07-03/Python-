#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


#casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


#center()
txt = "banana"
x = txt.center(20)
print(x)


#count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


#encode()
txt = "My name is Ståle"
x = txt.encode()
print(x)


#expandtabs()
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)


#format()
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


#index()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


#isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)


#isdecimal()
txt = "\u0033" 
x = txt.isdecimal()
print(x)


#islower()
txt = "hello world!"
x = txt.islower()
print(x)


#isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


#istitle()
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)


#partition()
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)


#rindex()
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)


#rsplit()
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)


#rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


#swapcase()
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)


#translate()
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


#zfill()
txt = "50"
x = txt.zfill(10)
print(x)
