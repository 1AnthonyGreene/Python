#!usr/bin/env python3

from math import floor
from math import ceil

credit = float(input("Enter credit card tips amount: "))
cash = float(input("Enter cash tips amount: "))


diner = 0
lst = []
x = input("\nEnter diner tips, seperating each with a space: ")
x = x.split(" ")


for i in range(len(x)):
    diner += (float(x[i]))

print ("\n\n")


total = floor(credit + cash)
print ("\n 3. Your total tips is: $" +str(total))

bar = floor(total * .1)
print("\n 4. The tips for bar is: $" + str(bar))

total -= bar

print ("\n 5. Total after bar: $" + str(total))

urdiner = round(diner * .6)
othrdiner= int(diner - urdiner)

print ("\n 6. Total diner: $" + str(ceil(diner)))

print ("\n 7. Tips for sushi chef: $" + str(othrdiner))
print ("\n 8. Your sushi/diner tips: $" + str(urdiner))


teppan = round(total - diner)
print ("\n 9. Teppan tips left: $" + str(teppan))
urteppan = round(teppan * .55)
othrteppan = int(teppan - urteppan)

print ("\n 10. Your teppan tips: $" + str(urteppan))
print ("\n 11. Tips for the chefs: $" + str(othrteppan))

print("\n 12.Tips you give to bar: $" + str(bar + othrdiner))

print ("\n 13. The tips you take home: $" + str((urdiner + urteppan)))

print("\n2% for Anthony: $" + str(ceil((urdiner + urteppan) * .02)))
