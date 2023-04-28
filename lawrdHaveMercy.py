import keyboard
from pynput.mouse import Button, Controller
mouse=Controller()

print(''' 
___  ___                       _                _    
|  \/  |                      | |              | |   
| .  . | ___  _   _ ___  ___  | |     ___   ___| | __
| |\/| |/ _ \| | | / __|/ _ \ | |    / _ \ / __| |/ /
| |  | | (_) | |_| \__ |  __/ | |___| (_) | (__|   < 
\_|  |_/\___/ \__,_|___/\___| \_____/\___/ \___|_|\_\                                      
                                                     
Made for RustyApple_ on twitch https://www.twitch.tv/rustyapple_\n\n\n\n''')

axis=input("What Axis do you want to Limit? (x, y)\n>").lower()
locks={'x':-1,'y':-1}
if(axis=='x'):
    err=True
    while err:
        try:
            locks['x']=int(input('At pos\n>'))
            err=False
        except:
            err=True
elif(axis=='y'):
    err=True
    while err:
        try:
            locks['y']=int(input('At pos\n>'))
            err=False
        except:
            err=True

print('Press ` to stop the script.')
while(not keyboard.is_pressed('`')):
    a=mouse.position
    newX=a[0]
    newY=a[1]
    if(locks['x']!=-1):
        newX=locks['x']
    if(locks['y']!=-1):
        newY=locks['y']
    mouse.position=(newX,newY)
    continue
