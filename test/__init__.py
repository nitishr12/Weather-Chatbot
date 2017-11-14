from weather import Weather
from watson_developer_cloud import ConversationV1
import json
import watson_developer_cloud
from click._compat import raw_input

weather=Weather()
#print(weather.lookup_by_location("Charlotte").condition())

p=weather.lookup_by_location("Charlotte").atmosphere()
print(p['humidity'])
    

conversation = watson_developer_cloud.ConversationV1(
  username = '497b8111-3060-4043-9afb-df0e487e4710',
  password = 'gWfKEGCSWUiu',
  version = '2017-05-26'
)
print("Start entering your messages")

response = conversation.message(
        workspace_id='727a8a5e-1b66-4009-9a5e-b64bd1505f4c',
        message_input={
            'text': "Charlotte"
        }
    )
print (response)
