

from utils import randbool
from utils import randcell
from utils import randcell2




#0-пусто
#1-лес
#2-река
#3-госпиталь
#4-магазин
#5-огонь
#6-

SYMBOL='.12+4@'
TREE_BONUS=100
UPGREDE_COST=300
LIVEL_COST=300

class Map():

    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.cells=[[0 for i in range(w)] for j in range(h)]
        self.gen_forest(30,100)
        self.gen_river(5)
        self.gen_river(5)
        self.generate_upgrade_shop()
        self.generate_hospitel()
        

    def print_map(self,helico,clouds):
        print('_'*(self.w+2))
        for ri in range(self.h):
            print('|',end="")
            for ci in range(self.w):
                cell=self.cells[ri][ci]
                if (clouds.cells[ri][ci]==1):
                    print('O',end="")
                elif (clouds.cells[ri][ci]==2):
                    print('W',end="")
                elif helico.x==ri and helico.y==ci:
                    print('8',end="")
                elif (cell>=0 and cell<len(SYMBOL)):
                    print (SYMBOL[cell],end="")
            print('|')
        print('-'*(self.w+2))
       
    def check_bouds(self,x,y):
        if (x<0 or y<0 or x>=self.h or y>=self.w):
            return False
        return True    

        #установка рек (=2) l-длина реки
    def gen_river(self,l):
        rc=randcell(self.w,self.h) #первая клетка
        rx, ry=rc[0],rc[1]      # можно заменить 
        self.cells[rx][ry]=2    #self.cells[rc[0]][rc[1]]=2
        while l>0:              #слейдующая клетка реки в цыкле
            rc2=randcell2(rx,ry)
            rx2, ry2=rc2[0],rc2[1]
            if(self.check_bouds(rx2,ry2) and self.cells[rx2][ry2]!=2): #проверкана границы и наличие реки в новой кледки
                self.cells[rx2][ry2]=2
                rx,ry=rx2,ry2
                l-=1

    #устанока леса(=1)
    def gen_forest(self,r,mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r,mxr): #выполняй ести True
                    self.cells[ri][ci]=1
    
    def gen_tree(self): #добавляет дериво в свободное поле
        c=randcell(self.w,self.h)
        cx, cy=c[0],c[1]
        if(self.check_bouds(cx,cy) and self.cells[cx][cy]==0):
            self.cells[cx][cy]=1
     
    def add_fire(self):
        c=randcell(self.w,self.h)
        cx, cy=c[0],c[1]
        if self.cells[cx][cy]==1:
            self.cells[cx][cy]=5
    
    def update_fire(self):
        for ri in range(self.h):
            for ci in range(self.w):
                 if self.cells[ri][ci]==5:
                    self.cells[ri][ci]=0
        for i in range(10):
            self.add_fire()

    def generate_upgrade_shop(self):
         c=randcell(self.w,self.h)
         cx, cy=c[0],c[1]
         self.cells[cx][cy]=4

    def generate_hospitel(self):
         c=randcell(self.w,self.h)
         cx, cy=c[0],c[1]

         if self.cells[cx][cy]!=4:
            self.cells[cx][cy]=3
         else:
            self.generate_hospitel()

    def process_helicopter (self,helico):
        c=self.cells[helico.x][helico.y]
        if (c==2):
            helico.tant=helico.mxtant

        if (c==5 and helico.tant>0):
            helico.tant-=1
            helico.score+=TREE_BONUS
            self.cells[helico.x][helico.y]=1

        if (c==4 and helico.score>=UPGREDE_COST):
            helico.mxtant+=1
            helico.score-=UPGREDE_COST

        if (c==3 and helico.score>=LIVEL_COST):
            helico.lives+=1
            helico.score-=LIVEL_COST





