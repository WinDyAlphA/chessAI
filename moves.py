import random

def playRandomMove(board):
    legal = board.legal_moves
    move = random.choice(list(legal))
    board.push(move)