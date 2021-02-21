# FINISHED PROJECT

#------------------------------------------------#
# Name: Han N.K. Nguyen                          #
# Education: University of California, Davis    `#
# Project: Tower of Hanoi (Walkthrough)          #
#                                                #
# Date created: February, 2018                   #
# Date finished: February , 2018                 #
#------------------------------------------------#

def tower(plates, begin, end, aux):
  if (plates == 1):
    print("Move plate " + begin + " to " + end)
  
  else: 
    tower(plates-1, begin, aux, end)
    print("Move plate from " + begin + " to " + end)
    tower(plates-1, aux, end, begin)

number_of_plates = int(input("How many blocks of tower do you have?\n--> "))

print("\n")
tower(number_of_plates, 'A', 'C', 'B')

# END OF CODE
