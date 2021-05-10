import sys
from wit import Wit


def analyze_sentence(sentence:str):
    access_token = 'FHY5QEOUGT5MBCO2OWZDDDQSRI26NXK4'
    print("=================================================sentence to wit: "+sentence)
    client = Wit(access_token=access_token)
    if not sentence or sentence =="":
        return None
    resp=client.message(sentence)
    print("=====================response: "+str(resp)) 
    intents=resp["intents"]
    if not intents or len(intents)==0:
        return None
    intent=intents[0]
    result={}
    confidence=intent["confidence"]
    if confidence < 0.5:
        return None
    
    entities=resp["entities"]
    intent_name=intent["name"]
    
    if 'channel:channel' in entities:
        channel_entity=entities['channel:channel']
        channel_name=None
        if 'value' in channel_entity[0]:
            channel_name=channel_entity[0]["value"]
        else:
            channel_name=channel_entity[0]["body"]
        result["channel"]=channel_name

    if 'show:show' in entities:
        show_entity=entities['show:show']
        show_name=None
        if 'value' in show_entity[0]:
            show_name=show_entity[0]["value"]
        else:
            show_name=show_entity[0]["body"]
        result["show"]=show_name

    if "wit$creative_work:creative_work" in entities:
        creative_show_entity=entities["wit$creative_work:creative_work"]
        craetive_show_name=None
        if 'value' in creative_show_entity[0]:
            craetive_show_name=creative_show_entity[0]["value"]
        else:
            craetive_show_name=creative_show_entity[0]["body"]

        result["show"]=craetive_show_name
    if 'show' in result and not 'channel' in result:
        result["channel"]='neflix'

    result["category"]=intent_name if intent_name !='wit$get_weather' else 'weather'
    return result

if __name__=="__main__":
    res=analyze_sentence("open facebook watch")
    print(res)