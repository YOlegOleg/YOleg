import collections



def get_suffix(age):
    if 5<=age<=14 or age%10==0:
        return ' let.'
    elif age%10==1:
        return ' god.'
    else:
        return " goda."

def get_pet(ID):
    
    if ID in pets.keys():
        return pets[ID]
    else:
        False


def create():
    
    neim=input('Klihka=')
    temp={neim:dict()}

    vid=input ('Vid pitomca=')
    age=input('Vozuast=')       
    while age.isdigit()!=True:
        print('Wrong age')
        age=input('Vozuast=')
    age=int(age)
    boss=input('boss=')

    temp[neim]['vid']=vid
    temp[neim]['age']=age
    temp[neim]['boss']=boss
    
    pets[ID+1]=temp
    

    

def read():
    pet=get_pet(ID)
    if not pet:
        print('There is no such pet.')
        return

    for k in pet:
        print('Eto',pet[k]['vid'],end=' ')
        print('po klihke',k,end='. ')
        print('Vozuast:',pet[k]['age'],end='')
        print(get_suffix (pet[k]['age']),end='')
        print(' Vledeet:',pet[k]['boss'])
    
def update():
    pet=get_pet(ID)
    if not pet:
        print('There is no such pet.')
        return

    for kk in pet:
        print('Enter the changes in the fields')
        temp={}
        print ('Changes for the pet:',kk)

        for k, v in pet[kk].items():
            res = input(f"{k}: ")
            if res:
                temp[k] = int(res) if res.isnumeric() else res

        pet[kk].update(temp)

def delete():
    pet=get_pet(ID)
    if not pet:
        print('There is no such pet.')
        return

    pets.pop(ID, None)

def pets_list():
    for k,v in pets.items():
        print (f'ID:{k}',v)



  
pets={}
pet={}



if len(pets)==0:
    print('Introduction of the first pet.')
    ID=0
    create()

print ('Possible commands:','create-1','read-2','update-3','delete-4','list-5','stop-0')
command=int(input ('Enter the command:'))

while command!=0:
    if command==1:
        ID = collections.deque(pets, maxlen=1)[0]
        create()

    elif command==2:
        ID=int(input('Enter the pet ID:'))
        read()
    elif command==3:
        ID=int(input('Enter the pet ID:'))
        update()
    elif command==4:
        ID=int(input('Enter the pet ID:'))
        delete()
    elif command==5:
        pets_list()
    else:
        print('There is no such command')

    command=int(input ('Enter the command:'))
