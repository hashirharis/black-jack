# black-jack
In this problem we'll be working with a simplified version of blackjack (aka twenty-one). In this version there is one player (who you'll control) and a dealer.

* The player is dealt two face-up cards.The dealer is dealt one face-up card.
* The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
* The dealer then deals additional cards to himself until either:
  * the sum of the dealer's cards exceeds 21, in which case the player wins the round
  * the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)


This is a basic strategy that takes into account whether the player has a soft hand or a hard hand. It suggests being more conservative when the player has a soft hand and more aggressive when the player has a hard hand. The decisions are based on common Blackjack strategies, but you can adjust the conditions based on your specific preferences or strategy.

```python
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

```
