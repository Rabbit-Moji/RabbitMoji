from gtts import gTTS
import os

# Text to be spoken
text = "Hello user, welcome to my channel"

# Create a gTTS object
tts = gTTS(text)

# Save the audio file
tts.save("welcome.mp3")

# Play the audio using a Termux command
os.system("termux-media-player play welcome.mp3")
