class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        # list with the days in the month
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # check for leap year
        isLeapYear = self.year%4 == 0 and \
                     (self.year%100 != 0 or self.year%400 == 0)
        if isLeapYear and self.month == 2:
            daysInMonth[2] = 29
            self.day += 1
            if self.day > daysInMonth[self.month]:
                self.day = 1
                self.month += 1
            if self.month == 12 and self.day >= self.month:
                self.day = 1
                self.month = 1
                self.year += 1
            daysInMonth[2] = 28
        else:
            self.day += 1
            if self.day >= daysInMonth[self.month]:
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.day = 1
                    self.month = 1
                    self.year += 1

#test cases
date = Date(12, 31, 2019)
date.go_to_next_day()
print(date)

date = Date(2, 28, 2020)
date.go_to_next_day()
print(date)
