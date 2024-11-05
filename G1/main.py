
from clouds import Clouds
from map import Map
from pynput import keyboard
import time
#import os
from helicopter import Helicopter as Helico

global helico #����� ����� helico ��� ��������



TICK_SLEEP=0.5 #�������� ����� ������ �����
TRIE_UPDATE=20
FIRE_UPDATE=50
CLOUDS_UPDATE=30
MAP_W,MAP_H=20,20

field = Map(MAP_W,MAP_H)
clouds = Clouds(MAP_W,MAP_H)
helico = Helico(MAP_W,MAP_H)

MOVES={'w':(-1,0),'d':(0,1),'s':(1,0),'a':(0,-1)} # ������� � ������-�����������


# ����� ��� ����� on_press �� �� ����� � ������ None (�� ����)

def on_release(key):
    try:                    #���������� ���� ������ �� ������
        c=key.char.lower() #������� ������ � ������� ������ (�� Unicode-���� � ������� ��������)
    except Exception:
        return
    if c in MOVES.keys():
        dx, dy=MOVES[c][0],MOVES[c][1]
        helico.move(dx,dy)


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=None,on_release=on_release)
listener.start()


tick=1
while True: #������ ����
    #os.system("cls") #��� ������ clear
    print('\n' * 100) 
    field.process_helicopter(helico)
    helico.print_stels()
    field.print_map(helico,clouds)
    print('TICK',tick)
    tick+=1
    time.sleep(TICK_SLEEP)
    if (tick%TRIE_UPDATE==0):
        field.gen_tree()

    if (tick%FIRE_UPDATE==0):
        field.update_fire()

    if (tick%CLOUDS_UPDATE==0):
        clouds.undate()

   
    