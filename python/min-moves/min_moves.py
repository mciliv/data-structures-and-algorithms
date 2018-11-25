"""
    Problem:

        On an 8x8 chess board, determine the minimum number of turns it would
        take for a chess piece at a given position to move to a goal position.
        If the goal position is unreachable, return a value representing that
        fact.

        Your solution should work for the following pieces:
        - King (can move 1 square in any direction per turn)
        - Knight (can move in a 2x1 or 1x2 "L" pattern per turn)
        - Bishop (can move any number of squares diagonally per turn)

        This is meant to be open ended. The only requirement is that the code is
        easily reviewable by the Tech Screener on your next interview.

    Morgan's Representation:

        - A position on a board is a tuple with values between 0 and 7
        - A chess piece's move on the board has the same representation as a
          position
        - The chess pieces set moves is a Python set
        - A chess piece is a string

"""

BOARD_DIM = 8

PIECE_MOVES = \
 {'King':
 {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)},
 'Knight':
 {(2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2)},
 'Bishop':
 {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
  (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
  (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
  (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)}}

def new_positions(move_set, start, tried_positions):
    """returns the moves given a piece's starting position and it's set of
        moves"""
    new_positions_set = set()
    for move in move_set:
        new_position = (move[0] + start[0], move[1] + start[1])
        if new_position[0] >= 0 and new_position[0] < BOARD_DIM and \
            new_position[1] >= 0 and new_position[1] < BOARD_DIM and \
            new_position not in tried_positions:
            new_positions_set.add(new_position)

    return new_positions_set

def min_moves_given_set(move_set, start, goal):
    """returns the min number of moves to get from the start position to
        the goal position on an 8x8 chessboard given move_set. If 'goal' can
        not be reached then 'None' is returned"""
    min_moves_num = 0
    positions = {start}
    tried_positions = set()
    next_positions = set()
    while True:
        if len(positions) == 0:
            return None

        for position in positions:
            if position == goal:
                return min_moves_num
            tried_positions.add(position)
            subsequent_positions = new_positions(move_set, position, \
                                                 tried_positions)
            next_positions = next_positions.union(subsequent_positions)

        positions = next_positions
        next_positions = set()
        min_moves_num += 1


def min_moves(piece, start, goal):
    """returns the min number of moves for the piece to get from the start
        position to the goal position on a 8x8 chessboard. If the piece can't
        reach 'goal' then 'None' is returned"""
    return min_moves_given_set(PIECE_MOVES[piece], start, goal)
