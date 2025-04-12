import random
from time import sleep

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
minor_arcana = [f"{n} of {suit}" for suit in suits for n in ["Ace"] + list(map(str, range(2,11))) + court]

tarot_deck = major_arcana + minor_arcana

# Card meanings database (simplified)
interpretations = {
    "The Fool": "New beginnings, spontaneity, free spirit",
    "The Magician": "Manifestation, resourcefulness, power",
    "Three of Cups": "Friendship, celebration, community",
    "Death": "Transformation, endings, new beginnings",
    # Add interpretations for all 78 cards here
}

def shufflecards():
    shuffled_deck = tarot_deck.copy()
    random.shuffle(shuffled_deck)

    return shuffled_deck

def draw(shuffled_deck):

    reading_cards = random.sample(shuffled_deck, 3)
    return reading_cards



def guided_reading():
    print("\n\033[1mClose your eyes and focus on your question...\033[0m")
    sleep(3)
    
    # Shuffle animation
    print("\nShuffling the deck...")
    for _ in range(3):
        print("♡♢♧♤" * 5)
        sleep(0.5)
    
    shuffled_deck = shufflecards()
    
    
    reading_cards = draw(shuffled_deck)

    positions = ["Past Influence", "Current Situation", "Future Potential"]
    
    # Interpretation
    print("\n\033[1mYour Reading:\033[0m")
    for card, position in zip(reading_cards, positions):
        print(f"\n{position}: {card}")
        sleep(1)
        print(f"Meaning: {interpretations.get(card, 'Card message being revealed...')}")
        sleep(1)
        print("\n\033[3mWhat images or feelings come to mind when you see this card?\033[0m")
        sleep(2)  # Pause for reflection
    
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
