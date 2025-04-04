from robot_hat import TTS
import time

# Initialize the Text-to-Speech object
tts = TTS()

# Say a phrase
tts.say("Hello, Roka. The Robot HAT is ready.")

# Wait a bit so it doesn't exit immediately
time.sleep(2)

# You can say more phrases
tts.say("Let me know what you want me to do next.")
