
import random
import string
from datetime import datetime
GREETING_KEYWORDS = ["hi", "hello", "hey", "greetings",
                      "good morning", "good afternoon", "good evening"]
GREETING_RESPONSES = [
    "Hello there! How can I help you today?",
    "Hi! Great to see you.",
    "Hey! What's on your mind?",
]

FAREWELL_KEYWORDS = ["bye", "goodbye", "exit", "quit", "see you"]
FAREWELL_RESPONSES = [
    "Goodbye! Have a wonderful day!",
    "See you later, take care!",
    "Bye! Come back anytime.",
]

THANKS_KEYWORDS = ["thank", "thanks", "appreciate"]
THANKS_RESPONSES = [
    "You're very welcome!",
    "Anytime, happy to help!",
    "No problem at all!",
]

JOKE_RESPONSES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the chatbot go to therapy? Too many unresolved queries.",
    "I would tell you a network joke, but it might time out.",
]


def contains_keyword(text, keywords):
    """
    Return True if any keyword appears in `text`.

    Multi-word keywords (e.g. 'good morning') are matched as plain
    substrings. Single-word keywords are matched as whole words only,
    so short words like 'hi' don't accidentally match inside longer
    words like 'this'.
    """
    no_punct = text.translate(str.maketrans("", "", string.punctuation))
    words = no_punct.split()

    for keyword in keywords:
        if " " in keyword:
            if keyword in no_punct:
                return True
        elif keyword in words:
            return True
    return False


def get_response(user_input):
   
    text = user_input.lower().strip()

    if contains_keyword(text, GREETING_KEYWORDS):
        return random.choice(GREETING_RESPONSES)

    elif contains_keyword(text, FAREWELL_KEYWORDS):
        return random.choice(FAREWELL_RESPONSES)

    elif contains_keyword(text, THANKS_KEYWORDS):
        return random.choice(THANKS_RESPONSES)

    elif contains_keyword(text, ["your name", "who are you"]):
        return "I'm RuleBot, a simple rule-based chatbot!"

    elif contains_keyword(text, ["how are you"]):
        return "I'm just a program, but running smoothly! How about you?"

    elif contains_keyword(text, ["help", "what can you do"]):
        return ("I can greet you, tell the time or date, tell a joke, "
                "and answer a few simple questions. Try asking my name, "
                "the time, or say 'joke'!")

    elif contains_keyword(text, ["time"]):
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    elif contains_keyword(text, ["date"]):
        return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."

    elif contains_keyword(text, ["joke"]):
        return random.choice(JOKE_RESPONSES)

    elif contains_keyword(text, ["weather"]):
        return "I can't check live weather, but I hope it's nice outside!"

    else:
        return "I'm not sure I understand. Could you rephrase that?"


def main():
    """Run the chatbot in a continuous loop until the user exits."""
    print("=" * 55)
    print(" RuleBot -- a simple rule-based chatbot")
    print(" Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 55)

    while True:  
        user_input = input("\nYou: ")

        if not user_input.strip():
            print("Bot: Please type something so I can respond!")
            continue

        print(f"Bot: {get_response(user_input)}")

        if contains_keyword(user_input.lower().strip(), FAREWELL_KEYWORDS):
            print("\n(Session ended.)")
            break


if __name__ == "__main__":
    main()