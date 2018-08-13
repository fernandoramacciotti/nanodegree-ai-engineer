from copy import deepcopy

xlim, ylim = 3,2
class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
        and a coordinate system where [0][0] is the top-
        left corner, and x increases to the right while
        y increases going down (this is an arbitrary
        convention choice -- there are many other options
        that are just as good)

    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player two

    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player one is at (0, 0) and player two is at (1, 0)
    """
    def __init__(self):
        # single-underscore prefix on attribute names means
        # that the attribute is "private" (Python doesn't truly
        # support public/private members, so this is only a
        # convention)
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1  # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]


    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        # TODO: implement this function!
        loc = self._player_locations[self._parity] # player location

        if not loc: # if loc is None
            legal_moves = [(x, y)
                         for x in range(xlim)
                         for y in range(ylim)
                         if self._board[x][y] == 0]
            return legal_moves

        legal_moves = []
        possible_directions = [( 0,  1), ( 0, -1),
                               ( 1,  0), ( 1, -1), ( 1,  1),
                               (-1,  0), (-1,  1), (-1, -1)]

        for dx, dy in possible_directions:
            _x, _y = loc
            while 0<= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]:
                    break
                legal_moves.append((_x, _y))

        return legal_moves


    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position f   or the active player's next move
            (e.g., (0, 0) if the active player will move to the
            top-left corner of the board)
        """
        # TODO: implement this function!
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        newBoard = deepcopy(self)
        newBoard._board[move[0]][move[1]] = 1
        newBoard._player_locations[self._parity] = move
        newBoard._parity ^= 1
        return newBoard
