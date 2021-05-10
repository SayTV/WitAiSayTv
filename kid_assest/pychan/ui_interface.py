import requests
import urllib.parse

def tell_ui_msg(text,vid): 
    try:
        URL = "http://127.0.0.1:9999/tell/"+urllib.parse.quote('{"text":"'+text+'","vid":"'+vid+'"}')
        PARAMS = {}
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS)
        return True
    except Exception as rs:
        print(rs)
        return False
    # extracting data in json format
#print(tell_ui_msg('hello','1080.mp4'))   #usage example