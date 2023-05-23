from geopy.geocoders import Nominatim
import speech_recognition as sr
import requests
import pyaudio
import pyttsx3


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


x=requests.get('http://127.0.0.1:8000/get/')
d=x.json()
x=requests.get('http://127.0.0.1:8000/getp/')
vi=x.json()



def speak(s) :
    engine.say(s)
    engine.runAndWait()

def take():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,timeout=6,phrase_time_limit=6)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"You said: {query}\n") 
        speak(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")    
        return "None" 
    return query


print("Hello there! I am IIIT Bot designed especially for the institute! How can I help you today? Press:")
speak(f"Hello there! I am Triple IT Bot designed especially for the institute! How can I help you today?")
print("1 - Information about a Person/Place in Institute")
print("2 - Where is this place in Jabalpur?")
print("3 - Where is this place in IIIT Jabalpur?")

uinp=int(input())

if uinp==3:

    n=take()
    n=n.lower()
    
    if n=="central mess":
        latitude = 23.177496404933162
        longitude = 80.0213508131445
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)

    elif n=="vivekananda hostel" :
        latitude = 23.176256939657186
        longitude = 80.01975674355369
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
    
    elif n=="aryabhatta hostel":
        latitude = 23.176618056751103
        longitude = 80.02044576405068
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
    
    elif n=="panini hostel":
        latitude = 23.1750997760246
        longitude = 80.02051839814224
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
    
    elif n=="saraswati hostel":
        latitude = 23.175335972511107
        longitude = 80.02260851129323
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)

if uinp==2:

    n=take()
    n=n.lower()

    address = n

    geolocator = Nominatim(user_agent="geocode")
    location = geolocator.geocode(address)

    latitude = location.latitude
    longitude = location.longitude
    maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)

    print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
    print("Google Maps link: " + maps_link)

if uinp==1:
    
    n=take()
    n=n.lower()
    k=0
    for i in d:
        if i['name'] in n :
            speak(i['name'])
            print(i['name'])
            speak(i['about'])
            print(i['about'])


    for i in vi:
        if i['name'] in n :
            speak(i['name'])
            print(i['name'])
            speak(i['about'])
            print(i['about'])