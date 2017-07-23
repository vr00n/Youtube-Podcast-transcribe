import speech_recognition as sr
import sys

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), sys.argv[1])
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
# recognize speech using Google Speech Recognition

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "seventh-oven-839",
  "private_key_id": "90dd0fc2b2759aefb9c39b4ceac27ec734191578",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDhsxlgN72Bw3Mt\n2Z2UV74OG0a7plOHsEMiUsVn+v+O2aZEnkDRAu01D3BX5VRX2sHbLdk5d0SWRchC\nCfoLOatMLs3u+4mM7A84WDyv5BYAcWEfnAIcaREFBpM03g+lI6W5Kz7KLORi1oug\n/mElD8LxIIhjDiExY08qxwRp1cvDH9MJHAVmi/HNFBth/4f/cmxIjonUiWTilA7w\nkKwbkYpr+gGu6iTD+xq6msQUicjiiS3LTQt07oF5sQcMpay1HYLHL1TVBo1V4boe\nDNgl0n09QaOVXpTqPmf2+38NbYfOLjDnUpYWPoj+or6ydTH1bmB/p9EN9hqR53Y7\nsNErmLPvAgMBAAECggEAW6az9kuMTAaHXiYRhGzBA891wLvBDce461Y7TYcygdrG\nVvUAkx+iHbrgPwEkZ+ywbgXHQTu6gV9i+9Y7UJWhhvU2sQY6DBzL7XB/bFmtyY5B\nB2n9vXW48JaD7qMCLWg1YuU5wTXLpItE9iJ2ZmtpGSvB1p+lQP335wIcO7IS5W/i\nh64u+kx8YT4rFHa+1NwUSKhJC96KX14ncdj+aHbycvc+GFJOcX4uCSSjPOGmI3CB\nG9OasQBxYIqMQYTpKJyLBRBJAaFM0WNZKMHiq7rl43Wxy21dXFxZZQcXNehRQvWM\niGINzzOdf+z6ZXB/RHgS2HCpT2ELmX5BhJEXDCE3iQKBgQD60BFuJjnXSFuOUYWc\nQMjvr5Vydvqk8ETn1V6T7+kQNq0IKNQP4YQJQ+DPjrTJGtVv40Kyh0Pv4/3lzBW7\nD+50xmvK/XprDxSmchM3kW/hi2pVu/gs37o8pb71jJtuG4vwOYKAz6Sq8Aek9xhH\nyhwDD0ukqXz3AeQ5BUW14GSoVQKBgQDmXhGsiMTu1uw0MdQIPbmbfON9McsjRuMc\nI+Cz2v8SWUyeQm3v/JhMSuxHrVl1IDQiwKlZs6QZ0HSbI3Fgb53Qx5BuHDUabh+Y\nl0/ygHVBETiSloZTUtjXVjIFV8US+xawtOgBLbFDun1VyoigvrdE4DCZoSiHZY3f\ninxZJOV/MwKBgHT1S/uChdx3WIKAT37y0wC6b0VmaDE7/dXiMO1ppdQyuvOgHmud\nbTXo2k/Pq0xQYBGB95tK6opWVhKv3b5Sio8X7DJHi6ua57VKYt25y2Nw4NBEDFHY\nrn8Th3336I8q91G5b7rjmVVBAz+RHlhzziY7HroVczm4PxW7+Kr8jdPVAoGAYoDA\nv+yvgI0H7P2Nc4SpM9JAF81N1iS+gc7Ziy5OORNUDqvLBH4WxTCYPcHi6ZE+mcmV\n4FRPC/a1lYyfMyQm8BoVKPAIyOdjvUSeG8xP1uW9MfkJMOHQ9KrXsq8oBoi02BRS\nzAY0sQgyBZgXudwy01Gllltx0AtdkcNOjnOXaj8CgYEA971WWlvtGg9naGussvgE\nsrB9Yvi+ESpkXE42zFiKCDYGNKnd1R/82HlNCuGHTEQYMzj/R+qITeGoQQd+V9Tx\nB1AHhveMmVwLOU1OaFQBzKg+fJrl5okQyJHfl8iZCCXL7HqNu6hMPErVbTBNJ86F\nOt886O6YwZf8jTw8K3T8qv0=\n-----END PRIVATE KEY-----\n",
  "client_email": "speech@seventh-oven-839.iam.gserviceaccount.com",
  "client_id": "117939430899753017320",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/speech%40seventh-oven-839.iam.gserviceaccount.com"
}
"""

# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY"))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech

try:
    print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
