from MyFirstModule import hello
#from MyFirstModule import ciao

print('Hello world')
print(globals())
a = "2"
c=12
#globals()['c'] = 12
hello()
print(globals()['c'])
print(locals()['c'])
#ciao()
print(c)
print(globals())

