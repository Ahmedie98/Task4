from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = 'PCr9zrYydGRyjcHM5qkC3FiIMYaltDTIbEKvBiny-myD'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/5ee4c44f-4f34-4239-92cf-b2396c897a43'
# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello everyone in Smart methods', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

