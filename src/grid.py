from square import Square

class Grid:
    """Represents a grid. (0,0) is the topleft corner. X-values grow right,
    Y-values grow down."""

    def __init__(self, xsize: int, ysize: int, element):
        self._xsize = xsize
        self._ysize = ysize

        # Create the grid. Insert rows (Y-values) inside each position
        # (X-value) on the grid.
        self.grid = []        
        for i in range(xsize):
            row = []
            self.grid.append(row)

        # Initialize the grid with objects
        for x in range(xsize):
            for y in range(ysize):
                self.grid[x].append(element(x, y, self))

    def all_objects(self) -> list[object]:
        """Returns all objects in the grid."""
        list = []
        for x in self.grid:
            list.extend(x)
        return list

    def all_objects_filtered(self, func) -> list[object]:
        """Returns all objects that pass a boolean test 'func'."""
        all = self.all_objects()
        filtered = []
        for i in all:
            if func(i):
                filtered.append(i)
        return filtered

    def object_at(self, x, y) -> object:
        """Returns the object at the given location."""
        return self.grid[x][y]
    
    def neighbors(self, x_location, y_location) -> list[object]:
        """Returns the neighboring objects at the given location (includes diagonals)."""
        xrange = range(x_location - 1, x_location + 2)
        yrange = range(y_location - 1, y_location + 2)
        neighbors = []
        for x in xrange:
            for y in yrange:
                try:
                    # Prevent indexing with negative numbers,
                    # and don't count the object at the center.
                    if x >= 0 and y >= 0 and not ((x == x_location) and (y == y_location)):
                        neighbors.append(self.grid[x][y])
                except:
                    pass
        return neighbors