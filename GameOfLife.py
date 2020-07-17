def preprocessing(game_file: str) -> str:
    raw_pgn = " ".join([line.strip() for line in game_file])