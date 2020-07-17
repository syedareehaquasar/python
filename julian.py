# def find_year(s):
#     return int(s[-4:])

# # def find_date(s):
# #     return int(s[:2])

# def find_month(s):
#     aplphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     month = {'JAN':0,'FEB':31,'MAR':59,'APR':,'MAY':151,'JUN':181,'JUL':212,'AUG':243,'SEP':304,'OCT':31,'NOV':30,'DEC':31}
#     for i in range(len(s)):
#         if s[i].upper() in alphabet:
#             return month[s[:3].upper()]

# def leap_year(year):
#     return True if (year%4 == 0 and year % 100 != 0) or (year % 100 == 0 and year%400 == 0) else False

# def req_output(s):

#     return str(int(s[-4:]))

# print(leap_year(2020))
# print(req_output("1 Jan 2012"))
# # print(find_month("10 Jan 2012"))
# COMMA , SPACE = "," , " "
# month_names = [SPACE, "JAN" , "FEB" , "MAR" , "APR" , "MAY" , "JUN" , "JUL" , "AUG" , "SEP" , "OCT" , "NOV" , "DEC"]

# def time_difference(city_a, timestamp , city_b):
#     sdd , mon , syyyy = timestamp.replace(COMMA,SPACE).split()
#     dd , yyyy = int(sdd) , int(syyyy)
#     mon = mon.upper()[:3]

COMMA , SPACE = "," , " "

month_names = [SPACE,"JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
leap = [0,31,29]+month_days[3:]

city_names = ["Los Angeles","New York","Caracas","Buenos Aires","London","Rome","Moscow","Tehran","New Delhi","Beijing" , "Canberra"]
city_GMT = [800,500,430,300,0,100,300,330,530,800,1000]

time_frame = dict(zip(city_names,city_GMT))
dm = dict(zip(month_names,month_days))
ldm = dict(zip(month_days,leap))

def is_leap(yyyy:int)->bool:
    c,y = divmod(yyyy,100)
    yy = c if y==0 else y
    return yy % 4 == 0

def time_difference(city_a, timestamp, city_b):
    mon , sdd , syyyy,stt = timestamp.replace(COMMA,SPACE).split()
    tt = int("".join(stt.split(":")))
    dd , yyyy = int(sdd) , int(syyyy)
    mon = mon.upper()[:3]
    m = month_names.index(mon)
    ntt = tt + (time_frame[city_a]+time_frame[city_b])
    while(ntt > 2400):
        ntt = ntt -2400
        dd += 1
        if is_leap(yyyy):
            days = ldm[mon]
        else:
            days = dm[mon]
        if dd > days:
            dd -= days
            m += 1
            if m > 12:
                yyyy += 1
                m -= 12
    return str(yyyy) + "-" + str(m) + "-" + str(dd) + " " + str(ntt//100) +":" + str(ntt%100)

print(time_difference("New York", "December 31, 1970 13:40","Beijing"))