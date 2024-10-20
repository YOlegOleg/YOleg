class kassa:
    def __init__(self,money):
        self.money = money
        
    def top_up(self,x):
        self.money+=x

    def count_1000(self):
        print (f"There are {self.money//1000} 1000 notes in the cash register")

    def take_away(self,x):
        if (self.money-x)<0:
            print ('There is not enough money')
        else:
            self.money-=x
 
k1=kassa(0)      

com=""


while com!='0':
    print(f"You have {k1.money} in your cash register")
    com=input(f"\n Enter the command:\n 1-top up \n 2-how 1000\n 3-pick up \n 0-exit\n")
    
    if com=='1':
        k1.top_up(int(input('The amount to be replenished=')))
    elif com=='2':
        k1.count_1000()
    elif com=='3':
        k1.take_away(int(input('How much to take away=')))
    
