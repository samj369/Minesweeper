This is a simple command-line version of the classic Minesweeper game implemented in Python. The game is played on a 5x5 grid where the player uncovers cells while trying to avoid hidden mines. 
The number of adjacent mines is revealed to help guide the player. The game ends either when a mine is revealed (loss) or all safe cells are uncovered (win!).

Game Features:
- 5x5 grid board
- Random or fixed mine placement
- Reveals number of adjacent mines
- Win detection (all safe cells uncovered)
- CLI input handling with validation
- Unit tests with pytest

Playing the Game:

To use specific board configurations, you can define mine positions directly in play_minesweeper.py

Rules:
- Select a cell using row and column numbers (0–4)
- If you uncover a mine (X), the game ends and you have lost :(
- If the cell is safe, the number of surrounding mines is shown
- The game is won when all safe cells are revealed




