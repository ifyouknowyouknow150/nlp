
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import os


# Function for Text to Speech
def tts():
    text = input("Enter the text: ")
    lang = "en"
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("output.mp3")
    print("Playing the converted text...")
    os.system("start output.mp3")  # Use 'start' for Windows, 'open' for macOS, or 'mpg321' for Linux


# Function for Speech to Text from a File (Audio File)
def att():
    file = "moon.wav"  # Make sure this file exists in your directory or change the path to your audio file
    s = sr.Recognizer()
    try:
        with sr.AudioFile(file) as source:
            audio_data = s.record(source)
            text = s.recognize_google(audio_data)
            print("Text from audio file: ", text)
    except FileNotFoundError:
        print("The specified audio file does not exist.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


# Main Menu Loop
while True:
    print("\nMENU:")
    print("Press 1 for Text to Speech")
    print("Press 2 for Speech to Text from File")
    print("Press 3 for Exit")

    # Get user choice
    choice = input("\nEnter your choice (1, 2, or 3): ")

    # Text to Speech
    if choice == '1':
        tts()

    # Speech to Text from an Audio File
    elif choice == '2':
        att()

    # Exit the program
    elif choice == '3':
        print("\nExiting program. Goodbye!")
        break

    # Invalid Input Handling
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n______________________________\n")



