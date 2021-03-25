# Day_of_Week
-"""Day of Week (DOW) Calculation (Years 1753 to 9999) - (credits at bottom, www.fuzzywidget.com)
- NOTE:  I am learning python and I selected this project to practice.  While there are existing python libraries and 
- functions that will provide the day of the week for future days in just three or so lines of code, can YOU do the 
- day-of-the-week by only using math and programming?  
- I can make this into a python function as well.   And furthermore, not bragging, but I have committed
- the whole process to memory so that I can be given a date in the range of years 1753 to 9999 and I can tell you the
- date using nothing but thinking.  10 random dates today in 4 minutes, with 2 errors in my math.  I'll get better.
- """ REFERENCE
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
