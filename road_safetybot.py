import json
import random
import re
from colorama import Fore, Style, init

init(autoreset=True)

with open("road_safety_training.json", "r", encoding="utf-8") as f:
    intents = json.load(f)["intents"]

STOP_WORDS = {
    "i", "me", "you", "can", "please", "help", "on", "about",
    "the", "a", "an", "is", "am", "are", "to", "for", "with",
    "my", "your", "of", "before", "after", "some", "any"
}

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOP_WORDS]
    return tokens

def stem(word):
    for suffix in ["ing", "ed", "s"]:
        if word.endswith(suffix) and len(word) > 4:
            return word[:-len(suffix)]
    return word

def detect_intent(user_input):
    tokens = normalize(user_input)
    stemmed = {stem(t) for t in tokens}

    best_intent = None
    highest_score = 0

    for intent in intents:
        score = 0
        keywords = {stem(k) for k in intent["keywords"]}
        for token in stemmed:
            if token in keywords:
                score += 1

        if score > highest_score:
            highest_score = score
            best_intent = intent

    return best_intent if highest_score > 0 else None

def guideline_help():
    return (
        "Travel Guidelines:\n"
        "- Keep documents secure\n"
        "- Respect local laws\n"
        "- Carry insurance\n"
        "- Stay aware of surroundings"
    )

def travelbot():
    print(Fore.CYAN + Style.BRIGHT + "\nTravelBot | Smart safety Assistant\n")

    while True:
        user_input = input(Fore.YELLOW + "You: ")

        intent = detect_intent(user_input)

        if not intent:
            print(Fore.RED + "TravelBot: I’m not fully sure I understood. Please ask about road safety rules, safety travel advice.")
            continue

        tag = intent["tag"]
        response = random.choice(intent["responses"])
        print(Fore.GREEN + "TravelBot: " + response)

     
        if tag == "guidelines":
            print(Fore.BLUE + guideline_help())

        elif tag == "exit":
            break

travelbot()