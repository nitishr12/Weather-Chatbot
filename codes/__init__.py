from watson_developer_cloud import ConversationV1
from weather import Weather
import requests
import json
import watson_developer_cloud
from click._compat import raw_input
from scipy import integer

def conv(conversation,type,flag,place):
    message=raw_input()
    response = conversation.message(
        workspace_id='727a8a5e-1b66-4009-9a5e-b64bd1505f4c',
        message_input={
            'text': message
        }
    )
    stopFlag=flag
    
    #print(type)
    if len(response["intents"])>0:
        if response["intents"][0]["intent"].__eq__("weather_plain"):
            weather = Weather()
            type="temp"
            send_url = 'http://freegeoip.net/json'
            r = requests.get(send_url)
            j = json.loads(r.text)
            print('The weather at '+j['city']+' is '+weather.lookup_by_location(j['city']).condition()['temp'])
        elif response["intents"][0]["intent"].__eq__("weather_conditions"):
            weather = Weather()
            type="temp"
            if len(response["entities"])>0:
                place=response["entities"][0]["value"]
                print(response["output"]["text"][0]+weather.lookup_by_location(place).condition()['temp'])
            else:
                if place =="":
                    send_url = 'http://freegeoip.net/json'
                    r = requests.get(send_url)
                    j = json.loads(r.text)
                    place=j['city']
                print(response["output"]["text"][0].replace('   ',j['city'])+" "+weather.lookup_by_location(place).condition()['temp'])
            #print (response["entities"][0]["value"])
        elif response["intents"][0]["intent"].__eq__("general"):
            weather = Weather()
            type="general"
            conclusion=""
            if len(response["entities"])>0:
                place=response["entities"][0]["value"]
            else:
                if place =="":
                    send_url = 'http://freegeoip.net/json'
                    r = requests.get(send_url)
                    j = json.loads(r.text)
                    place=j['city']
            if "thunder" in weather.lookup_by_location(place).condition()['text'].lower() or "showers" in weather.lookup_by_location(place).condition()['text'].lower() or "breezy" in weather.lookup_by_location(place).condition()['text'].lower() or "windy" in weather.lookup_by_location(place).condition()['text'].lower() or "cloudy" in weather.lookup_by_location(place).condition()['text'].lower() or "rain" in weather.lookup_by_location(place).condition()['text'].lower() or "snow" in weather.lookup_by_location(place).condition()['text'].lower() or int(weather.lookup_by_location(place).condition()['temp'])<55:
                conclusion="you need to"
            else:
                conclusion="you don't need to"
            print(response["output"]["text"][0].replace('(condition)',weather.lookup_by_location(place).condition()['text']).replace('(place)',place).replace('(result)',conclusion))

        elif response["intents"][0]["intent"].__eq__("title"):
            weather = Weather()
            type="title"
            if len(response["entities"])>0:
                place=response["entities"][0]["value"]
                print(response["output"]["text"][0].replace('(condition)',weather.lookup_by_location(place).condition()['text']))            
            else:
                if place =="":
                    send_url = 'http://freegeoip.net/json'
                    r = requests.get(send_url)
                    j = json.loads(r.text)
                    place=j['city']
                print(response["output"]["text"][0].replace('(condition)',weather.lookup_by_location(place).condition()['text'])+" "+place)
            #print (response["entities"][0]["value"])
        elif response["intents"][0]["intent"].__eq__("humidity"):
            weather = Weather()
            type="humidity"
            if len(response["entities"])>0:
                place=response["entities"][0]["value"]
                print(response["output"]["text"][0]+" "+weather.lookup_by_location(place).atmosphere()['humidity'])
            else:
                if place =="":
                    send_url = 'http://freegeoip.net/json'
                    r = requests.get(send_url)
                    j = json.loads(r.text)
                    place=j['city']
                print(response["output"]["text"][0]+" "+weather.lookup_by_location(place).atmosphere()['humidity'])

            #print (response["entities"][0]["value"])
        elif response["intents"][0]["intent"].__eq__("forecast"):
            weather = Weather()
            type="forecast"
            if len(response["entities"])>0:
                place=response["entities"][0]["value"]
            else:
                if place =="":
                    send_url = 'http://freegeoip.net/json'
                    r = requests.get(send_url)
                    j = json.loads(r.text)
                    place=j['city']
            forecasts=weather.lookup_by_location(place).forecast()
            conditions=''
            for f in forecasts:
                conditions+=(f.text()+',')
            print(response["output"]["text"][0].replace('(forecast)',conditions))
        elif response["intents"][0]["intent"].__eq__("Goodbye"):
            stopFlag=False
            print(response["output"]["text"][0])
        else:
            print(response["output"]["text"][0])
    elif len(response["entities"])>0:
        weather = Weather()
        #print(type)
        if(type=="temp"):
            place=response["entities"][0]["value"]
            print("The weather at "+place+" is "+weather.lookup_by_location(place).condition()['temp'])
        elif(type=="title"):
            place=response["entities"][0]["value"]
            print("It is "+weather.lookup_by_location(place).condition()['text']+" at "+place)
        elif(type=="humidity"):
            place=response["entities"][0]["value"]
            print("The humidity is "+weather.lookup_by_location(place).atmosphere()['humidity']+" at "+place)
        elif(type=="general"):
            place=response["entities"][0]["value"]
            if "thunder" in weather.lookup_by_location(place).condition()['text'].lower() or "showers" in weather.lookup_by_location(place).condition()['text'].lower() or "breezy" in weather.lookup_by_location(place).condition()['text'].lower() or "windy" in weather.lookup_by_location(place).condition()['text'].lower() or "cloudy" in weather.lookup_by_location(place).condition()['text'].lower() or "rain" in weather.lookup_by_location(place).condition()['text'].lower() or "snow" in weather.lookup_by_location(place).condition()['text'].lower() or int(weather.lookup_by_location(place).condition()['temp'])<55:
                conclusion="you need one"
            else:
                conclusion="you don't need one"
            print("It is "+weather.lookup_by_location(place).condition()['text']+" at "+place+", Hence "+conclusion)

        elif(type=="forecast"):
            place=response["entities"][0]["value"]
            forecasts=weather.lookup_by_location(place).forecast()
            conditions=''
            for f in forecasts:
                conditions+=(f.text()+',')
            print("It is going to be "+conditions+" at "+place)
        else:
            print(response["output"]["text"][0])
    else:
            print(response["output"]["text"][0])
    if(stopFlag):
        conv(conversation,type,stopFlag,place)

conversation = watson_developer_cloud.ConversationV1(
  username = '497b8111-3060-4043-9afb-df0e487e4710',
  password = 'gWfKEGCSWUiu',
  version = '2017-05-26'
)
print("Start entering your messages")
conv(conversation,'',True,"")
print("\n*********************An implementation by Nitish and Piyusha****************************")
