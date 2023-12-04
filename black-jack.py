def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Decide whether the player should hit or stand in a Blackjack game."""
    
    # Strategy: If the player has a soft hand (an Ace being counted as 11), be more conservative.
    # If the player has a hard hand, be more aggressive.

    # Soft hand: A hand where an Ace is being counted as 11.
    is_soft_hand = player_low_aces > 0 or (player_high_aces > 0 and player_total <= 11)

    # If the player has a soft hand, be more conservative
    if is_soft_hand:
        if player_total < 18:
            return True
        elif player_total == 18 and dealer_total in [9, 10, 11]:
            return True
        else:
            return False
    # If the player has a hard hand, be more aggressive
    else:
        if player_total <= 11:
            return True
        elif player_total == 12 and dealer_total in [2, 3, 7, 8, 9, 10, 11]:
            return True
        elif 13 <= player_total <= 16 and dealer_total in [7, 8, 9, 10, 11]:
            return True
        else:
            return False
