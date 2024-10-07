# Contains tools for debugging the game board through terminal

from grid import *
from game import *

def terminal_interface(game: Game) -> None:
    """Prints the game board"""
    tabsize = 3
    board = game._board
    xsize = range(board._xsize)
    ysize = range(board._ysize)

    row = [" \t".expandtabs(tabsize)]       # Initialize with whitespace
    for x in xsize:
        row.append(f"{x}\t".expandtabs(tabsize))
    print(*row)

    for y in ysize:
        row = [f"{y}\t".expandtabs(tabsize)]    # Initialize with the row's Y-coord
        for x in xsize:
            square = board.object_at(x,y)
            if square.mine():
                if square.is_revealed():
                    row.append("X_\t".expandtabs(tabsize))
                else:
                    row.append("X\t".expandtabs(tabsize))
            else:
                if square.is_revealed():
                    row.append(f"{square.dangerlevel()}_\t".expandtabs(tabsize))
                else:
                    row.append(f"{square.dangerlevel()}\t".expandtabs(tabsize))
        print(*row)