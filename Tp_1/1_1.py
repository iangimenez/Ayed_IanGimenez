
def nose():
    a=int(input("asdads:  "))
    b=int(input("asdads:  "))
    c=int(input("asdads:  "))
    lis=[a,b,c]
    return lis
def encontrar_maximo(a,b,c):
    if a>b:
        if a>c:
            return a
        elif a==c:
            return -1
    elif b>c:
        return b
    elif b==c:
        return -1
    else:
        return c
lis=nose()
print(f'maximo:  {encontrar_maximo(lis[0],lis[1],lis[2])}')