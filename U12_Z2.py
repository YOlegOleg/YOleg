temp = input('The list is separated by a space:').split()
a = list(map(int, temp))
print ('Array:',a)
a.sort()
n=1
l=len(a)

for i in range(l-1):
      if a[i]!=a[i+1]:
        n+=1

print('The array is sorted',a)
print('The number of different elements:',n)
