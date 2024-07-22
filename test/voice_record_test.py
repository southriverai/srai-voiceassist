import time
import wave
from datetime import datetime

import speech_recognition as sr

if __name__ == "__main__":

    # create a new recognizer instance
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 7000
    recognizer.pause_threshold = 1.0
    with sr.Microphone() as source:
        print("adjusting for ambient noise")
        recognizer.adjust_for_ambient_noise(source)
        print("ambient noise adjusted")
        while True:
            print("Listening!")
            audio = recognizer.listen(source)
            print("Recording done!")
            print(type(audio))
            # write audio to a WAV file
            name_promt = str(time.mktime(datetime.now().timetuple()))[:-2]
            print(name_promt)
            name_file_wave = name_promt + ".wav"
            with wave.open(name_file_wave, "wb") as wav_file:
                wav_file.setnchannels(1)  # mono
                wav_file.setsampwidth(2)  # 2 bytes per sample
                wav_file.setframerate(44100)  # 16 kHz sampling rate
                wav_file.writeframes(audio.get_wav_data())
