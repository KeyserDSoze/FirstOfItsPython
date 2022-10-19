from random import randint

#globals()['c'] = 10
c = 6

def hello():
    b = randint(0,1)
    #print(a)
    print(b)
    global c
    if b == 1:
        c=3
        print("E' uno")
    else:
        c=4
        print("non e' uno")
    print(c)

def ciao():
    return True

print(c)