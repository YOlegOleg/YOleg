from utils import randbool


class Clouds():
    def __inin__(self,w,h):
        self.w=w
        self.h=h
        self.cells=[[0 for i in range(w)] for j in range(h)]
        

    

    def undate(self,r=2,mxr=10,g=4,mxg=10): #g=4,mxg=10 отсечка для грозовых облаков
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r,mxr): #выполняй ести True
                    self.cells[i][j]=1
                    if randbool(g,mxg):
                        self.cells[i][j]=2
                else:
                    self.cells[i][j]=0


