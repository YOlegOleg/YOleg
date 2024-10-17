my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
def pri(x=0):
    if x==n:
        print('End of the list')
        return
    print (my_list[x])
    pri(x+1)

n=len(my_list)
pri()
