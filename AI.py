import chess
import random
import moves

board = chess.Board()

moves.playRandomMove(board)
moves.playRandomMove(board)
print(board.legal_moves)



