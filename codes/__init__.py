from watson_developer_cloud import ConversationV1
from weather import Weather
import json
import watson_developer_cloud
from click._compat import raw_input


def conv(conversation,type,flag):
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
        if response["intents"][0]["intent"].__eq__("weather_conditions") and len(response["entities"])>0:
            weather = Weather()
            type="temp"
            #print (response["entities"][0]["value"])
            print(response["output"]["text"][0]+weather.lookup_by_location(response["entities"][0]["value"]).condition()['temp'])
        elif response["intents"][0]["intent"].__eq__("title") and len(response["entities"])>0:
            weather = Weather()
            type="title"
            #print (response["entities"][0]["value"])
            print(response["output"]["text"][0].replace('(condition)',weather.lookup_by_location(response["entities"][0]["value"]).condition()['text']))
        elif response["intents"][0]["intent"].__eq__("humidity") and len(response["entities"])>0:
            weather = Weather()
            type="humidity"
            #print (response["entities"][0]["value"])
            print(response["output"]["text"][0]+" "+weather.lookup_by_location(response["entities"][0]["value"]).atmosphere()['humidity'])
        elif response["intents"][0]["intent"].__eq__("forecast") and len(response["entities"])>0:
            weather = Weather()
            type="forecast"
            forecasts=weather.lookup_by_location(response["entities"][0]["value"]).forecast()
            conditions=''
            for f in forecasts:
                conditions+=(f.text()+',')
            print(response["output"]["text"][0].replace('(forecast)',conditions))
        elif response["intents"][0]["intent"].__eq__("Goodbye"):
            stopFlag=False
            print(response["output"]["text"][0])
#         elif len(response["entities"])>0:
#             weather = Weather()
#             if(type=="temp"):
#                 print("The weather at "+response["entities"][0]["value"]+" is "+weather.lookup_by_location(response["entities"][0]["value"]).condition()['temp'])
#             elif(type=="title"):
#                 print("It is "+weather.lookup_by_location(response["entities"][0]["value"]).condition()['text']+" at "+response["entities"][0]["value"])
#             elif(type=="forecast"):
#                 forecasts=weather.lookup_by_location(response["entities"][0]["value"]).forecast()
#                 conditions=''
#                 for f in forecasts:
#                     conditions+=(f.text()+',')
#                 print("It is going to be "+conditions+" at "+response["entities"][0]["value"])
#             else:
#                 print(response["output"]["text"][0])
        else:
            print(response["output"]["text"][0])
    elif len(response["entities"])>0:
        weather = Weather()
        #print(type)
        if(type=="temp"):
            print("The weather at "+response["entities"][0]["value"]+" is "+weather.lookup_by_location(response["entities"][0]["value"]).condition()['temp'])
        elif(type=="title"):
            print("It is "+weather.lookup_by_location(response["entities"][0]["value"]).condition()['text']+" at "+response["entities"][0]["value"])
        elif(type=="humidity"):
            print("The humidity is "+weather.lookup_by_location(response["entities"][0]["value"]).atmosphere()['humidity']+" at "+response["entities"][0]["value"])

        elif(type=="forecast"):
            forecasts=weather.lookup_by_location(response["entities"][0]["value"]).forecast()
            conditions=''
            for f in forecasts:
                conditions+=(f.text()+',')
            print("It is going to be "+conditions+" at "+response["entities"][0]["value"])
        else:
            print(response["output"]["text"][0])
    else:
            print(response["output"]["text"][0])
    if(stopFlag):
        conv(conversation,type,stopFlag)

conversation = watson_developer_cloud.ConversationV1(
  username = '497b8111-3060-4043-9afb-df0e487e4710',
  password = 'gWfKEGCSWUiu',
  version = '2017-05-26'
)
print("Start entering your messages")
conv(conversation,'',True)
print("\n*********************An implementation by Nitish and Piyusha****************************")
#response = conversation.list_workspaces()
#print(json.dumps(response, indent=2))
