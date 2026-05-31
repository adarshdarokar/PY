import os

print("Welcome to RoboSpeaker 1.1 created by Adarsh")

x = input("Enter what you want me to speak: ")

if x == "q":
    print("Bye Bye Friend")
    quit()

command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'

os.system(command)