"""
    Steve and Josh are bored and want to play something. They don't want to think too much,
    so they come up with a really simple game. Write a function called winner and figure out who is going to win.

    They are dealt the same number of cards. They both flip the card on the top of their deck. Whoever has a card
    with higher value wins the round and gets one point (if the cards are of the same value, neither of them gets a point).
    After this, the two cards are discarded and they flip another card from the top of their deck. They do this until they have
    no cards left.
    deckSteve and deckJosh are arrays representing their decks. They are filled with cards, represented by a single character.
    The card rank is as follows (from lowest to highest):
"""

def winner(deck_steve, deck_josh):
    #6 kyu

    cards: tuple = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
    steve_score: int = 0
    josh_score: int = 0
    
    for card_z in zip(deck_steve, deck_josh):
        steve = cards.index(card_z[0])
        josh = cards.index(card_z[-1])
        if steve > josh: steve_score += 1
        elif josh > steve: josh_score += 1
    if steve_score > josh_score: return "Steve wins {} to {}".format(steve_score, josh_score)
    elif josh_score > steve_score: return "Josh wins {} to {}".format(josh_score, steve_score)
    else: return "Tie"