import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import time
import wikipedia
import pyjokes
import webbrowser
import requests
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
   engine.say(text)
   engine.runAndWait()

def take_command():
 try:
     with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)

 except:
    pass
 return command

def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = dt.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'go to market' in command:
        talk('sorry, i have headache')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "Open Google".lower() in command:
        talk(f"Opening Google ...")
        webbrowser.open("https://www.google.com")

    elif "what's the weather" in command:
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "0c3a3ef355dd361dfdeafa5274d683d8"
        city = "Kanpur"

        def kelvin_to_celsius_fahrenheit(kelvin):
            celsius = kelvin - 273.15
            fahrenheit = celsius * (9 / 5) + 35
            return celsius, fahrenheit

        url = weather_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        print(f"Temperature in {city}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
        print(f"Temperature in {city} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
        print(f"Humidity in {city}: {humidity}%")
        print(f"General Weather in {city}: {description}")
        print(f"Sun rises  in {city} at {sunrise_time} local time")
        print(f"Sun sets in {city} at {sunset_time} local time")

    elif "send message" in command:
        pywhatkit.sendwhatmsg('+7068684855', 'Hi there! Nice to meet you', 13, 00)

    else:
        talk("Please say that command again")

while True:
  run_alexa()