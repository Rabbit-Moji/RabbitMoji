from gtts import gTTS
import os

# Read the content of "moji.txt"
with open("moji.txt", "r") as file:
    text = file.read()

# Convert text to speech
tts = gTTS("Hello users,Welcome to my facebook clone tool")
tts.save("output.mp3")

# Play the generated audio
os.system("mpv output.mp3")


import time

def loading_animation():
    frames = [
        "⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣿⣿⣿⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣷⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            ]

    for frame in frames:
        print(frame)
        time.sleep(0.1)

loading_animation()
print("\n                               Checking update ... ")
print("")
  ⠀⠀⠀⠀⠀⠀⠀⠀  
