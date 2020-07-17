import re

game_file = "[Event \"Lloyds Bank op\"] [Site \"London\"] [Date \"1984.??.??\"] [Round \"1\"] [White \"Adams, Michael\"] [Black \"Sedgwick, David\"] [Result \"1-0\"] [WhiteElo \"\"] [BlackElo \"\"] [ECO \"C05\"] 1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4 f6 9.Bd3 Bb4+ 10.Bd2 Qb6 11.Ne2 fxe5 12.fxe5 O-O 13.a3 Be7 14.Qc2 Rxf3 15.gxf3 Nxd4 16.Nxd4 Qxd4 17.O-O-O Nxe5 18.Bxh7+ Kh8 19.Kb1 Qh4 20.Bc3 Bf6 21.f4 Nc4 22.Bxf6 Qxf6 23.Bd3 b5 24.Qe2 Bd7 25.Rhg1 Be8 26.Rde1 Bf7 27.Rg3 Rc8 28.Reg1 Nd6 29.Rxg7 Nf5 30.R7g5 Rc7 31.Bxf5 exf5 32.Rh5+  1-0"


def setup():
    squares = [y + x for x in "12345678" for y in "abcdefgh"]
    start = "RNBQKBNR" + "P" * 8 + (" " * 8) * 4 + "p" * 8 + "rnbqkbnr"
    board_view = dict(zip(squares, start))

    piece_view = {_: [] for _ in "RBKQNPrbkqnp"}
    for sq in board_view:
        piece = board_view[sq]
        if piece != " ":
            piece_view[piece].append(sq)
    return board_view, piece_view


def pgn_to_move(game_file: str) -> [str]:
    # raw_pgn = " ".join([line.strip() for line in game_file])
    raw_pgn = game_file

    comments_marked = raw_pgn.replace("{", "<").replace("}", ">")
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub("", comments_marked)
    # comments_removed = re.sub("<[^>]*>", " ", comments_marked)

    STR_marked = comments_removed.replace("[", "<").replace("]", ">")
    str_removed = STRC.sub("", STR_marked)

    MOVE_NUM = re.compile("[1-9][0-9]* *\\.")
    just_moves = [_.strip() for _ in MOVE_NUM.split(str_removed)]
    # just_moves = [_.strip() for _ in re.split("[1-9][0-9]* *\.",str_removed)]

    last_move = just_moves[-1]
    result = re.compile("( *1 *- *0 *| *0 *- *1 *| *1/2 *= *1/2 *)")
    last_move = result.sub("", last_move)
    moves = just_moves[:-1] + [last_move.strip()]

    return [_ for _ in moves if len(_) > 0]


def file_diff(from_pos: str, to_pos: str) -> int:
    return abs(ord(from_pos[0]) - ord(to_pos[0]))


def rank_diff(from_pos: str, to_pos: str) -> int:
    return abs(ord(from_pos[1]) - ord(to_pos[1]))


def move_sep(from_pos: str, to_pos: str) -> (int, int):
    return file_diff(from_pos, to_pos), rank_diff(from_pos, to_pos)


def check_move(piece: str, from_pos: str, to_pos: str) -> bool:
    fp = from_pos.strip().upper()
    tp = to_pos.strip().upper()
    if fp == tp or from_pos not in setup()[0] or to_pos not in setup()[0]:
        return False
    moved_by = move_sep(fp, tp)

    def can_rook_move():
        return moved_by[0] == 0 or moved_by[1] == 0

    def can_knight_move():
        return moved_by in [(2, 1), (1, 2)]

    def can_bishop_move():
        return moved_by[0] == moved_by[1]

    def can_queen_move():
        return can_rook_move() or can_bishop_move()

    def can_king_move():
        return moved_by in [(0, 1), (1, 0), (1, 1)]

    def can_pawn_move():
        return moved_by[0] == 0 and moved_by[1] == 1

    return {"R": can_rook_move, "N": can_knight_move,  "B": can_bishop_move,
            "Q": can_queen_move, "K": can_king_move, "P": can_pawn_move, "r": can_rook_move, "n": can_knight_move,  "b": can_bishop_move,
            "q": can_queen_move, "k": can_king_move, "p": can_pawn_move}[piece]()


pawn_piece = ["P", "p"]


def move_piece(board, piece, from_pos, to_pos):
    board[1][piece][board[1][piece].index(from_pos)] = to_pos
    board[0][from_pos] = " "
    board[0][to_pos] = piece
    return board


def is_enpassant(piece, from_pos, to_pos):
    if (piece, from_pos[1], to_pos[1]) == ('p', '4', '3') and abs(ord(from_pos[0]) - ord(to_pos[0])) == 1:
        return True
    elif (piece, from_pos[1], to_pos[1]) == ('P', '5', '6') and abs(ord(from_pos[0]) - ord(to_pos[0])) == 1:
        return True
    return False


def pawn_move(board, piece, to_pos):
    for from_pos in board[1][piece]:
        if is_enpassant(piece, from_pos, to_pos) or check_move(piece, from_pos, to_pos):
            move_piece(board, piece, from_pos, to_pos)
        elif from_pos[0] == to_pos[0]:
            if (piece, from_pos[1], to_pos[1]) == ('p', '7', '5') or (piece, from_pos[1], to_pos[1]) == ('P', '2', '4'):
                move_piece(board, piece, from_pos, to_pos)
    return board


Queen_side_castling = {'O': {'K': ('e1', 'c1'), 'R': ('a1', 'd1')}, 'o': {
    'k': ('e8', 'c8'), 'r': ('a8', 'd8')}}
King_side_castling = {'O': {'K': ('e1', 'g1'), 'R': ('h1', 'f1')}, 'o': {
    'k': ('e8', 'g8'), 'r': ('h8', 'f8')}}


def fpiece_move(board, piece, to_pos, extra):
    piece_possitions = board[1][piece]
    if extra != 0:
        for x in piece_possitions:
            if extra in x:
                if check_move(piece, x, to_pos):
                    move_piece(board, piece, x, to_pos)
    else:
        for from_pos in piece_possitions:
            if check_move(piece, from_pos, to_pos):
                move_piece(board, piece, from_pos, to_pos)
    return board


def capture(board, piece, to_pos, n, move):
    if piece in "RNBKQrnbkq":
        fpiece_move(board, piece, to_pos, 0)
    else:
        fpiece_move(board, pawn_piece[n], to_pos, piece)


def castle(board, piece, each_move):
    if piece == "O":
        king, rook = "K", "R"
    else:
        king, rook = "k", "r"
    side = Queen_side_castling
    if len(each_move) == 3:
        side = King_side_castling
    move_piece(board, king, side[piece][king][0], side[piece][king][1])
    move_piece(board, rook, side[piece][rook][0], side[piece][rook][1])
    return board


def ambiguous(m):
    if m[-1] == "#" or m[-1] == "+":
        return m[:-1]
    if m[-1] == ":":
        return m[0] + ":" + m[1:]
    if len(m) > 5:
        return m[:-4]
    return m


def pawn_promotion(board, each_move, n):
    if n == 0:
        piece = each_move[-1].upper()
    else:
        piece = each_move[-1].lower()
    board[0][each_move[:2]] = piece
    board[0][each_move[0] + str(int(each_move[:2][1])-1)] = " "
    board[1][piece].append(each_move[:2])
    return board


def each_move_display(move_num: int):
    moves = pgn_to_move(game_file)
    board = setup()
    for num, move in enumerate(moves):  # all moves
        two_moves = move.split(" ")
        for n, each_move in enumerate(two_moves):  # each step 2 moves
            each_move = ambiguous(each_move)
            if each_move[-1] in "QRBNqrbn":
                return pawn_promotion(board, each_move, n)
            elif len(each_move) == 2:
                piece = pawn_piece[n]
                pawn_move(board, piece, each_move)
            elif 3 <= len(each_move) <= 5:
                if n == 1:
                    piece = each_move[0].lower()
                else:
                    piece = each_move[0].upper()
                if piece in "oO":  # castling
                    castle(board, piece, each_move)
                elif len(each_move) == 3:
                    fpiece_move(board, piece, each_move[1:], 0)
                elif len(each_move) == 4:
                    if each_move[1] == "X" or each_move[1] == "x":  # capture
                        capture(board, each_move[1],
                                each_move[-2], n, each_move)
                    else:
                        fpiece_move(board, piece, each_move[2:], each_move[1])
        if num + 1 == move_num:
            printable = board[0].values()
            break
    return printable


# # chess print
def display(moves):
    c = []
    s = ""
    for x in moves:
        c.append(x)
    i = 8
    j = 0
    while i <= 64:
        s += str(c[j:i])
        s += "\n"
        i += 8
        j += 8
    return s


print(display(each_move_display(10)))

# c = ""
# for x in each_move_display(9):
#     c += x

# i = 8
# j = 0
# while i <= 64:
#     print(c[j:i], end=" ")
#     print()
#     i += 8
#     j += 8
