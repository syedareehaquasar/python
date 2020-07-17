#...............................................................................................

# def pattern(n):
#     for i in range(n):
#         k = 2*i-2
#         for j in range(k):
#             print(end=" ")
#         k -=1
#         for j in range(i+1):
#             print("*",end=" ")
#         print("\n")

# # pattern(5)

# a1 = " "
# b1 = "*"
# def pattern(rows : int) -> str:
#     return "".join(a(row,rows)+b(row)+"\n" for row in range(1,rows+1))

# def a(row:int , rows:int) -> str:
#     return "".join((rows-row)*a1)

# def b(row:int) -> str:
#     return "".join((2*row-1)*b1)

# print(pattern(5))

# def pattern(v1,v2,rows):
#     return "".join(pattern_v1(v1,row,rows) + pattern_v2(v2,row) + "\n" for row in range(1,rows+1))

# def pattern_v1(v1,row,rows):
#     return (rows-row)*v1

# def pattern_v2(v2,row):
#     return (2*row-1)*" " if row%2 == 0 else (2*row-1)*v2

# print(pattern(' ',"*",5))

# from sys import argv

# STAR = "*"
# CRLF = "\n"
# MINUS = "-"
# SPACE = " "
# SCREEN_WIDTH = 60


# SP = STAR
# RP = MINUS + STAR
# EP = ""

# def pattern(size: int, width = SCREEN_WIDTH):
#     return CRLF.join([line(line_no, width) for line_no in range(size)])

# def line(n: int, width: int) -> str:
#     return leading_space(n, width) + start_pattern(n) + repeat_pattern(n) + end_pattern(n)

# def leading_space(n: int, w: int) -> str:
#     return (w//2 - n) * SPACE

# def start_pattern(n: int):
#     return SP

# def repeat_pattern(n: int):
#     return n * RP

# def end_pattern(n: int):
#     return EPprint(pattern(int(argv[1])))


STAR = "*"
CRLF = "\n"
SPACE = " "
SHARP = "#"
SCREEN_WIDTH = 60
MINUS = "-"
BS = "\b"

sp = SHARP
rp = MINUS + MINUS
ep = BS + SHARP

orientations = "right" , "pyramid" , "Inverse"

def pattern(size: int,  orientation = "diamond", width = SCREEN_WIDTH):
    if orientation == "pyramid":
        return CRLF.join([line(line_no , width) for line_no in range(size)])
    elif orientation == "right":
        return CRLF.join([line(line_no , 0) for line_no in range(size)])
    elif orientation == "pyramid":
        return CRLF.join([line(line_no , width) for line_no in range(size)][::-1])
    elif orientation == "diamond":
        return CRLF.join([line(line_no , width) for line_no in range(size)]) + CRLF + CRLF.join([line(line_no , width) for line_no in range(size - 1)][::-1])

def line(n: int, width:int) -> str:
    return leading_space(n,width) + start_pattern(n) + repeat_pattern(n) + end_pattern(n)

def leading_space(n: int, width: int) -> str:
    return  (width //2 - n) * SPACE

def start_pattern(n:int):
    return sp
    # return str(n)

def repeat_pattern(n:int):
    return n*rp
    # return 2*n*str(n)

def end_pattern(n:int):
    return ep

print(pattern(7))
