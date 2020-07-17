import re

file  = """A 12 14 16
B 5 6 7
C 17 20 23
D 2 40 12
E 6 44 15
F 7 8 9
G 4 5 6"""

def ranking(records: str) -> str:
    class_record = []
    record = re.split("\n",records +"\n" + records)
    result = ""
    final_result = ""
    for mark in record:
        class_record.append(mark.split(" "))
    for n,i in enumerate(class_record):
        e = 1
        for num in range(1,len(i)):
            result += greater(int(class_record[n][num]), greater(int(class_record[n+1][num]))):
                e = 0
        if e == 1:
            result += i[0] + " > "
    return result[:-3]

def greater(x:int, y:int) -> int:
    return x if x > y else y


print(ranking(file))