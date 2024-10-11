def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


n=int(input('='))
f=int(fact(n))
sp=[]

for i in range(f,0,-1):
    sp.append(fact(i))

print(sp)
