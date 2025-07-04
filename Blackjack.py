import random

def card_value(card):
    if card.upper() in ['J', 'Q', 'K']:
        return 10
    elif card.upper() == 'A':
        return 'ACE'
    else:
        try:
            return int(card)
        except ValueError:
            print("Invalid card entered. Use numbers or J, Q, K, A. ")
            return 0

def best_ace_value(total_so_far, ace_count):
    total = total_so_far
    for _ in range(ace_count):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

def draw_card():
    """Randomly draw a card from deck"""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def get_player_hand():
    cards = []
    print("\nStarting your hand...")
    while True:
        print(f"Current hand: {cards}")
        choice = input("Do you want to [hit] or [stand]? ").lower()
        if choice == 'stand':
            break
        elif choice == 'hit':
            card = draw_card()
            print(f"You drew: {card}")
            cards.append(card)
            total = calculate_hand_total(cards)
            if total > 21:
                break
        else:
            print("Please type 'hit' or 'stand'.")
    return cards

def calculate_hand_total(cards):
    total = 0
    ace_count = 0
    for card in cards:
        val = card_value(card)
        if val == 'ACE':
            ace_count += 1
        else:
            total += val
    return best_ace_value(total, ace_count)

def dealer_play():
    cards = []
    while True:
        card = draw_card()
        cards.append(card)
        total = calculate_hand_total(cards)
        if total >= 17:
            break
    return cards, total

def check_winner(player_total, dealer_total):
    if player_total > 21:
        return 'Player busts, dealer wins!'
    elif dealer_total > 21:
        return 'Dealer busts, player wins!'
    elif dealer_total > player_total:
        return "Dealer wins!"
    elif player_total > dealer_total:
        return "Player wins!"
    else:
        return "It's a tie!"

def play_blackjack():
    print("🃏 Welcome to Blackjack!\n")
    player_cards = get_player_hand()
    player_total = calculate_hand_total(player_cards)

    print(f"\nYour final hand: {player_cards} → Total: {player_total}")

    if player_total > 21:
        print("You busted! Dealer wins. ")
        return

    print("\nDealer's turn...")
    dealer_cards, dealer_total = dealer_play()
    print(f"Dealer's hand: {dealer_cards} → Total: {dealer_total}")

    result = check_winner(player_total, dealer_total)
    print("\n🎲 Result:", result)

def main():
    while True:
        play_blackjack()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! ")
            break

# Start the game
main()
