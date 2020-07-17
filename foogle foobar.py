# def solution( area : int) -> [int]:
#     ans = []
#     while area > 0:
#         side = int(area ** 0.5)
#         new_area = side ** 2
#         area -= new_area
#         ans.append(new_area)
#     return ans

# print(solution(15324))

# def solution(l : [int], t : int):
#     ans = []
#     for x,y in enumerate(l):
#         total = 0
#         if y == t:
#             return [-1,x]
#         for i in range(x,len(l)):
#             total += l[i]
#             if total == t:
#                 ans.append((x,i))
#     if len(ans) == 1:
#         for i in ans:
#             return i
#     return ans if ans else [-1,-1]


# print(solution([4, 3, 10, 2, 8], 12))
# print(solution([1, 2, 3, 4], 15))

# def solution(s : str) -> int:
#     z = s.replace(">","<") + s.replace("<",">")
#     return z - s
#     return salute(s) + salute(s[::-1])

# def salute(s : str) -> int:
#     ans = 0
#     for i in range(len(s)):
#         if s[i] == ">":
#             for j in range(i, len(s)):
#                 if s[j] == "<":
#                     ans += 1
#     return ans

# def solution(s : str) -> int:
#     ans = 0
#     for i in range(len(s)):
#         if s[i] == ">":
#             for j in range(i, len(s)):
#                 if s[j] == "<":
#                     ans += 2
#     return ans

# print(solution("<<>><"))

# from itertools import combinations

# def solution(l):
#     ans = 0
#     q = sorted(set(list(combinations(l,3))))
#     for i in q:
#         if i[1] % i[0] == 0 and i[2] % i[1] == 0:
#             ans += 1
#     return ans

# print(solution([1, 2, 3, 4, 5, 6]))
# print(solution([1,1,1]))

# import re

# x = "<-->"
# z = re.sub("<",">",x)
# x = re.sub(">","<",x)
# print(z)

# from fractions import Fraction


# def gcd(x, y):
#     def gcd1(x, y):
#         if y == 0:
#             return x
#         return gcd1(y, x % y)
#     return gcd1(abs(x), abs(y))


# def simplify(x, y):
#     g = gcd(x, y)
#     return Fraction(x//g, y//g)


# def lcm(x, y):
#     return (x*y/gcd(x, y))


# def transform(matrix):
#     sum_list = list(map(sum, matrix))
#     bool_indices = list(map(lambda x: x == 0, sum_list))
#     indices = set([i for i, x in enumerate(bool_indices) if x])
#     new_mat = []
#     for i in range(len(matrix)):
#         new_mat.append(list(map(lambda x: Fraction(0, 1) if(
#             sum_list[i] == 0) else simplify(x, sum_list[i]), matrix[i])))
#     transform_mat = []
#     zeros_mat = []
#     for i in range(len(new_mat)):
#         if i not in indices:
#             transform_mat.append(new_mat[i])
#         else:
#             zeros_mat.append(new_mat[i])
#     transform_mat.extend(zeros_mat)
#     tmat = []
#     for i in range(len(transform_mat)):
#         tmat.append([])
#         extend_mat = []
#         for j in range(len(transform_mat)):
#             if j not in indices:
#                 tmat[i].append(transform_mat[i][j])
#             else:
#                 extend_mat.append(transform_mat[i][j])
#         tmat[i].extend(extend_mat)
#     return [tmat, len(zeros_mat)]


# def copy_mat(matrix):
#     cmat = []
#     for i in range(len(matrix)):
#         cmat.append([])
#         for j in range(len(matrix[i])):
#             cmat[i].append(
#                 Fraction(matrix[i][j].numerator, matrix[i][j].denominator))
#     return cmat


# def gauss_elmination(m, values):
#     matrix = copy_mat(m)
#     for i in range(len(matrix)):
#         index = -1
#         for j in range(i, len(matrix)):
#             if matrix[j][i].numerator != 0:
#                 index = j
#                 break
#         if index == -1:
#             raise ValueError('Gauss elimination failed!')
#         matrix[i], matrix[index] = matrix[index], matrix[j]
#         values[i], values[index] = values[index], values[i]
#         for j in range(i+1, len(matrix)):
#             if matrix[j][i].numerator == 0:
#                 continue
#             ratio = -matrix[j][i]/matrix[i][i]
#             for k in range(i, len(matrix)):
#                 matrix[j][k] += ratio * matrix[i][k]
#             values[j] += ratio * values[i]
#     ans = [0 for i in range(len(matrix))]
#     for i in range(len(matrix)):
#         index = len(matrix) - 1 - i
#         end = len(matrix) - 1
#         while end > index:
#             values[index] -= matrix[index][end] * ans[end]
#             end -= 1
#         ans[index] = values[index]/matrix[index][index]
#     return ans


# def transpose(matrix):
#     tmat = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i == 0:
#                 tmat.append([])
#             tmat[j].append(matrix[i][j])
#     return tmat


# def inverse(matrix):
#     tmat = transpose(matrix)
#     mat_inv = []
#     for i in range(len(tmat)):
#         values = [Fraction(int(i == j), 1) for j in range(len(matrix))]
#         mat_inv.append(gauss_elmination(tmat, values))
#     return mat_inv


# def mat_mult(mat1, mat2):
#     ans = []
#     for i in range(len(mat1)):
#         ans.append([])
#         for j in range(len(mat2[0])):
#             ans[i].append(Fraction(0, 1))
#             for k in range(len(mat1[0])):
#                 ans[i][j] += mat1[i][k] * mat2[k][j]
#     return ans


# def splitQR(matrix, lengthR):
#     lengthQ = len(matrix) - lengthR
#     Q = []
#     R = []
#     for i in range(lengthQ):
#         Q.append([int(i == j)-matrix[i][j] for j in range(lengthQ)])
#         R.append(matrix[i][lengthQ:])
#     return [Q, R]


# def solution(matrix):
#     ans = transform(matrix)
#     if ans[1] == len(matrix):
#         return [1, 1]
#     Q, R = splitQR(*ans)
#     inv = inverse(Q)
#     ans = mat_mult(inv, R)
#     row = ans[0]
#     l = 1
#     for item in row:
#         l = lcm(l, item.denominator)
#     ans = list(map(lambda x: (x.numerator*l/x.denominator), row))
#     ans.append(int(l))
#     return ans


# print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [
#       0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))


# def firstUniqChar(s: str) -> int:
#     for i in s:
#         x = s.count(i)
#         if x == 1:
#             return s.index(i)
#     return -1

# print(firstUniqChar("a"))

# def solution(n):
#     n = int(n)
#     step = 0
#     while n > 1:
#         if n & 1 ==0:
#             n >>= 1
#         else:
#             n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)
#         step += 1
#     return step

# print(solution(15))

# from itertools import combinations

# def solution(banana_list):
#     b = []
#     ans = combinations(banana_list, 2)
#     for x,y in ans:
#         b.append((x,y))
#     return b

# def solution(banana_list):
#     ans = 0
#     for n, i in enumerate(banana_list):
#         if i not in banana_list[:n] or n == 0:
#             if banana_list.count(i) > 1:
#                 ans += banana_list.count(i)
#     return ans

# print(solution([1, 2, 3, 4, 5, 5, 2, 0]))
# print(solution([1, 7, 3, 21, 13, 19]))

# def willLoop(x, y):
#     n = x+y
#     n_tilde = n
#     while n_tilde % 2 == 0:
#         n_tilde = n_tilde / 2
#     return (x % n_tilde) != 0

# def bananaGraph(banana_list):
#     G = {i: [] for i in range(len(banana_list))}
#     for i, a in enumerate(banana_list):
#         for j, b in enumerate(banana_list):
#             if i != j and willLoop(a, b):
#                 G[i].append(j)
#     return G

# def answer(banana_list):
#     G = bananaGraph(banana_list)
#     matches = bananaGraph(G)
#     return len(banana_list) - len(matches)

# print(answer([1, 1]))
# print(answer([1, 7, 3, 21, 13, 19]))
# print(answer([1]))
# print(answer([1, 7, 1, 1]))

# from itertools import combinations


# def solution(num_buns, num_required):
#     keyrings = [[] for num in range(num_buns)]
#     copies_per_key = num_buns - num_required + 1
#     for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
#         for bunny in bunnies:
#             keyrings[bunny].append(key)

#     return keyrings


# print(solution())

def matches_possible(graph):
    n_edges = [[x, y] for x in range(len(graph))
                        for y in range(len(graph[x]))
                        if graph[x][y] == 1]
    matchingEdges = []
    nonmatching = [x for x in range(len(graph))]
    pathFound = True
    while pathFound:
        pathFound = False
        for j in nonmatching:
            visited = []
            path = []
            node = j
            edgeNotInMatching = True
            while 1:
                findUnvisited = False
                visited.append(node)
                index = 0
                for i in range(len(graph[node])):
                    if i not in visited and graph[node][i] != 0:
                        if ((edgeNotInMatching and [node, i] in n_edges)
                                or (not edgeNotInMatching and [node, i] in matchingEdges)):
                            edgeNotInMatching = not edgeNotInMatching
                            index = i
                            findUnvisited = True
                            break
                if findUnvisited:
                    path.append(node)
                    node = index
                elif not path:
                    break
                else:
                    node = path.pop()
                    edgeNotInMatching = not edgeNotInMatching
                if node in nonmatching and node != j:
                    path.append(node)
                    pathFound = True
                    for i in range(len(path) - 1):
                        if [path[i], path[i + 1]] in matchingEdges:
                            matchingEdges.remove([path[i], path[i + 1]])
                            matchingEdges.remove([path[i + 1], path[i]])
                            n_edges.append([path[i], path[i + 1]])
                            n_edges.append([path[i + 1], path[i]])
                        else:
                            n_edges.remove([path[i], path[i + 1]])
                            n_edges.remove([path[i + 1], path[i]])
                            matchingEdges.append([path[i], path[i + 1]])
                            matchingEdges.append([path[i + 1], path[i]])
                    nonmatching.remove(path[0])
                    nonmatching.remove(path[len(path) - 1])
                    break
    return len(nonmatching)


def solution(banana_list):
    pairs = [[0 for y in banana_list] for x in banana_list]
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            guardi, guardj = banana_list[i], banana_list[j]
            if (guardi + guardj) % 2 == 1:
                pairs[i][j] = 1
                continue
            if guardi == guardj:
                continue
            while guardi % 2 == 0 and guardj % 2 == 0:
                guardi /= 2
                guardj /= 2
            if guardi % 2 != guardj % 2:
                pairs[i][j] = 1
                continue
            while guardi != guardj and (guardi + guardj) % 2 != 1:
                temp = max(guardi, guardj)
                guardi = min(guardi, guardj)
                guardj = temp - guardi
                guardi *= 2
                guardi /= 2
                guardj /= 2
            if (guardi + guardj) % 2 == 1:
                pairs[i][j] = 1
    return matches_possible(pairs)


print(solution([1, 7, 3, 21, 13, 19]))
