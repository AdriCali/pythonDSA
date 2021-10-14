def numInteiros(a,b,c,d):
    a = int('Digite um número: ')
    b = int('Digite um número: ')
    c = int('Digite um número: ')
    d = int('Digite um número: ')
    if((o<a<1001) and (0<b<1001) and (0<c<1001) and (0<d<1001)):
        print((a**b)+(c**d))
    else:
        return('Operação errada')