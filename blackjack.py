# FINISHED PROJECT

#------------------------------------------------#
# Name: Han N.K. Nguyen                          #
# Education: University of California, Davis     #
# Project: Blackjack Game in Python              #
#                                                #
# Date created: April 2018                       #
# Date finished: May 2018                        #
#------------------------------------------------#

# github.com/hanshannon

# Import Python libraries:
import random

# (Global) deck of card:
CARD_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
random.shuffle(CARD_DECK) # Shuffle deck of card

# (Global) Sets of cards of player & dealer
PLAYER_CARDS = []
DEALER_CARDS = []

# First cards of player and dealer & add in hand:
player_card1 = random.choice(CARD_DECK)
PLAYER_CARDS.append(player_card1) # Put in set

dealer_card1 = random.choice(CARD_DECK)
DEALER_CARDS.append(dealer_card1) # Put in set

# Second cards of user and dealer & add in hand
player_card2 = random.choice(CARD_DECK)
PLAYER_CARDS.append(player_card2) # Put in set

dealer_card2 = random.choice(CARD_DECK)
DEALER_CARDS.append(dealer_card2) # Put in set

DEALER_SECRET_CARD = DEALER_CARDS[1] # Hidden card of dealer

# Display all cards of player and one card of dealer:
print("\nPlayer's cards: ", PLAYER_CARDS[0], " ", PLAYER_CARDS[1])
print("Dealer's cards: ", DEALER_CARDS[0], " ", "???")

# WIN-IMMEDIATELY CASES:

# Case 1: If player has blackjack while dealer doesn't:
if ((PLAYER_CARDS == ["A", 10] or PLAYER_CARDS == ["A", "J"] or PLAYER_CARDS == ["A", "Q"] or PLAYER_CARDS == ["A", "K"] or PLAYER_CARDS == [10, "A"] or PLAYER_CARDS == ["J", "A"] or PLAYER_CARDS == ["Q", "A"] or PLAYER_CARDS == ["K", "A"]) and (DEALER_CARDS != ["A", 10] or DEALER_CARDS != ["A", "J"] or DEALER_CARDS != ["A", "Q"] or DEALER_CARDS != ["A", "K"] or DEALER_CARDS != [10, "A"] or DEALER_CARDS != ["J", "A"] or DEALER_CARDS != ["Q", "A"] or DEALER_CARDS != ["K", "A"])):
  print("\nPLAYER WINS!")
  exit()

# Case 2: If dealer has blackjack while player doesn't:
elif ((PLAYER_CARDS != ["A", 10] or PLAYER_CARDS != ["A", "J"] or PLAYER_CARDS != ["A", "Q"] or PLAYER_CARDS != ["A", "K"] or PLAYER_CARDS != [10, "A"] or PLAYER_CARDS != ["J", "A"] or PLAYER_CARDS != ["Q", "A"] or PLAYER_CARDS != ["K", "A"]) and (DEALER_CARDS == ["A", 10] or DEALER_CARDS == ["A", "J"] or DEALER_CARDS == ["A", "Q"] or DEALER_CARDS == ["A", "K"] or DEALER_CARDS == [10, "A"] or DEALER_CARDS == ["J", "A"] or DEALER_CARDS == ["Q", "A"] or DEALER_CARDS == ["K", "A"])):
  print("\nDEALER WINS!")
  print("Dealer's cards: ",  DEALER_CARDS)
  exit()

# Case 3: Both have blackjack
elif ((PLAYER_CARDS == ["A", 10] or PLAYER_CARDS == ["A", "J"] or PLAYER_CARDS == ["A", "Q"] or PLAYER_CARDS == ["A", "K"] or PLAYER_CARDS == [10, "A"] or PLAYER_CARDS == ["J", "A"] or PLAYER_CARDS == ["Q", "A"] or PLAYER_CARDS == ["K", "A"]) and (DEALER_CARDS == ["A", 10] or DEALER_CARDS == ["A", "J"] or DEALER_CARDS == ["A", "Q"] or DEALER_CARDS == ["A", "K"] or DEALER_CARDS == [10, "A"] or DEALER_CARDS == ["J", "A"] or DEALER_CARDS == ["Q", "A"] or DEALER_CARDS == ["K", "A"])):
  print("\nBOTH OF YOU DRAW!")
  exit()

else:

  # Set total counts of cards of player and dealer: 
  player_count = 2
  dealer_count = 2

  # FUNCTION to SET CONDITIONS of POINTS to ACE CARD of PLAYER: 
  def player_ace_condition(card, count, CARDS):
    # Player - Ace conditions:
    if (card == "A" and count < 3 and CARDS != ["A", "A"]): 
      card = 11
    
    elif (card == "A" and count == 3): 
      print("Since you have an Ace card while having 3 cards in total, do you want to make it 1 or 11?")
      ace_choice = input("--> ")
      ace_choice = ace_choice.replace(" ", "")
      ace_choice = int(ace_choice)
      card = ace_choice
    
    elif (card == "A" and count > 3):
      card = 1

    return card

  # Initialize points of player and dealer:
  player_points = 0
  dealer_points = 0

  # FUNCTION to SET CONDITIONS of POINTS to ACE CARD of DEALER: 
  def dealer_ace_condition(card, count, CARDS, dealer_points):
    # Player - Ace conditions:
    if (card == "A" and count < 3 and CARDS != ["A", "A"]): 
      card = 11
    
    elif (card == "A" and count == 3 and dealer_points <= 10):
      card = 11
    
    elif (card == "A" and count == 3 and dealer_points > 10):
      card = 1
    
    elif (card == "A" and count > 3):
      card = 1
    
    elif (CARDS == ["A", "A"]):
      card = 1

    return card

  # FUNCTION to set 10 points to J, Q and K cards:
  def jqk_points(card):
    if (card == "J" or card == "Q" or card == "K"):
      card = 10

    return card

  # Call the function to get points: 
  player_card1 = player_ace_condition(player_card1, player_count, PLAYER_CARDS)
  player_card2 = player_ace_condition(player_card2, player_count, PLAYER_CARDS)
  dealer_card1 = dealer_ace_condition(dealer_card1, dealer_count, DEALER_CARDS, dealer_points)
  dealer_card2 = dealer_ace_condition(dealer_card2, dealer_count, DEALER_CARDS, dealer_points)

  # Set 10 points to J, Q, K of player or dealer
  player_card1 = jqk_points(player_card1)
  player_card2 = jqk_points(player_card2)
  dealer_card1 = jqk_points(dealer_card1)
  dealer_card2 = jqk_points(dealer_card2)

  # Set total points variables: 
  player_points = player_card1 + player_card2
  print ("\nPlayer's points: ", player_points)
  dealer_points = dealer_card1 + dealer_card2

  # Ask player if he/she wants to draw another card
  def player_choice_loop(player_count, player_points, PLAYER_CARDS):
    print("\nPlayer, do you want to draw another card? (YES/NO)")
    player_choice = input("--> ")
    player_choice = player_choice.replace(" ", "") # Truncate any whitespace
    player_choice = player_choice.upper()

    while (player_choice != "YES" and player_choice != "NO"):
      print("Invalid input, please try again!")
      player_choice = input("--> ")

    if (player_choice == "YES"): 
      player_extra = random.choice(CARD_DECK)
      print("You've picked ", player_extra)
      player_count += 1

      player_extra = jqk_points(player_extra)
      player_extra = player_ace_condition(player_extra, player_count, PLAYER_CARDS)

      player_points += player_extra
      print("Your points now: ", player_points)

      if (player_points > 21): 
        print("\nPLAYER LOST!")
        exit()
      else: 
        player_choice_loop(player_count, player_points, PLAYER_CARDS)
    
    return player_points    

  player_points = player_choice_loop(player_count, player_points, PLAYER_CARDS)

  # Display hidden card of dealer after player finished picking
  print("\nDealer's hidden card: ", DEALER_SECRET_CARD)

  # Ask dealer if he/she wants to draw another card
  def dealer_choice_loop(dealer_count, dealer_points, DEALER_CARDS, player_points):

    dealer_choice = ""
    
    if (dealer_points < player_points):
      dealer_choice = "YES"
    else: 
      if (dealer_points == player_points and dealer_points < 18):
        dealer_choice == "YES"
      else:
        dealer_choice = "NO"

    if (dealer_choice == "YES"): 
      dealer_extra = random.choice(CARD_DECK)
      print("\nDealer has picked: ", dealer_extra)
      dealer_count += 1

      dealer_extra = jqk_points(dealer_extra)
      dealer_extra = dealer_ace_condition(dealer_extra, dealer_count, DEALER_CARDS, dealer_points)

      dealer_points += dealer_extra
      
      if (dealer_points > 21): 
        print("\nDEALER LOST!")
        exit()
      else: 
        dealer_choice_loop(dealer_count, dealer_points, DEALER_CARDS, player_points)

    return dealer_points

  dealer_points = dealer_choice_loop(dealer_count, dealer_points, DEALER_CARDS, player_points)

  # Display points of Player and Dealer
  print("\nPlayer's points: ", player_points)
  print("Dealer's points: ", dealer_points)

  # Compare points:
  if ((dealer_points > player_points and dealer_points <= 21 and player_points <= 21) or (dealer_points <= 21 and player_points > 21)):
    print("\nDEALER WON!")
  elif ((dealer_points < player_points and dealer_points <= 21 and player_points < 21) or (dealer_points > 21 and player_points <= 21)):
    print("\nPLAYER WON!")
  elif (dealer_points == player_points and dealer_points <= 21 and player_points <= 21):
    print("\nBOTH OF YOU HAVE A DRAW!")
