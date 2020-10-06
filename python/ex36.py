import math

def is_bissextile(y):
    return ( y % 4 == 0 and y % 100 != 0 ) or ( y % 400 == 0 )

assert is_bissextile(2004)

def number_of_days(year, month):
    """Returns the number of days of the specified month"""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        return 29 if is_bissextile(year) else 28
    else:
        return 30

assert number_of_days(2020, 2) == 29
assert number_of_days(2019, 2) == 28
assert number_of_days(2019, 9) == 30
assert number_of_days(2019, 12) == 31

def is_valid_date(y, m, d):
    return y >= 0 \
        and ( 1 <= m <= 12 ) \
        and ( 1 <= d <= number_of_days(y, m) )

assert is_valid_date(*(2020, 9, 23))
assert not is_valid_date(*(2015, 29, 2))
assert not is_valid_date(*(2015, 2, 29))

"""
# lazy version
def days_between(y, m, d, Y, M, D):
    # calulate number of days from 0000/00/00 to y/m/d
    days1 = sum([366 if is_bissextile(yy) else 365 for yy in range(y)]) \
        + sum([number_of_days(y, mm) for mm in range(1, m)]) + d

    # calulate number of days from 0000/00/00 to Y/M/D
    days2 = sum([366 if is_bissextile(YY) else 365 for YY in range(Y)]) \
        + sum([number_of_days(Y, MM) for MM in range(1, M)]) + D

    # then substract
    return days2 - days1
"""

def days_between(y, m, d, Y, M, D):
    def nb_days_of_year(y):
        return 366 if is_bissextile(y) else 365

    def nb_days_from_new_year(y, m, d):
        return sum([number_of_days(y, mm) for mm in range(1, m)]) + d
    
    def days_between_positive_year(y, m, d, Y, M, D):
        # y must be < or = Y
        return sum([nb_days_of_year(yy) for yy in range(y, Y)]) \
            - nb_days_from_new_year(y, m, d) \
            + nb_days_from_new_year(Y, M, D)

    if y <= Y:
        return days_between_positive_year(y, m, d, Y, M, D)
    else:
        return -days_between_positive_year(Y, M, D, y, m, d)

assert (days_between(1985,10,21, 1985,10,21) == 0)
assert (days_between(1985,10,20, 1985,10,21) == 1)
assert (days_between(1985,10,21, 1985,10,20) == -1)
assert (days_between(1985,10,21, 2017,9,19) == 11656)
assert (days_between(2017,9,19, 1985,10,21) == -11656)
assert (days_between(1999,12, 5, 2000,3,1) == 87)

def weekday(y, m, d):
    days = days_between(1900,1,1, y,m,d)
    return (days+1) % 7

assert weekday(1900,1,1) == 1
assert weekday(1985,10,21) == 1
assert weekday(2017,9,19) == 2
assert weekday(1899,12,31) == 0
assert weekday(1700,1,1) == 5
assert weekday(2019,9,14) == 6

def cal(y, m, weekday=weekday):
    def print_cell(s):
        print('{0: >3}'.format(s), end='')

    months = [
        '  Janvier',
        '  Février',
        '     Mars',
        '    Avril',
        '      Mai',
        '     Juin',
        '  Juillet',
        '     Août',
        'Septembre',
        '  Octobre',
        ' Novembre',
        ' Décembre'
    ]

    print(' '*3, months[m-1], y)
    print(' di lu ma me je ve sa')

    first_day_of_week = weekday(y, m, 1)
    nb_days = number_of_days(y, m)
    current_day = 1
    for y in range(6):
        for x in range(7):
            if (y == 0 and x < first_day_of_week) or current_day > nb_days:
                print_cell('')
            else:
                print_cell(current_day)
                current_day = current_day + 1
        print()

cal(2020,9)

def weekday_delambre(y, m, d):
    def m_bar(m, y):
        m_year_norm = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
        m_year_leap = [3, 6, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
        return (m_year_leap if is_bissextile(y) else m_year_norm)[m-1]

    def y_pp(y):
        return y // 100

    def y_p(y):
        return y % 100

    s = d + m_bar(m, y) + (21 * y_pp(y)) // 4 + (5 * y_p(y)) // 4 + 2
    return s % 7

assert weekday_delambre(1985, 10, 21) == 1
assert weekday_delambre(2020, 9, 29) == 2

cal(2020,9,weekday=weekday_delambre)

APPROX_DAYS_PER_YEAR = 365.2425
def days_between_approx(y,m,d,Y,M,D):
    #return (D + M*APPROX_DAYS_PER_YEAR/12 + Y*APPROX_DAYS_PER_YEAR) - (d + m*APPROX_DAYS_PER_YEAR/12 + y*APPROX_DAYS_PER_YEAR)
    return (D-d) + (M-m)*APPROX_DAYS_PER_YEAR/12 + (Y-y)*APPROX_DAYS_PER_YEAR

def isalmost(n, m, d=1):
	return abs(n - m) <= d

def approxrat(*p):
    ex = days_between(*p)
    ap = days_between_approx(*p)
    return 0 if ex == 0 else ap/ex

assert isalmost(approxrat(1985,10,21,2020,9,19) , 1 , 0.0001)
assert isalmost(approxrat(1800,1,1, 2100,1,1)   , 1 , 0.000005)
print(approxrat(2019,2,28,2019,3,1))


'''
36.10 Effects of approximations onweekday
'''

def weekday_approx(y, m, d):
    days = int(days_between_approx(1900,1,1,y,m,d))
    return (days+1) % 7

'''assert weekday_approx(1900,1,1) == 1
assert weekday_approx(1985,10,21) == 1
assert weekday_approx(2017,9,19) == 2
assert weekday_approx(1899,12,31) == 0
assert weekday_approx(1700,1,1) == 5
assert weekday_approx(2019,9,14) == 6'''

def daysgen(y,m,d,Y,M,D,show_weekday=False):
    date = (y,m,d)
    while date != (Y,M,D):
        yield (date, weekday(*date)) if show_weekday else date
        (_y,_m,_d) = date
        if _m == 12 and _d == 31:
            date = (_y+1,1,1)
        elif _d == number_of_days(_y, _m):
            date = (_y,_m+1,1)
        else:
            date = (_y,_m,_d+1)

assert next(daysgen(1899,12,31,1900,1,4)) == (1899, 12, 31)
assert list(daysgen(1899,12,31,1900,1,4)) == \
    [(1899, 12, 31), (1900, 1, 1), (1900, 1, 2), (1900, 1, 3)]
assert list(daysgen(2020,2,28,2020,3,2)) == \
    [(2020, 2, 28), (2020, 2, 29), (2020, 3, 1)]
assert list(daysgen(2019,2,28,2019,3,2)) == \
    [(2019, 2, 28), (2019, 3, 1)]
assert sum( 1 for _ in daysgen(1985,10,21, 2017,9,19)) == 11656

from datetime import date
#assert all( (date(*t).weekday()+1)%7 == weekday(*t)for t in daysgen(1800,1,1, 2100,1,1) )

assert list(daysgen(1899,12,31,1900,1,4,True)) == \
    [((1899, 12, 31), 0), ((1900, 1, 1), 1),((1900, 1, 2), 2), ((1900, 1, 3), 3)]

assert list(daysgen(1899,12,31,1905,1,4,True)) == \
    [ (t,weekday(*t))for t in daysgen(1899,12,31,1905,1,4) ]

def approxdayrat(*p):
    N = days_between(*p)
    n = sum( 1 for (t,d) in daysgen(*p,True) if d == weekday_approx(*t) )
    #print(n,N,n/N)
    return n/N

assert isalmost( approxdayrat(1985,10,21, 2017,9,19), .49, .001 )
assert isalmost( approxdayrat(1800,1,1, 2100,1,1),     .35, .01 )
