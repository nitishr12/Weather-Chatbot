from watson_developer_cloud import ConversationV1
from weather import Weather
import json
import watson_developer_cloud
from click._compat import raw_input

def conv(conversation):
    message=raw_input()
    response = conversation.message(
        workspace_id='727a8a5e-1b66-4009-9a5e-b64bd1505f4c',
        message_input={
            'text': message
        }
    )
    if len(response["intents"])>0:
        if len(response["intents"])>0 & response["intents"][0]["intent"].__eq__("weather_conditions") & len(response["entities"])>0:
            weather = Weather()
            #print (response["entities"][0]["value"])
            print(response["output"]["text"][0]+weather.lookup_by_location(response["entities"][0]["value"]).condition()['temp'])
        elif len(response["entities"])>0:
            weather = Weather()
            print("The weather at "+response["entities"][0]["value"]+" is "+weather.lookup_by_location(response["entities"][0]["value"]).condition()['temp'])
        else:
            print(response["output"]["text"][0])
    elif len(response["entities"])>0:
            weather = Weather()
            print("The weather at "+response["entities"][0]["value"]+" is "+weather.lookup_by_location(response["entities"][0]["value"]).condition()['temp'])
    else:
        print(response["output"]["text"][0])
    conv(conversation)

conversation = watson_developer_cloud.ConversationV1(
  username = '497b8111-3060-4043-9afb-df0e487e4710',
  password = 'gWfKEGCSWUiu',
  version = '2017-05-26'
)
print("Start entering your messages")
conv(conversation)
#response = conversation.list_workspaces()
#print(json.dumps(response, indent=2))
