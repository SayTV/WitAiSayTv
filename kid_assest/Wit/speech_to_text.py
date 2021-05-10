import speech_recognition as sr
import os
def RecognizeSpeech(AUDIO_FILENAME,PRINT_OUTPUT, num_seconds = 5):

    r = sr.Recognizer()
    speech = sr.Microphone()
    with speech as source:
        PRINT_OUTPUT("What do you want to do?")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        PRINT_OUTPUT("I'm listening...")
    try:
        PRINT_OUTPUT("Processing command...")
        # recog = r.recognize_wit(audio, key = "YTF3ZVJYYYQC6PPKJ4FJIHCKGTP4HUKY")
        recog = r.recognize_wit(audio, key = "FHY5QEOUGT5MBCO2OWZDDDQSRI26NXK4")
        #PRINT_OUTPUT("your order is " + recog)
        return recog
    except sr.UnknownValueError:
        PRINT_OUTPUT("could not understand audio")
        return None
    except sr.RequestError as e:
        PRINT_OUTPUT("Could not request results , {0}".format(e))
        return None

    except:
            return None