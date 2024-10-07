class Square:
    """Square represents a single position on the grid."""

    def __init__(self, x_location: int, y_location: int, parent_grid: object, has_mine: bool=False):
        self._x = x_location            # X-coord
        self._y = y_location            # Y-coord
        self._parentgrid = parent_grid  # The grid this Square is in
        self._mine = has_mine           # Square has a mine
        self._dangerlevel = 0           # How many mines in neighboring Squares
        self._flagged = False           # Has the player flagged this square as a mine
        self._revealed = False          # Player has revealed this Square
    
    def print_location(self) -> None:
        """Prints location."""
        print(f"({self._x}, {self._y})")
    
    def location(self) -> (int, int):
        """Returns tuple of its location: (x-coord, y-coord)."""
        return (self._x, self._y)
    
    def mine(self) -> bool:
        """Returns whether the square has a mine in it."""
        return self._mine
    
    def dangerlevel(self) -> int:
        """Returns the square's danger level (how many neighboring mines)."""
        return self._dangerlevel
    
    def set_dangerlevel(self, value: int) -> None:
        """Sets the square's danger level."""
        self._dangerlevel = value
    
    def increment_dangerlevel(self, repeat_n: int=1) -> None:
        """Increments this square's danger level by 1 by default, or 'repeat_n'-times"""
        self._dangerlevel += repeat_n
    
    def set_mine(self) -> None:
        """Sets up a mine in this Square."""
        self._mine = True
    
    def parent_grid(self) -> object:
        """Returns the grid this Square is in."""
        return self._parentgrid
    
    def reveal(self) -> None:
        """Sets a flag that tells this Square has been revealed by the player."""
        self._revealed = True
    
    def flag(self) -> None:
        """Sets a flag that the player thinks this Square has a mine. Prevents accidental
        uncovering once flagged."""
        self._flagged = True
    
    def unflag(self) -> None:
        """Removes a previously set flag."""
        self._flagged = False

    def is_revealed(self) -> bool:
        """Returns whether the player has revealed this Square."""
        return self._revealed
    
    def is_flagged(self) -> bool:
        """Returns whether the player has flagged this Square as a mine."""
        return self._flagged

# The following are helper functions mainly used to pass into higher order functions:
def mined(object: Square) -> bool:
    """Returns 'True' if the target Square is mined."""
    return object.mine()

def revealed(object: Square) -> bool:
    """Returns 'True' if the target Square has been uncovered."""
    return object.is_revealed()

def not_revealed(object: Square) -> bool:
    """Returns 'True' if the target Square has not been uncovered."""
    return not object.is_revealed()