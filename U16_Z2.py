class turtle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_down(self):
        self.y-=self.s

    def go_up(self):
        self.y+=self.s

    def go_left(self):
        self.x-=self.s

    def go_right(self):
        self.x+=self.s

    def evolve(self):
        self.s+=1

    def degrade(self):
        if (self.s)-1<=0:
            print ('Step <=0')
        else:
            self.s-=1

    def count_moves(self,x2,y2):
        h_x=-1*(abs(self.x-x2))//self.s*-1
        h_y=-1*(abs(self.y-y2))//self.s*-1
        print(f"moves= {h_x+h_y} steps")
       
 
tur1=turtle(0,0,1)      

com=""

while com!='0':
    print(f"The turtle is {tur1.x}, {tur1.y} step {tur1.s}")
    com=input(f"""\n Enter the command:\n 1-down\n 2-up\n 3-left\n 4-right
 5-step+1\n 6-step-1\n 7-count_moves \n 0-exit\n:""")
    
    if com=='1':
        tur1.go_down()
    elif com=='2':
        tur1.go_up()
    elif com=='3':
        tur1.go_left()
    elif com=='4':
        tur1.go_right()
    elif com=='5':
        tur1.evolve()
    elif com=='6':
        tur1.degrade()
    elif com=='7':
        tur1.count_moves(int(input('x2=')),int(input('y2=')))
