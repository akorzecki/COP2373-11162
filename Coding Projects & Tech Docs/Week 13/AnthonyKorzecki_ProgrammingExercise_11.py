import random


class Deck:
    """
    This class represents a standard 52-card deck of playing cards,
    providing capabilities to initialize, shuffle, and deal cards.

    Attributes:
        cards (list): A list of strings representing the cards currently
        present in the deck.

    Methods:
        __init__(): Initializes a full 52-card deck and shuffles it.
        shuffle(): Re-randomizes the order of remaining cards in the deck.
        deal(): Pops and returns a single card from the top of the deck.
    """

    def __init__(self):
        """
        Initializes the Deck instance by generating all 52 card combinations
        of suits and ranks, then shuffling the resulting list.

        Parameters:
            None

        Variables:
            ranks (list): Strings for card ranks (2-10, Jack, Queen, King, Ace).
            suits (list): Strings for card suits (Clubs, Diamonds, Hearts, Spades).

        Logic:
            1. Define lists of all possible ranks and suits.
            2. Build the cards list combining each rank with each suit.
            3. Call the shuffle method to randomize deck order immediately.

        Return:
            None
        """
        # establishing standard card ranks and suits
        # using standard names so cards print cleanly for the user
        ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        # populating the cards list with all 52 unique combinations
        self.cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]

        # shuffling the deck immediately upon creation
        self.shuffle()

    def shuffle(self):
        """
        Randomizes the order of the cards currently remaining in the deck.

        Parameters:
            None

        Variables:
            None

        Logic:
            1. Use random.shuffle to reorder the deck list in-place.

        Return:
            None
        """
        # using the random module to shuffle the list in place
        random.shuffle(self.cards)

    def deal(self):
        """
        Deals a single card from the top of the deck.

        Parameters:
            None

        Variables:
            None

        Logic:
            1. Check if cards remain in the deck.
            2. Pop and return the last card from the deck list.
            3. Return None if the deck is empty.

        Return:
            str or None: The dealt card string, or None if empty.
        """
        # checking to ensure the deck has cards left before popping
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("Error: The deck is empty.")
            return None


def draw_replacement_cards(current_hand, game_deck):
    """
    This function prompts the user to choose which cards to discard from
    their 5-card hand, validates their selection, and replaces chosen cards
    with fresh draws from the deck.

    Parameters:
        current_hand (list): The list of 5 card strings currently held.
        game_deck (Deck): The active Deck instance used to draw replacements.

    Variables:
        user_input (str): The raw string of indices entered by the user.
        raw_choices (list): List of split string tokens from the user input.
        valid_indices (set): Cleaned zero-based integer indices corresponding
        to cards selected for replacement.
        idx (int): Loop index counter for processing card replacements.

    Logic:
        1. Prompt the user for card positions (1-5) separated by commas/spaces.
        2. If the user presses enter with no input, return the hand unchanged.
        3. Parse the entered values, stripping spaces and commas.
        4. Validate that each entered index is between 1 and 5.
        5. For each valid selection, deal a new card from the deck and swap it
           into the corresponding position in current_hand.
        6. Return the updated hand to the caller.

    Return:
        list: The updated 5-card hand after card replacements.
    """
    # prompting the user to enter the card positions they wish to swap
    # informing them of the format and option to keep all cards
    user_input = input(
        "\nEnter the card numbers to replace (e.g. 1, 3, 5), "
        "or press ENTER to keep all: "
    ).strip()

    # if the user just pressed Enter, they want to hold their entire hand
    if not user_input:
        print("Holding all current cards.")
        return current_hand

    # cleaning and tokenizing user input
    # replacing commas with spaces so split() handles either delimiters smoothly
    cleaned_input = user_input.replace(",", " ")
    raw_choices = cleaned_input.split()

    # set to hold validated zero-based card index positions
    valid_indices = set()

    # iterating through each input token to validate it
    for choice in raw_choices:
        # checking if the token is numeric before converting
        if choice.isdigit():
            card_num = int(choice)
            # validating that the number corresponds to a card in a 5-card hand (1 to 5)
            if 1 <= card_num <= len(current_hand):
                valid_indices.add(card_num - 1)
            else:
                print(
                    f"Warning: {card_num} is out of range (1-5) and will be ignored."
                )
        else:
            print(
                f"Warning: '{choice}' is not a valid number and will be ignored."
            )

    # replacing the selected cards with new cards from the deck
    if valid_indices:
        for idx in sorted(valid_indices):
            new_card = game_deck.deal()
            if new_card:
                print(
                    f"Replacing Card {idx + 1} ({current_hand[idx]}) -> {new_card}"
                )
                current_hand[idx] = new_card
    else:
        print("No valid card numbers entered. Keeping current hand.")

    return current_hand


def play_poker_game():
    """
    This is the main driver function that initializes the deck, deals the
    initial 5-card poker hand, displays the hand, coordinates the draw phase,
    and displays the final hand.

    Parameters:
        None

    Variables:
        poker_deck (Deck): The active Deck object containing shuffled cards.
        hand (list): List containing the 5 cards dealt to the player.
        i (int): Loop index variable used for enumerating cards on screen.
        final_hand (list): The updated hand returned after the draw phase.

    Logic:
        1. Instantiate a new Deck object (shuffled automatically).
        2. Deal 5 cards sequentially into the player's initial hand.
        3. Print welcome banner and display initial hand with numbered labels (1-5).
        4. Pass the hand and deck to draw_replacement_cards() to perform the draw.
        5. Display the final hand with numbered labels (1-5).
        6. Conclude the round.

    Return:
        None
    """
    print("=" * 45)
    print("        WELCOME TO VIDEO POKER (5-CARD DRAW) ")
    print("=" * 45)

    # instantiating the deck object which creates and shuffles 52 cards
    poker_deck = Deck()

    # dealing initial 5-card poker hand
    hand = []
    for _ in range(5):
        hand.append(poker_deck.deal())

    # displaying the dealt hand to the player with 1-based indexing
    print("\nYour Initial Hand:")
    print("-" * 25)
    for i in range(len(hand)):
        print(f"Card {i + 1}: {hand[i]}")

    # executing the draw phase by calling the replacement function
    final_hand = draw_replacement_cards(hand, poker_deck)

    # displaying the final results after the draw phase has completed
    print("\nYour Final Hand:")
    print("-" * 25)
    for i in range(len(final_hand)):
        print(f"Card {i + 1}: {final_hand[i]}")
    print("=" * 45)
    print("Draw complete. Thanks for playing!")


if __name__ == "__main__":
    play_poker_game()
