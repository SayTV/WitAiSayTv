
import os
import pyowm
import time
import threading
from Wit.speech_to_text import RecognizeSpeech
from tv import run_netflix,run_youtube,run_channel,channels_db
from bot import analyze_sentence
from pychan.ui_interface import tell_ui_msg
from tendo import singleton
from wit import WitError
me = singleton.SingleInstance()
def has_intent(text,job):
    return text.lower().find(job.lower())!=-1

def get_weather_info():
    APIKEY='8a1f612ff7e68702523686d37a8de96b'                  #your API Key here as string
    OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
    Weather=OpenWMap.weather_manager()  # give where you need to see the weather
    Data=Weather.weather_at_place('Amman').to_dict()               # get out data in the mentioned location
    
    cels=float(Data["weather"]["temperature"]["temp"])-273.15,Data["weather"]["detailed_status"]
    return cels
        
def wait_little():
    time.sleep(5)

def print_out(st,vid=''):
    tell_ui_msg(st,vid)
    print(st)
    

def run_wit():
    text =  RecognizeSpeech('myspeech.wav',print_out, 10)
    if(text==None or text==""):
        sent="I didn't understand, can you say that again?"
        print_out(sent)
        speak(sent,True)
    else:
        #print_out("\nYou said: {}".format(text))
        # print_out()
        speak("You said: {}".format(text),False)
        try:
            res=None
            while True:
                try:
                    res=analyze_sentence(text)
                    break
                except:
                    continue

            if res==None:
                sent="I'm sorry I can't do that, maybe try something else?"
                print_out(sent)
                speak(sent,True)
            else:
                category=res['category']
                if category=='weather':
                    t,r=get_weather_info()
                    # print_out(f"its {r}, {t: .2f}c")
                    sent=f'the weather today is {r}, the temp is{t: .2f} celsius'
                    print_out(sent)
                    speak(sent,False)
                    wait_little()
                    run_wit()   
                else: #channel intent
                    if not 'channel' in res:
                        sent="I'm sorry I didn't hear the channel name"
                        print_out(sent)
                        speak(sent,True)
                    else:
                        channel=res['channel'].lower()
                        if channel=='netflix':
                            print('run netflix')
                            #Amr to integrate here
                            if 'show' in res:
                                show=res['show'].lower()
                                movie_name=show
                                run_netflix(movie_name)         
                            else:
                                sent="I'm sorry I didn't hear the show name"
                                print_out(sent)
                                speak(sent,True)
                        elif channel=='youtube':
                            print('run youtube')
                            #Amr to integrate here
                            if 'show' in res:
                                show=res['show'].lower()
                                video_name=show
                                run_youtube(video_name)         
                            else:
                                sent="I'm sorry I didn't hear the show name"
                                print_out(sent)
                                speak(sent,True)
                        elif channel in channels_db:
                            print('run channel')
                            run_channel(channel)
                        else:
                            print("I don't know this channel")
                            sent="I'm sorry I don't know this channel"
                            print_out(sent)
                            speak(sent,True)
        except WitError:
            print("Bad internet connection")
            sent="I think you have a bad internet connection"
            print_out(sent)
            speak(sent,True)
    #os.system('python3 dict.py')
    speak("Enjoy",False)
    print_out('Say \\"TV\\", so I can help you')
    exit()


def speak(msg,run_wit_after):
    tell_ui_msg(msg,"")
    os.system(f'espeak -s150 -ven+f3 "{msg}"')
   
    if(run_wit_after):
        run_wit()

def run_ui(): 
        #is_in_ui=False
    #thread2 = threading.Thread(target=speak, args=('Hello Dad, I\'m here to serve you , tell me what do you need',True))
    #thread2.daemon = 1
    #thread2.start()
    speak('Hello Sir, I\'m here to serve you , tell me what do you need',True)

run_ui()
