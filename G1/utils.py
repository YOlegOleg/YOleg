from random import randint as rand

def randbool(r,mxr): #Вормерует с F или T в заданой верочтности mxr-интервал r-отсечка
    t=rand(0,mxr)
    return (t<=r) #выходит со зечением F или T в зависемости от условия

def randcell(w,h):
    tw=rand(0,w-1)
    th=rand(0,h-1)
    return (th,tw)
#0-наверх 1-направа 2-вниз 3-налево
def randcell2(x,y):
    moves=[(-1,0),(0,1),(1,0),(0,1)] #список возможных перемещений(по х у)
    t=rand(0,3)
    
    dx,dy=moves[t][0],moves[t][1]
    
    return (x+dx,y+dy)


    
