import tkinter as tk
from game import Game
from square import Square
import constants
import os

# Asset locations
currentdir = os.path.dirname(os.path.abspath(__file__))
assetsdir = os.path.join(currentdir, '..', 'assets')

icon_flag = os.path.join(assetsdir, 'flag.png')
icon_mine = os.path.join(assetsdir, 'mine.png')


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(constants.title)

        # Create a menu bar and insert a menu called 'Menu' in it:
        self.menubar = tk.Menu(self.root)   # Create
        self.root["menu"] = self.menubar    # Insert

        self.menu = tk.Menu(self.menubar, tearoff=False)        # Create
        self.menubar.add_cascade(menu=self.menu, label="Menu")  # Insert

        self.newgame = tk.Menu(self.menu, tearoff=False)            # Create
        self.menu.add_cascade(menu=self.newgame, label="New Game")  # Insert

        # Fill menu:
        self.newgame.add_command(label="Easy", command=self.new_game_easy)
        self.newgame.add_command(label="Intermediate", command=self.new_game_intermediate)
        self.newgame.add_command(label="Hard", command=self.new_game_hard)

        self.mineimg = tk.PhotoImage(file=icon_mine)
        self.flagimg = tk.PhotoImage(file=icon_flag)

        # Initial content:
        self.create_content(constants.difficulty[0])
    
    def create_content(self, difficulty):
        """Creates a new content window (new game) that will be inserted into root."""
        self.content = tk.Frame(self.root)
        self.content.grid()

        width = difficulty["width"]
        height = difficulty["height"]
        n_mines = difficulty["n_mines"]
        self._game = Game(width, height, n_mines)

        # Head:
        self.head = tk.Frame(self.content, borderwidth=1, relief="solid")
        self.head.grid(row=0, column=0, padx=5, pady=0, sticky="nesw")

        self.statuslabel = tk.Label(self.head, text=" ")
        self.statuslabel.grid(row=0, column=1, padx=2, pady=2)

        self.turnlabel = tk.Label(self.head, text=f"Turn: {self._game.turn()}")
        self.turnlabel.grid(row=0, column=0, padx=2, pady=2)

        # Gameboard:
        self.gameboard = tk.Frame(self.content)
        self.gameboard.grid(row=1, column=0, padx=5, pady=5)

        # Button Grid:
        self.buttons = []
        for x in range(self._game._width):
            for y in range(self._game._height):
                button = tk.Canvas(self.gameboard, width=18, height=18, borderwidth=1,
                                  relief="raised", bg="lightgray")
                button.grid(column=x, row=y, padx=0, pady=0)
                # Key bindings:
                button.bind("<Button-1>", lambda event, column=x, row=y:
                            self.left_click(event, column, row))
                button.bind("<Button-3>", lambda event, column=x, row=y:
                            self.right_click(event, column, row))
                self.buttons.append({"button": button,
                                     "x": x,
                                     "y": y,
                                     "image": None})

    def new_game(self, difficulty):
        """Creates a new game. Destroys old content and replaces it with new."""
        self.content.destroy()
        self.create_content(difficulty)

    def new_game_easy(self):
        """Creates a new easy game."""
        self.new_game(constants.difficulty[0])
    
    def new_game_intermediate(self):
        """Creates a new intermediate game."""
        self.new_game(constants.difficulty[1])
    
    def new_game_hard(self):
        """Creates a new hard game."""
        self.new_game(constants.difficulty[2])

    def mainloop(self):
        self.root.mainloop()
    
    def update_board(self):
        """Checks the state of each Square and updates the visuals accordingly."""
        for a_button in self.buttons:
            button = a_button["button"]
            x = a_button["x"]
            y = a_button["y"]
            target: Square = self._game.object_at(x,y)
            
            # Update head:
            self.turnlabel.configure(
                text=f"Turn: {self._game.turn()}")
            if self._game.game_over() and self._game.game_won():
                self.statuslabel.configure(text=constants.victorytext)
            elif self._game.game_over() and self._game.game_lost():
                self.statuslabel.configure(text=constants.losetext)

            # Draw uncovered mines:
            if target.mine() and target.is_revealed():
                button.delete(a_button["image"])
                button.create_image(12, 12, image=self.mineimg, anchor="center")
                button.configure(bg="red")

            # Draw uncovered tiles:
            elif target.is_revealed():
                button.configure(bg="gray", relief="sunken")
                dangerlevel = target.dangerlevel()
                # Remove clutter by drawing safe tiles as blank:
                if dangerlevel == 0:
                    dangerlevel = " "
                button.create_text(12, 12, anchor="center", text=f"{dangerlevel}",
                                   fill="white")
            
            # Draw flags:
            elif target.is_flagged() and not target.is_revealed():
                # Only draw flag if no previous flag exists:
                if a_button["image"] == None:
                    imgID = button.create_image(12, 12, image=self.flagimg, anchor="center")
                    a_button["image"] = imgID
            
            # Neutral uncovered tile:
            else:
                button.configure(bg="lightgray")
                button.delete(a_button["image"])
    
    def left_click(self, event, x, y):
        if self._game.play_turn(x,y):
            self.update_board()

    def right_click(self, event, x, y):
        self._game.flag_square(x,y)
        self.update_board()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()