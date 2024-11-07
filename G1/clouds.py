from utils import randbool


class Clouds():
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.cells=[[0 for i in range(w)] for j in range(h)]
        

    

    def undate(self,r=1,mxr=25,g=1,mxg=10): #g=4,mxg=10 отсечка для грозовых облаков
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r,mxr): #выполняй ести True
                    self.cells[i][j]=1
                    if randbool(g,mxg):
                        self.cells[i][j]=2
                else:
                    self.cells[i][j]=0

    def export_data(self):
	    return {'cells':self.cells}

    def inport_data(self,data):
        self.cells=data['cells'] or  [[0 for i in range(self.w)] for j in range(self.h)]




