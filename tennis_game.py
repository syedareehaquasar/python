# tennis game
scoreboard = {'Players': ['A', 'B'], 'match': [0, 0],'sets': [0, 0], 'games': [0, 0], 'points': [0, 0]}
who = {'A': 0, 'B': 1}


def point(s):
    for i in range(len(s)):
        scoreboard['points'][who[s[i]]] += 1
        if win(scoreboard['points'][0], scoreboard['points'][1]) and (scoreboard['points'][who[s[i]]] >= 4):
            return game(s[i], s[i+1:])
    return scoreboard


def game(x, remaining_evaluation):
    scoreboard['points'] = [0, 0]
    scoreboard['games'][who[x]] += 1
    if win(scoreboard['games'][0], scoreboard['games'][1]) and scoreboard['games'][who[x]] >= 6:
        return sets(x, remaining_evaluation)
    return point(remaining_evaluation)


def sets(x, remaining_evaluation):
    scoreboard['games'] = [0, 0]
    scoreboard['sets'][who[x]] += 1
    if win(scoreboard['sets'][0], scoreboard['sets'][1]) and scoreboard['sets'][who[x]] >= 2:
        return match(x, remaining_evaluation)
    return point(remaining_evaluation)


def match(x, remaining_evaluation):
    scoreboard['sets'] = [0, 0]
    scoreboard['match'][who[x]] += 1
    if win(scoreboard['match'][0], scoreboard['match'][1]) and scoreboard['match'][who[x]] >= 2:
        return x + "has won"
    return point(remaining_evaluation)


def win(a, b):
    return True if ((a-b) >= 2 or (b-a) >= 2) else False


def scoring(s):
    if point(s):
        score = {0: 'love', 1: 15, 2: 30, 3: 40, 4: 'ad', 5: 'ad', 6: 'ad'}
        for i in range(2):
            scoreboard['points'][i] = score[scoreboard['points'][i]]
        return point(s)
    else:
        score = {0: 'love', 1: 15, 2: 30, 3: 40, 4: 'ad', 5: 'ad', 6: 'ad'}
        for i in range(2):
            scoreboard['points'][i] = score[scoreboard['points'][i]]
        return scoreboard


print(scoring("ABABABAAB"))

#...............................................................................................................................................

# def point(s):
#     for i in range(len(s)):
#         if s[i] == "A":
#             scoreboard['points'][0] += 1
#             if win(scoreboard['points'][0],scoreboard['points'][1]) and scoreboard['points'][0] >= 4:
#                 return game("A",s[i:])
#         else: #in B
#             scoreboard['points'][1] += 1
#             if win(scoreboard['points'][1],scoreboard['points'][0]) and scoreboard['points'][1] >= 4:
#                 return game("B",s[i:])

# def game(x,left):
#     scoreboard['points'] = [0,0]
#     if x == "A":
#         scoreboard['games'][0] += 1
#         if win(scoreboard['games'][0],scoreboard['games'][1]) and scoreboard['games'][0] >= 6:
#             return sets("A",left)
#         point(left)
#     else: # x == "B":
#         scoreboard['games'][1] += 1
#         if win(scoreboard['games'][1],scoreboard['games'][0]) and scoreboard['games'][1] >= 6:
#             return sets("B",left)
#         point(left)

# def sets(x,left):
#     scoreboard['games'] = [0,0]
#     if x == 'A':
#         scoreboard['sets'][0] += 1
#         if scoreboard['sets'][0] >= 2 and win(scoreboard['sets'][0],scoreboard['sets'][1]):
#             return match("A",left)
#         point(left)
#     else: # x== 'B':
#         scoreboard['sets'][1] += 1
#         if scoreboard['sets'][1] >= 2 and win(scoreboard['sets'][1],scoreboard['sets'][0]):
#             return match("B",left)
#         point(left)

# def match(x,left):
#     scoreboard['sets'] = [0,0]
#     if x == 'A':
#         scoreboard['match'][0] += 1
#         if scoreboard['match'][0] >= 2 and win(scoreboard['match'][0],scoreboard['match'][1]):
#             return "A has Won" + str(scoreboard)
#         point(left)
#     else: # x == 'B'
#         scoreboard['match'][1] += 1
#         if scoreboard['match'][1] >= 2 and win(scoreboard['match'][1],scoreboard['match'][0]):
#             return "B has won" + str(scoreboard)
#         point(left)