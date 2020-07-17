# # from itertools import chain

# # abc = "ABCDEFGHABCDEFGH"
# # num = "1234567812345678"
# # chessBoard = [[1] * 8 for i in range(8)]

# # def chess():
# #     return [x+y for x in "ABCDEFGH" for y in "12345678"]


# # def king(x1, x2, y1, y2):
# #     return abs(abc.index(x2) - abc.index(x1)) <= 1 and abs(int(y2) - int(y1)) <= 1


# # def bishop(x1, x2, y1, y2):
# #     return abs(abc.index(x2) - abc.index(x1)) == abs(int(y2) - int(y1))


# # def rook(x1, x2, y1, y2):
# #     return x2 == x1 or int(y2) == int(y1)


# # def knight(x1, x2, y1, y2):
# #     return any(abs(abc.index(x2) - abc.index(x1)) == 1 and abs(int(y2) - int(y1)) == 2, abs(abc.index(x2) - abc.index(x1)) == 2 and abs(int(y2) - int(y1)) == 1)


# # def pawn(x1, x2, y1, y2):
# #     return x2 == x1 and int(y2) - int(y1) == 1


# # def queen(x1, x2, y1, y2):
# #     return any(bishop(x1, x2, y1, y2), rook(x1, x2, y1, y2))


# # def move_possible(who, start, stop, colour):
# #     x1, y1 = start[0], start[1]
# #     x2, y2 = stop[0], stop[1]
# #     if start not in chess() or stop not in chess():
# #         return False
# #     which_piece = {'K': king, "Q": queen, "R": rook,
# #                    "B": bishop, "N": knight, "P": pawn}
# #     list(chain(*chessBoard))
# #     return which_piece[who](x1, x2, y1, y2)

# # def possitions(chessBoard,new_game_or_continue):
# #     if new_game_or_continue == 'N':
# #         chessBoard[0][0] = "BR"
# #         chessBoard[0][1] = "BK"
# #         chessBoard[0][2] = "BB"
# #         chessBoard[0][3] = "BQ"
# #         chessBoard[0][4] = "BK"
# #         chessBoard[0][5] = "BB"
# #         chessBoard[0][6] = "BK"
# #         chessBoard[0][7] = "BR"
# #         chessBoard[6][0] = "WP"
# #         chessBoard[6][1] = "WP"
# #         chessBoard[6][2] = "WP"
# #         chessBoard[6][3] = "WP"
# #         chessBoard[6][4] = "WP"
# #         chessBoard[6][5] = "WP"
# #         chessBoard[6][6] = "WP"
# #         chessBoard[6][7] = "WP"
# #         chessBoard[1][7] = "BP"
# #         chessBoard[1][0] = "BP"
# #         chessBoard[1][1] = "BP"
# #         chessBoard[1][2] = "BP"
# #         chessBoard[1][3] = "BP"
# #         chessBoard[1][4] = "BP"
# #         chessBoard[1][5] = "BP"
# #         chessBoard[1][6] = "BP"
# #         chessBoard[1][7] = "BP"
# #         chessBoard[7][0] = "WR"
# #         chessBoard[7][1] = "WK"
# #         chessBoard[7][2] = "WB"
# #         chessBoard[7][3] = "WQ"
# #         chessBoard[7][4] = "WK"
# #         chessBoard[7][5] = "WB"
# #         chessBoard[7][6] = "WK"
# #         chessBoard[7][7] = "WR"
# #     return chessBoard

# # print(move_possible("K", "D2", "B1", "W"))
# # print(possitions(chessBoard,'N'))
# # for i in chessBoard

# # import re

# # piece = {'K': king_move, "Q": queen_move, "R": Rook_move,
# #                    "B": bishop_move, "N": knight_move, "P": pawn_move}
        
# # def chessBoard():
# #     return [[1] * 8 for i in range(8)]

# # def move_validation():
# #     if in chessBoard()

# # def Rook_move():


# # def knight_move():

# # def queen_move():

# # def king_move():

# # def pawn_move():

# # def bishop_move():

# # def check():
# #     if piece():

# # def possition_updating():

# # def chess():

# from collections import namedtuple


# Square = namedtuple("Square", "File Rank")
# Move = namedtuple("Move", "Piece From To")

# BOARD = [Square(File=x, Rank=y) for x in "ABCDEFGH" for y in "12345678"]


# def move_sep(from_pos: Square, to_pos: Square) -> (int, int):
#     return abs(ord(from_pos.File) - ord(to_pos.File)), abs(ord(from_pos.Rank) - ord(to_pos.Rank))


# def check_move(move: Move) -> bool:

#     if  move.Piece not in "RNBQK" or     \
#         move.From == move.To or     \
#         move.From not in BOARD or   \
#         move.To not in BOARD:
#         # return move.To
#         return False

#     moved_by = move_sep(move.From, move.To)

#     def can_rook_move():
#         return moved_by[0] == 0 or moved_by[1] == 0


#     def can_knight_move():
#         return moved_by in [(1, 2), (2, 1)]

    
#     def can_bishop_move():
#         return moved_by[0] == moved_by[1]


#     def can_queen_move():
#         return can_rook_move() or can_bishop_move()


#     def can_king_move():
#         return moved_by in [(0, 1), (1, 0), (1, 1)]

#     return {"R": can_rook_move, "N": can_knight_move,  "B": can_bishop_move, \
#             "Q": can_queen_move, "K": can_king_move}[move.Piece]()

# print(check_move(Move("Q", Square("D", "2"), Square("D", "4"))))
# print(check_move(Move("K", Square("E", "2"), Square("E", "3"))))
# print(check_move(Move("N", Square("D", "2"), Square("E", "4"))))
# print(check_move(Move("B", Square("D", "2"), Square("F", "4"))))
# print(check_move(Move("R", Square("D", "2"), Square("E", "4"))))
# print(check_move(Move("R", Square("G", "2"), Square("E", "2"))))

BOARD = [x + y for x in "ABCDEFGH" for y in "12345678"]


def file_diff(from_pos: str, to_pos: str) -> int:
    return abs(ord(from_pos[0]) - ord(to_pos[0]))


def rank_diff(from_pos: str, to_pos: str) -> int:
    return abs(ord(from_pos[1]) - ord(to_pos[1]))


def move_sep(from_pos: str, to_pos: str) -> (int, int):
    return file_diff(from_pos, to_pos), rank_diff(from_pos, to_pos)


def check_move(piece: str, from_pos: str, to_pos: str) -> bool:
    fp = from_pos.strip().upper()
    tp = to_pos.strip().upper()
    if fp == tp or from_pos not in BOARD or to_pos not in BOARD:
        return False
    moved_by = move_sep(fp, tp)

    
    def can_rook_move():
        return moved_by[0] == 0 or moved_by[1] == 0


    def can_knight_move():
        return moved_by in [(1, 2), (2, 1)]

    
    def can_bishop_move():
        return moved_by[0] == moved_by[1]


    def can_queen_move():
        return can_rook_move() or can_bishop_move()


    def can_king_move():
        return moved_by in [(0, 1), (1, 0), (1, 1)]

    return {"R": can_rook_move, "N": can_knight_move,  "B": can_bishop_move, \
            "Q": can_queen_move, "K": can_king_move}[piece]()

print(check_move("Q", "D2", "E4"))
print(check_move("K", "E2", "E3"))
print(check_move("N", "D2", "E4"))
print(check_move("B", "D2", "E4"))
print(check_move("R", "D2", "E4"))