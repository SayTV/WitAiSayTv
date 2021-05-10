
import os
import tkinter as tk, threading
import imageio
import subprocess
from PIL import Image, ImageTk
from pocketsphinx import LiveSpeech
from multiprocessing import Process
from CommandsServer import CommandsServer
from pychan.ui_interface import tell_ui_msg
from tendo import singleton
me = singleton.SingleInstance()
server=CommandsServer()

server.run()
## init python channel pychan
pychanp=Process(target=os.system, args=('python3 pychan/pychan.py',))
pychanp.start()
#init UI static server
ui_serv=Process(target=os.system, args=('python3 -m http.server 9997 --directory "/home/pi/kid_assest/ui"',))
ui_serv.start()
##
chromeUI=Process(target=os.system, args=('./run.sh http://localhost:9997/ rubish',))
chromeUI.start()
busy_file='/home/pi/kid_assest/busy1.lg'
os.system('rm -f '+busy_file)

#keywords=['word', 'phrase one', 'something else', 'test', 'etc']
#speech = LiveSpeech(lm=False, keyphrase='help', kws_threshold=1)
speech = LiveSpeech(lm=False, kws='commands.list')

tell_ui_msg('Say \\"TV\\", so I can help you','')

for phrase in speech:
    #print(phrase.probability())
    #print (phrase.segments(detailed=True))
    print("===========")
    max=-999999999
    posPh=""
    for ph in phrase.segments(detailed=True):
        if(max<ph[1]):
            max=ph[1]
            posPh=ph[0]

    print("found is "+posPh)
    print("max is "+str(max))
    print("===========")
    if(max <-1900):
        print("ignored")
        continue
    print("executing")
    k=(phrase.segments(detailed=False))
    # if(posPh.strip()=='help'):
    if(posPh.strip()=='tv' and not os.path.isfile(busy_file)):
       print("call main shell")
       proc = subprocess.Popen(["ps", " -fA | grep Kid.py"], stdout=subprocess.PIPE, shell=True)
       (out, err) = proc.communicate()
       print ("program output:", str(out))
       shellrunning=str(out).find('ffmpeg')!= -1
       print("shell search found?",shellrunning)
       if(shellrunning):
            print('shell is running')
       else:
            #tell_ui_msg('I am calling the TV helper for you','')
            #os.system('python3 Kid.py')
            if(not os.path.isfile('/home/pi/kid_assest/busy1.lg')):
                P=Process(target=os.system, args=('python3 Kid.py',))
                P.start()
       #exit()
        #break
        # run_wit()
    elif (posPh.strip()=='pause' or posPh.strip()=='stop'):
        print('call for stop')
        server.change_cmd("pause")
    elif (posPh.strip()=='play' or posPh.strip()=='start'):
        print('call for play')
        server.change_cmd("play")
    elif (posPh.strip()=='exit' or posPh.strip()=='boring'):
        os.system('rm -f '+busy_file)
        print('call for exit')
        server.change_cmd("exit")

