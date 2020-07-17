# karprekar 4 digits then form no. subtract largest from smallest the stop when constant
x = input()

def smallest(x : str) -> int:
    return int("".join(sorted(str(x))))

def largest(x : str) -> int:
    return int("".join(sorted(str(x), reverse=True)))

def diff(x : int) -> int:
    return largest(x) - smallest(x)

def series(n: int, last:int = 0):
    if n == last:
        return "end"
    else:
        last = diff(x)
        return f'{x}\n {largest(x)}\n ' + series(last,x)

print(series(x))
def num2digits(n: int) -> [int]:
    return [int(ch) for ch in str(n)]


def digits2num(ds: [int]) -> int:
    return int("".join(str(d) for d in ds))


def next_kap(n: int) -> int:
    ds = num2digits(n)
    maxi = digits2num(sorted(ds, reverse=True))
    mini = digits2num(sorted(ds))
    return n, maxi, mini, maxi - mini


def kap_seq(n: int) -> [int]:
    nn = next_kap(n)
    if nn[-1] == n:
        return [nn]
    return [nn] + kap_seq(nn[-1])


for k in kap_seq(1267):
    print(k)
print(kap_seq(2376))

lis=intlist(num)
    if len(set(lis))==1:
        return "All digits same!"
    smallest= getsmallest(lis)
    largest= getlargest(lis)
    curr=largest-smallest
    templis=[]
    while curr not in templis:
        templis.append(curr)
        smallest=getsmallest(intlist(curr))
        largest=getlargest(intlist(curr))
        curr=largest-smallest
    return templis[templis.index(curr):]