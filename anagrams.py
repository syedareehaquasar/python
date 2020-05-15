# abc = ['tar', 'State', 'rat', 'art', 'Taste', 'dream']

# for i in ans:
    #     for j in i:
    #         j = j.lower()
    # return ans

# def sortstring(s:str):
#     return sorted(s.lower())

# def a(arr):
#     more = []
#     i=0
#     while i< len(arr):
#         new = []
#         j = 0
#         while j <len(arr):
#             if sortstring(arr[j]) == sortstring(arr[i]):
#                 new.append(arr[j])
#                 arr.pop(j)
#             j += 1
#         i += 1
#         if len(new) !=0:
#             more.append(new)
#     return more

# print(a(abc))

# def anagram(a:str):
#     ans = []
#     for i in range(len(a)):
#         snew =[]
#         if any(a[i].lower() in sublist for sublist in ans) == False:
#             snew.append(a[i])
#         for j in range(i+1,len(a)):
#             if sortstring(a[i]) == sortstring(a[j]):
#                 snew.append(a[j])
#         if len(snew) != 0:
#             ans.append(snew)
#     return ans

# def list4anagrams(s):
#     newlist = []
#     for i in range(len(s)):
#         newlist += []
#         for j in range(len(s)):
#             if is_anagram(s[i],s[j]):
#                 newlist.append(s[j])
#     newlist = set(newlist)
#     return newlist

# def is_anagram(s1 : str ,s2 :str ) ->bool:
#     return True if sorted(s1.lower()) == sorted(s2.lower()) else False

# def list4anagrams(s : [str]):
#     return [word for word in s if is_anagram(s[0],word)]

# def exactlist(s):
#     for x in list4anagrams(s):
#         if x in s:
#             s.remove(x)
#     return s

# def call(s):
#     ans = []
#     while len(s)>0:
#         ans.append(list4anagrams(s))
#         s = exactlist(s)
#     ans = sorted(ans)
#     return [[j.lower() for j in i] for i in ans]

# print(call(['tar', 'State', 'rat', 'art', 'Taste', 'dream']))

#.........................................................................................
def group_anagrams( list: [str])-> [str]:
	answer=[]
	while len(list):
		answer.append(anagrams(list))
		remove(list)
	return answer

def remove(list:[str]):
	for word in anagrams(list):
		if word in list:
			list.remove(word)
	return list

def anagrams(list:[str]):
	return [word for word in list if is_anagram(list[0],word)]

def is_anagram( str1, str2):
	return sorted(str1.lower())== sorted(str2.lower())

print(group_anagrams(['tar', 'State', 'rat', 'art', 'Taste', 'dream']))