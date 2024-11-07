
import os
from clouds import Clouds
from map import Map
from pynput import keyboard
import time
import json

from helicopter import Helicopter as Helico

global helico #чтобы обект helico был доступен



TICK_SLEEP=0.2 #задержка перед сменой кадра
TRIE_UPDATE=20
FIRE_UPDATE=50
CLOUDS_UPDATE=75
MAP_W,MAP_H=30,15
tick=1

field = Map(MAP_W,MAP_H)
clouds = Clouds(MAP_W,MAP_H)
helico = Helico(MAP_W,MAP_H)

MOVES={'w':(-1,0),'d':(0,1),'s':(1,0),'a':(0,-1)} # славарь с симвал-направление


# Сдесь был метод on_press он не нужен и уазали None (см ниже)

def on_release(key):
    global helico,clouds,tick, field #чтобы обекты были доступен

    try:                    #исключения если нажали не символ
        c=key.char.lower() #нажатый симвал в удобный формат (из Unicode-кода и внижний регистор)
    except Exception:
        return
    if c in MOVES.keys():
        dx, dy=MOVES[c][0],MOVES[c][1]
        helico.move(dx,dy)
    # сохранение
    elif c == 'f':
        data={'helico':helico.export_data(),
              'clouds':clouds.export_data(),
              'field':field.export_data(),
              'tick':tick}
        with open('level.jesn','w') as lvl: #with gзволяет работать с файлам только в нури with выходим из него файл закрывается
            json.dump(data,lvl)
          
    # востановление
    elif c == 'g':
        with open('level.jesn','r') as lvl:
            data=json.load(lvl)
            tick=data['tick'] or 1
            helico.inport_data(data['helico'])
            field.inport_data(data['field'])
            clouds.inport_data(data['clouds'])


listener = keyboard.Listener(on_press=None,on_release=on_release)
listener.start()


while True: #вечный цикл
    os.system("cls") #для линекс clear
    #print('\n' * 100) 
    field.process_helicopter(helico,clouds)
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

   
    