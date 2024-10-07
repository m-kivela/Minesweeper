import grid
import square
import random

class Game:
    """Represents a single game. Controls the game's logic and state."""

    def __init__(self, xsize: int, ysize: int, n_mines: int, seed=None):
        # Initialize the game board
        self._board = grid.Grid(xsize, ysize, square.Square)

        self._mines = n_mines               # Number of mines in the game
        self._width = xsize                 # Game board width
        self._height = ysize                # Game board height
        self._gamelost = False              # Flag set when game is lost
        self._gamewon = False               # Flag set when game is won
        self._gameover = False              # Flag set when game is over (won or lost)
        self._firstmove = True              # Flag unset when player makes first move
        self._turn = 0                      # How many turns the player has played
        self._randgen = random.Random(seed) # Random number generator

    def game_won(self) -> bool:
        """Returns whether the game has been won."""
        return self._gamewon
    
    def game_lost(self) -> bool:
        """Returns whether the game has been lost."""
        return self._gamelost
    
    def game_over(self) -> bool:
        """Returns whether the game is over."""
        return self._gameover

    def object_at(self, x: int, y: int) -> object:
        """Returns the object at the given location."""
        return self._board.object_at(x,y)
    
    def neighbors(self, x: int, y: int) -> list[object]:
        """Returns the neighboring objects at the given location (includes diagonals)."""
        return self._board.neighbors(x,y)
    
    def turn(self) -> int:
        """Returns how many turns the player has played."""
        return self._turn

    def place_mines(self) -> None:
        """Places mines randomly on the game board. Called after first move."""
        # Take all covered Squares and shuffle them in random order. Then pick
        # 'n_mines'-number of Squares from the beginning and set mines in them.
        all_squares = self._board.all_objects_filtered(square.not_revealed)
        self._randgen.shuffle(all_squares)
        mined_squares = all_squares[:self._mines]

        for a_square in mined_squares:
            a_square.set_mine()
            neighbors = self._board.neighbors(*a_square.location())
            for neighbor in neighbors:
                neighbor.increment_dangerlevel()

    def reveal(self, target: square.Square) -> bool:
        """Player clicks on a Square to uncover it. Returns 'True' if the player hit a
        mine, 'False' if the move was successful."""
        # Recursion to reveal all safe Squares if the target has no mines around it:
        def check_if_target_safe(self, target) -> None:
            if target.dangerlevel() == 0:
                neighbors = self.neighbors(*target.location())
                for neighbor in neighbors:
                    if not neighbor.is_revealed():
                        self.reveal(neighbor)

        # Gets executed on first move:
        if self._firstmove:
            self._firstmove = False
            target.reveal()
            self.place_mines()  # Mines placed only after first move is done
            check_if_target_safe(self, target)
            return False
        
        # Gets executed if the player hits a mine:
        elif target.mine():
            all_mines = self._board.all_objects_filtered(square.mined)
            for mine in all_mines:      # Reveal all mines when one mine is hit
                mine.reveal()
            return True
        
        # Gets executed when not first move and not mine:
        else:
            target.reveal()
            check_if_target_safe(self, target)
            return False

    def flag_square(self, x: int, y: int) -> None:
        """Player toggles a flag on the Square; prevents accidental click on the square and
        marks it as a mine."""
        target: square.Square = self.object_at(x,y)
        if not self._gameover:
            if target.is_flagged():
                target.unflag()
            elif not target.is_flagged():
                target.flag()

    def check_wincondition(self) -> None:
        """Checks if the player has successfully uncovered all tiles except mines, sets
        a flag '_gamewon' if so."""
        covered_squares = self._board.all_objects_filtered(square.not_revealed)
        mined_squares = self._board.all_objects_filtered(square.mined)
        only_mined_covered = True
        # Check that all covered squares have mines in them:
        for a_square in covered_squares:
            if a_square not in mined_squares:
                only_mined_covered = False
        # Check that there are the same count of covered squares and mined squares, and
        # check that only mined squares are covered:
        if len(covered_squares) == len(mined_squares) and only_mined_covered:
            self._gamewon = True
            self._gameover = True

    def play_turn(self, x: int, y: int) -> bool:
        """Gets called to play a single turn. Returns whether a turn was played."""
        # Don't allow further turns if game is already over:
        if not self._gameover:
            # Do nothing if target Square is already uncovered or flagged by the player...:
            target: square.Square = self.object_at(x,y)
            if target.is_revealed() or target.is_flagged():
                return False
            # ...execute from here otherwise
            else:
                self._turn += 1
                # Check if the player uncovered a mine, set flag '_gamelost' if so.
                # Otherwise check if the game has been won:
                if self.reveal(target):
                    self._gamelost = True
                    self._gameover = True
                    return True
                else:
                    self.check_wincondition()
                    return True
        return False