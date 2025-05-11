# assistant.py
from utils.speech import listen_command
from utils.speak import speak
from tasks.info import answer_question
from tasks.websearch import search_web

def main():
    speak("Hello! I am your AI assistant.")
    while True:
        command = listen_command().lower()
        if 'exit' in command:
            speak("Goodbye!")
            break
        elif 'search' in command:
            query = command.replace('search', '').strip()
            result = search_web(query)
            speak(result)
        elif 'what is' in command or 'who is' in command or 'tell me' in command:
            answer = answer_question(command)
            speak(answer)
        else:
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
