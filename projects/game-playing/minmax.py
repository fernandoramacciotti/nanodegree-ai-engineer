from minmax_helpers import *

def minimax_decision(gameState, depth):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    # TODO: Finish this function!
    return max(gameState.get_legal_moves(),
               key=lambda x: min_value(gameState.forecast_move(x)))

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    # TODO: finish this function!
    return not bool(gameState.get_legal_moves())

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    # TODO: finish this function!
    if terminal_test(gameState):
        return 1

    v = float('inf')
    for a in gameState.get_legal_moves():
        v = min(v, max_value(gameState.forecast_move(a)))
    return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    # TODO: finish this function!
    if terminal_test(gameState):
        return -1

    v = float('-inf')
    for a in gameState.get_legal_moves():
        v = max(v, min_value(gameState.forecast_move(a)))
    return v
