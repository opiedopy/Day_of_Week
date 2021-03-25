"""Day of Week (DOW) Calculation (Years 1753 to 9999) - (credits at bottom, www.fuzzywidget.com)
__________________________________________________
Day of Week (DOW) = a + b + c + d + e = Base Formula, for any year
(DOW is a number from 0 to 6, (Base Formula)m7)
Where
a = month #, from the table (table 1)
b = (DOM, Day of month)m7
c = First 2 digits of the year (century #),from table (table 2)
d = (Y)m7 where Y is last 2 digits of year
e = (Y)/4, use the whole number)m7
DOW is the result of adding these numbers, m7, and using table 3.
(where "m7" indicates "modulo 7" and
          that means divide by 7 and just use the remainder)

Table 1
Non Leap   Jan Feb Mar Apr May Jun Jul Aug Sept Oct Nov Dec
Year        6   2   2   5   0   3   5   1   4    6   2   4
Leap
Year        5   1    otherwise, the same for Mar thru Dec


Table 2
            Century divisible by  1st Following  2nd Following  3rd Following
                    400               Century      Century       Century 
                     0                  5            3              1

Example: 16XX = 0, 17XX = 5, 18XX = 3, 19XX = 1,  20XX = 0, 21XX = 5, 22XX = 3,
     23XX = 1, 24XX = 0, 25XX = 5, 26XX = 3, 27XX = 1 and so on....forever
     
Table 3    
    Sun Mon Tue Wed Thu Fri Sat  (Sunday can be 0 or 7)
      0  1   2   3   4   5   6
"""
# input date
out_of_range = 0
m = int(input("Month 1 to 12?  "))
if m>12:
    out_of_range = 1
    
day = int(input("Day 1 to 31? "))
if day>31:
    out_of_range = 1
if day>30 and (m==9 or m==4 or m==6 or 11):
    out_of_range = 1
if day>29 and m==2:
    out_of_range = 1
    
y = int(input ("Year (XXXX format) ? "))
if y<1753 or y>9999:
    out_of_range = 1
    
#find last 2 digits of year, modulo 7
last3digitsofyear = (y%1000)
last2digitsofyear = (last3digitsofyear%100)
d = last2digitsofyear%7 #modulo 7

#find last 2 digits of year/4, modulo 7
e = int((last2digitsofyear/4)%7)

#find day of month, modulo 7
b = (day%7)
    
#determine leap year, returns leap = 1
leap = 0
y_m = (y%4)
y_m_400 = (y%400)
y_m_100 = (y%100)
if ((y_m_400 != 0) and (y_m_100 == 0)):
    leap = 0     #("year is not a leap year.")
    
elif y_m == 0:
    leap = 1     #("year is a leap year.")
   
else:
    leap = 0     #("year is not a leap year.")
    
#Month number program, adj for leap year, table 1
m_num = 0
if out_of_range == 0: 
    if leap == 1 and m == 1:
        m_num = 5
    elif leap == 1 and m == 2:
        m_num = 1
    else:
        monthnumlist = (6,2,2,5,0,3,5,1,4,6,2,4)
        m_num = (monthnumlist[m-1])
a = m_num

#century calc, table 2
century = y - y_m_100
century_xx_m4 = int((century/100)%4)
centurylist = (0,5,3,1)   
century_num = (centurylist[century_xx_m4])
c = century_num

# DOW number
dow_nu = a+b+c+d+e
dow_num = dow_nu%7

#check for out of range
if m==2 and day==29 and leap==0:
    print("Invalid data since no February 29th that year")
elif out_of_range == 1:
    print ("data out of range, correct the date or use year  >1752 or <9999")
else:
    dowlist = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
           "Friday", "Saturday", "Sunday")
#convert day of week # to string name and print answer - Table 3
    print ("DOW = ",dowlist[dow_num])

#Individual Data Results that produce DOW
    print(" ")
    print("The following is the data that was used to find DOW: ")
    print(" The goal is to do all this in your head.  It is possible. I can do it.")
    print ("a = month #, from table 1                  ",a)
    print ("b = (DOM, Day of month)m7                  ",b)
    print ("c = year (century #),from table 2          ",c)
    print ("d = (Y)m7 where Y is last 2 digits of year ",d)
    print ("e = (Y)/4, whole number)m7                 ",e)
    print ("Sum of a+b+c+d+e = ",dow_nu)
    print (dow_nu,"modulo 7 = ", dow_num)
    if m>12 or day>31 or y<1753 or y>9999:
        print ("Date may be wrong because, out of range")
    print("Sun Mon Tue Wed Thu Fri Sat")
    print(" 0   1   2   3   4   5   6")

""" REFERENCE
CRC Standard Mathematical Tables and Formulae, 30th Edition , CRC Press, 1996
Page 738, 10.2.2 "Day of Week Given any Day"
The formula that I term the "base" formula above was modified from the formula given in the above reference.
My modifications were made to make it easier to understand. I made my own tables from calculations from my
modifications and methods. I referred nowhere else, either by text, book, or internet. The CRC method uses a
complex formula for the month and century and then does the modulo 7 calculation. CRC also uses the previous year
method for Jan and Feb, a method that confused me so I re-did that part to make it easier, so this program is unique.
There are other formulae given on the Internet, such as those under DOW in Wikipedia. I did not study those sources since I
had already learned my method. I believe my method is the easiest to memorize and quite innovative. Again, the
only credit I owe is to the CRC reference book above.
NOTE: This DOW method gives results that agree with all other methods on the internet for
Gregorian dates. Gregorian is what the USA and almost all nations use.The Julian Calendar was replaced, in the USA in 1752,
by the Gregorian Calendar, changing the formula for calculating leap years. The beginning of the legal new year
was moved from March 25 to January 1.  11 days were dropped from the month of September 1752.
Also, beware of something called the “Revised Julian Date” method. That method is rare and agrees with Gregorian only until the
year 2800, but Wikipedia Experts will disagree on dates after 2800.  I found one source that said that in the distant
future, a whole day may need to be added, thereby, making this program inaccurate in a couple of thousand years. :-)
And a different method was used by many countries prior to 1752, so this program does not work <1753.
Note: All rights reserved. May not be copied or distributed or modified for profit.

Refer to CRC book if you want to write your own program due to any inspiration found here.
Send any comments to email address on www.fuzzywidget.com home page.
Leap Year:
To use table 1, and if your month is January or February, you must memorize
the rules for all LEAP YEARS!!
Except for case below, if a year is divisible by 4 it is a leap year:
Examples: 1952, 2016, 2020, 2024, 2096, 2548 are all leap years since they
are divisible by 4.
- A year divisible by 100, but not 400, is not a leap year, so
1900, 2100, 2200, 2300, 2700 are not leap years since they are
divisible by 100 but not 400. 1600 and 2000 and 2400 are leap years.
"""
