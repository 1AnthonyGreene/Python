from math import floor
from os import sep
from tkinter import N

credit = float(input("Enter credit card tips amount: "))
cash = float(input("Enter cash tips amount: "))
diner = float(input ("Enter diner tips amount: "))
print ("\n\n")


total = floor(credit + cash)
print ("Your total tips is: $" +str(total))

bar = floor(total * .1)
print("The tips for bar is: $" + str(bar))

total -= bar

print ("The amount after bar is: $" + str(total))

urdiner = round(diner * .6)
othrdiner= int(diner - urdiner)

print ("Your diner tips are: $" + str(urdiner))
print ("The tips for sushibar are: $" + str(othrdiner))

teppan = round(total - diner)
print ("Your tips after diner is: $" + str(teppan))
urteppan = round(teppan * .55)
othrteppan = int(teppan - urteppan)

print ("Your teppan tips are: $" + str(urteppan))
print ("The tips for the chefs are: $" + str(othrteppan))

print("The amount of tips you give to bar is: $" + str(bar + othrdiner))

print ("The tips you take home is: $" + str((urdiner + urteppan)))