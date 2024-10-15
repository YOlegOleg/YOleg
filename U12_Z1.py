def cmp(x):
    return x%3

temp = input('=').split()
a = list(map(int, temp))
a.sort(key=cmp)
print(a)
