import random
from time import sleep
from openai import OpenAI
import os

from PIL import Image

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Create full tarot deck (78 cards)
major_arcana = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

suits = ["Wands", "Cups", "Swords", "Pentacles"]
court = ["Page", "Knight", "Queen", "King"]
minor_arcana = [f"{n} of {suit}" for suit in suits for n in ["Ace"] + list(map(str, range(2, 11))) + court]

tarot_deck = major_arcana + minor_arcana

def shufflecards():
    shuffled_deck = tarot_deck.copy()
    random.shuffle(shuffled_deck)
    return shuffled_deck

def draw(shuffled_deck):
    return random.sample(shuffled_deck, 3)

def show_card_image(card):
    filename = f"ASCII/{card}.png"
    if os.path.exists(filename):
        try:
            img = Image.open(filename)
            img.show()
        except Exception as e:
            print(f"Could not display image for {card}: {e}")
    else:
        print(f"[Image for {card} not found at {filename}]")

def get_chatgpt_interpretation(card, position, user_input):
    prompt = (
        f"The user drew the tarot card '{card}' in the position of '{position}'.\n"
        f"Their personal interpretation or feeling was:\n\"{user_input}\"\n"
        f"Now give a poetic and intuitive tarot reading, incorporating their reflection into the message."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a mystical tarot guide offering deep and intuitive interpretations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting interpretation from ChatGPT: {e}"

def guided_reading():
    print("\n\033[1mClose your eyes and focus on your question...\033[0m")
    sleep(3)

    print("\nShuffling the deck...")
    for _ in range(3):
        print("♡♢♧♤" * 5)
        sleep(0.5)

    shuffled_deck = shufflecards()
    reading_cards = draw(shuffled_deck)
    positions = ["Past Influence", "Current Situation", "Future Potential"]

    print("\n\033[1mYour Reading:\033[0m")
    for card, position in zip(reading_cards, positions):
        print(f"\n\033[4m{position}:\033[0m {card}")
        show_card_image(card)
        sleep(1)

        user_input = input(f"\nWhat feelings, thoughts, or symbols stand out to you in '{card}'? ")
        print("\nInterpreting your reflection with the wisdom of the cards...\n")
        sleep(2)

        meaning = get_chatgpt_interpretation(card, position, user_input)
        print(f"\033[3m{meaning}\033[0m")
        sleep(2)

    print("\n\033[1mHow do these messages resonate with your situation? Trust your intuition.\033[0m")

def main():
    print("""
    Welcome to the Digital Tarot Reader
    ------------------------------------
    1. Start Reading
    2. Exit
    """)

    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            guided_reading()
        elif choice == "2":
            print("Thank you for exploring the tarot. May your path be clear!")
            break
        else:
            print("Please choose a valid option")

if __name__ == "__main__":
    main()
