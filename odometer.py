# #odometer
from itertools import combinations

readings_possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def readingBasedOnSize(x):
    readings = []
    comb = list(combinations(readings_possible, x))
    for i in list(comb):
        readings.append(int("".join(str(x) for x in i)))
    return readings


def all_reading(a):
    all_readings = []
    for i in range(1, 10):
        all_readings += ReadingBasedOnSize(i)
    return all_readings


def nth_reading(n):
    x = all_reading(1)
    return x[n-1]


def reading_in_range(start: 1, limit, index_or_value):
    x = all_reading(1)
    if index_or_value == "index":
        return [x.index(y)+1 for y in range(start, limit)]
    return z.index(y) - z.index(x)

# def no_of_readings_btw(x, y):
#     z = all_reading(1)
#     return z.index(y) - z.index(x)

def next_nth_reading(nth, n):
    z = all_reading(1)
    where = z.index(nth)
    return z[where+n]


def check_validation(a):
    return True if sorted(str(a)) == str(a) else False


print(readingBasedOnSize(1))
print(reading_in_range(1, 5))
print(nth_reading(5))
print(check_validation(1234))
# print(no_of_readings_btw(1, 123456789))
print(all_reading(1))
print(next_nth_reading(2, 4))
