'''circle'''
def cir():
    '''circle'''
    cenx = float(input())
    ceny = float(input())
    rad = float(input())
    mosx = float(input())
    mosy = float(input())
    if (mosx - cenx)**2 + (mosy - ceny)**2 == rad:
        print('Yes')
    else:
        print('No')
cir()
