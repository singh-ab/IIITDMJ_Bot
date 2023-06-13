from geopy.geocoders import Nominatim
import speech_recognition as sr
import requests
import pyaudio
import pyttsx3
import json


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


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

#weather function
def get_weather(place):
    api_key = 'f12d3cc1cc034908b5290617232605'
    base_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

    params = {
        'key': api_key,
        'q': place,
        'format': 'json',
        'num_of_days': 1,
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)

        if 'data' in data:
            current_condition = data['data']['current_condition'][0]
            temperature = current_condition['temp_C']
            weather_desc = current_condition['weatherDesc'][0]['value']
            humidity = current_condition['humidity']
            wind_speed = current_condition['windspeedKmph']

            print(f"Weather in {place}:")
            print(f"Temperature: {temperature}°C")
            print(f"Weather Description: {weather_desc}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")

            speak(f"Weather in {place}:")
            speak(f"Temperature: {temperature}°C")
            speak(f"Weather Description: {weather_desc}")
            speak(f"Humidity: {humidity}%")
            speak(f"Wind Speed: {wind_speed} km/h")
        else:
            print("Unable to retrieve weather information.")
            speak("Unable to retrieve weather information.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


print("Hello there! I am IIIT Bot designed especially for the institute! How can I help you today? Press:")
speak(f"Hello there! I am Triple IT Bot designed especially for the institute! How can I help you today?")
print("1 - Information about a Person/Place in Institute")
print("2 - Where is this place in Jabalpur?")
print("3 - Where is this place in IIIT Jabalpur?")
print("4 - How is the Weather in the city?")

uinp=int(input())

#weather call
if uinp==4:
    n=take()

    place_name = n
    get_weather(place_name)

#iiit jabalpur internal locations
if uinp==3:

    n=take()
    n=n.lower()
    
    if n=="central mess":
        latitude = 23.177496404933162
        longitude = 80.0213508131445
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
        speak("Here is the location on Google Maps")

    elif n=="vivekananda hostel" :
        latitude = 23.176256939657186
        longitude = 80.01975674355369
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
        speak("Here is the location on Google Maps")
    
    elif n=="aryabhatta hostel":
        latitude = 23.176618056751103
        longitude = 80.02044576405068
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
        speak("Here is the location on Google Maps")
    
    elif n=="panini hostel":
        latitude = 23.1750997760246
        longitude = 80.02051839814224
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
        speak("Here is the location on Google Maps")


    elif n=="saraswati hostel":
        latitude = 23.175335972511107
        longitude = 80.02260851129323
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
        speak("Here is the location on Google Maps")


    else:
        print("Location Not Found, Please try again.")
        speak("Location Not Found, Please try again.")


#external locations
if uinp==2:

    n=take()
    n=n.lower()

    address = n

    geolocator = Nominatim(user_agent="geocode")
    location = geolocator.geocode(address)

    if location == None:
        print("Location Not Found, Please try again.")
        speak("Location Not Found, Please try again.")
    else:
        latitude = location.latitude
        longitude = location.longitude
        maps_link = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)

        print("Latitude, Longitude: " + str(latitude) + ", " + str(longitude))
        print("Google Maps link: " + maps_link)
        speak("Here is the location on Google Maps")

#personal info & about college
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
        
    else:
        print("Information Unavailable. Try visiting the official institute website https://www.iiitdmj.ac.in/ ")
        speak("The information you are seeking is unavailable")