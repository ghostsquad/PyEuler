"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime


def main():
    sundays = 0

    # I could redo this using the algorithm here:
    # http://gmmentalgym.blogspot.com/2011/03/day-of-week-for-any-date-revised.html#ndatebasics

    # loop through years 1901-2000
    for year in range(1901, 2001):
        # loop through months 1-12
        for month in range(1, 13):
            d = datetime.date(year, month, 1)
            if d.weekday() == 6:
                sundays += 1

    print('answer: ' + str(sundays))

if __name__ == '__main__':
    main()
