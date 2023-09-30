from gtts import gTTS
import os
import time

# Read the content of "moji.txt"
with open("moji.txt", "r") as file:
    text = file.read()

# Convert text to speech
tts = gTTS("Hello users, welcome to my Facebook clone tool")
tts.save("output.mp3")

# Play the generated audio
os.system("mpv output.mp3")

def loading_animation():
    frames = [
        "⠔⠋⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠃⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠘⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠙⠢",
        # Add more frames here if needed
    ]

    for frame in frames:
        os.system("clear")  # Clear the terminal before printing the new frame
        print(frame)
        time.sleep(0.1)

loading_animation()
print("\nChecking for updates...")  # Updated the message for clarity
