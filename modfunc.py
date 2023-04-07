#modulus

def mod(x,m):
    y = x % m
    return y

xan = int(input('choose x: '))
man = int(input('modulus? '))

print(mod(xan,man))
