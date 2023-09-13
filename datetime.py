#!usr/bin/env python3

#datetime.py
#Anthony Greene
#8/26/22
#Outputs the date and time

#imports datetime
import datetime

#creates a funciton that asks for the input form user
def iput():
    prompt = input("Please enter the date and time in (ex. August 25, 2022 1:00 PM): ")
    #creates a list that seperates objects in list
    sep = prompt.split()
    return sep

#creates a function that formats the list sep, taking away punctuation
def format(date):
    #removes the comma and colon in list
    date[1]= date[1].replace(",", "")
    lst = [x if x.isalnum() else x.split(":") for x in date]
    lst.insert(4, lst[3][0])
    lst.insert(5,lst[3][1])
    del lst[3]
    return lst 

#creates a funciton that gets the month number
def month_number(mnth):
    month_list = ["", "January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    num = month_list.index(mnth)
    return num

#creates a function that formats the time to military time
def mili_time(ap, time):
    time = int(time)
    if ap.upper() == "PM" and not(time >= 12):
        time += 12
    elif ap.upper() == "AM" and time == 12:
        time = 0
    return time

#creatse a main function 
def main():
    #runs functions iput() and format()
    response = iput()
    lst1 = format(response)

    #gets month number and military time, sets date to run datetime
    mth = lst1[0]
    m_num = month_number(mth)
    military_time = mili_time(lst1[5], lst1[3])
    date = datetime.datetime(int(lst1[2]), m_num, int(lst1[1]), military_time, int(lst1[4]), 00, 00)

    #gives output with date and time formated in various ways
    print(date.strftime("%Y/%m/%d %H:%M:%S"))
    print(date.strftime("%y/%B/%d %H:%M:%S %p"))
    print(date.strftime("%a, %Y %b %d"))
    print(date.strftime("%A, %Y %B %d"))
    print(date.strftime("Weekday: %w"))
    print(date.strftime("Day of the year: %j"))
    print(date.strftime("Week number of the year: %W"))
   
    #creates variable for day of year
    day_o_year = int(date.strftime("%j"))

    
    lst1[3] = int(date.strftime("%H"))
    lst1[4]= int(date.strftime("%M"))



    new_year = datetime.datetime(int(lst1[2]), 12, 31, 23, 59)
    #states time untill ball drop
    print(new_year -date)





if __name__ == "__main__":
    main()
