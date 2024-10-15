n=int(input('Number of employees='))

sph = []
hs = []

for i in range(n):
    temp = input(f"nter the rate and time separated by the space of employee No. {i+1} =").split()
    int_temp=list(map(int, temp))
    
    sph.append(int_temp[0])
    hs.append(int_temp[1])

res=[]
for i in range(n):
    r=sph[i]*hs[i]
    res.append(r)

res.sort()
print([res])
