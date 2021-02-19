# main.py
# Last update: Sep 19, 2020 10:27AM
#---------------------------------------------

# Licensing information: ...updating...



#--------------------------------------------------------------------#
#                           LIBRARY IMPORT                           #
#--------------------------------------------------------------------#

# Alphabetical order

import datetime
import math 
import random
import sys



#--------------------------------------------------------------------#
#                            PUBLIC KEYS                             #
#--------------------------------------------------------------------#

# Normal Expressions: 
l_i_love_you = ["I LOVE YOU", "I LUV YOU", "I LOVE U", "I LUV U", "LUV U",
                "I <3 YOU", "I <3 U", "<3 U", "<3"]
l_i_hate_you = ["I HATE YOU", "HATE YOU", "I HATE U", "HATE U", "I DON'T LOVE YOU", 
                "I DON'T LUV YOU", "I DON'T LOVE U", "I DON'T LUV U", "DON'T LUV U", "I DON'T <3 YOU"]


# Normal Greetings:
l_hello_hi = ["HELLO", "HI", "HELLO THERE", "HI THERE"]
l_hey = ["HEY", "HEY THERE"]
l_howdy = ["HOWDY", "HOWDIE"]

l_good_morning = ["GOOD MORNING", "MORNING", "GUD MORNING", "GUD MORN", "MORN"]
l_good_afternoon = ["GOOD AFTERNOON", "AFTERNOON", "GUD AFTERNOON", "GUD AFTERNUN"]
l_good_evening = ["GOOD EVENING", "EVENING", "GUD EVENING", "GUD EVE"]
l_good_night = ["GOOD NIGHT", "NIGHT", "NITE", "GEE NITE", "GNITE", "G9", 
                "GUD NIGHT", "GUD NITE", "GUD 9"]


# Thank you / Sorry:
l_thank_you = ["THANK YOU", "THANKS", "TKS", "THKS", "THANK U", "THK U", "THANKYOU", "THANKU"]
l_sorry = ["SORRY", "I AM SORRY", "I'M SORRY", "IM SORRY", "SRY", "I AM VERY SORRY", 
            "I'M VERY SORRY", "IM VERY SORRY"]


# Others:
l_bad_words = ["BITCH", "FUCK", "SCREW", "DICK", "WHORE", "SLUT"]


# Time: 



#--------------------------------------------------------------------#
#                     NORMAL GREETINGS FUNCTIONS                     #
#--------------------------------------------------------------------#

# FUNCTION to respond to "Hello"/"Hi": 
def hello_hi(user_input):
    _user_input = user_input.upper() 

    _res_1 = any(c in _user_input for c in l_hello_hi)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_hello_hi)
    _res_2 = any(c in _user_input for c in l_bad_words)
    
    if (_res_1 == True or _res_1_2 == True) and _res_2 == False:
        print("Hi there! Nice to see you!")


# FUNCTION to respond to "Hey": 
def hey(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_hey)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_hey)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("Hey there! What's up?")


# FUNCTION to respond to "Howdy":
def howdy(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_howdy)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_howdy)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("Howdy! What's up?")


# FUNCTION to respond to "Good morning": 
def good_morning(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_good_morning)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_good_morning)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("Good morning! How are you feeling right now?")


# FUNCTION to respond to "Good afternoon":
def good_afternoon(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_good_afternoon)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_good_afternoon)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False:
        print("Good afternoon! How are you feeling right now?")


# FUNCTION to respond to "Good evening": 
def good_evening(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_good_evening)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_good_evening)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("Good evening! How are you feeling right now?")


# FUNCTION to respond to "Good night": 
def good_night(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_good_night)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_good_night)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("Good night! Have a good sleep and sweet dream!")


# FUNCTION to respond to "Thank you": 
def thank_you(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_thank_you)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_thank_you)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("No problem! My pleasure to support you!")


# FUNCTION to respond to "Sorry":
def sorry(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_sorry)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_sorry)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("No worries! You are totally fine!")



#--------------------------------------------------------------------#
#                    NORMAL EXPRESSIONS FUNCTIONS                    #
#--------------------------------------------------------------------#

# FUNCTION to respond to "I love you":
def i_love_you(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_i_love_you)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_i_love_you)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("I love you too!")


# FUNCTION to respond to "I hate you":
def i_hate_you(user_input):
    _user_input = user_input.upper()

    _res_1 = any(c in _user_input for c in l_i_hate_you)
    _res_1_2 = any(_user_input.find(s)>=0 for s in l_i_hate_you)
    _res_2 = any(c in _user_input for c in l_bad_words)

    if (_res_1 == True or _res_1_2 == True) and _res_2 == False: 
        print("I know you love me but you are just being mad...")



#--------------------------------------------------------------------#
#                           OTHER FUNCTIONS                          #
#--------------------------------------------------------------------#

     

#--------------------------------------------------------------------#
#                            BOT EXECUTION                           #
#--------------------------------------------------------------------#

def bot_exe(user_input):

# NORMAL GREETING FUNCTIONS: 
    # Call hello_hi(): 
    hello_hi(user_input)
    # Call hey():
    hey(user_input)
    # Call howdy(): 
    howdy(user_input)
    # Call good_morning():
    good_morning(user_input)
    # Call good_afternoon():
    good_afternoon(user_input)
    # Call good_evening():
    good_evening(user_input)
    # Call good_night():
    good_night(user_input)


# NORMAL GREETING FUNCTIONS: 
    # Call i_love_you():
    i_love_you(user_input)
    # Call i_hate_you():
    i_hate_you(user_input)


#----------------------------------------------#
    if (user_input != "Exit" and user_input != "EXIT" and user_input != "exit"):
        user_input = input("\n--> ")
        # user_input = user_input.replace(" ", "")
        bot_exe(user_input)
    
    else:
        print("BestFriend Bot has been deactivated!")
        pass



#--------------------------------------------------------------------#
#                            MAIN FUNCTION                           #
#--------------------------------------------------------------------#

def main():
    print("Please enter something to activate your BestFriend Bot or type 'Exit' to close the program: ")
    user_input = input("--> ")
    # user_input = user_input.replace(" ", "")

    bot_exe(user_input)



#--------------------------------------------------------------------#
#                           MAIN EXECUTION                           #
#--------------------------------------------------------------------#

main()