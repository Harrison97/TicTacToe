class TicTacToe:
  grid = []

  for i in range(3):
    grid.append(['-', '-', '-'])

  def print_game(self):
    for row in self.grid:
      print(row)

  def __str__(self):
    # this function is basically the same as the above
    # but instead allows us to print with print(game)
    s = ''
    for row in self.grid:
      s += str(row) + '\n'
    return s

  def play_x(self, row, col):
    if self.grid[row][col] == '-':
      self.grid[row][col] = 'X'
      if self.get_winner():
        print(self.get_winner(), ' has won the game!')
    else:
      print('Invalid move. Try again!')

  def play_o(self, row, col):
    if self.grid[row][col] == '-':
      self.grid[row][col] = 'O'
      if self.get_winner():
        print(self.get_winner(), ' has won the game!')
    else:
      print('Invalid move. Try again!')

  def get_winner(self):
    for i in range(3):
      #check all rows to find a winner
      if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != '-':
        return self.grid[i][0]
    for i in range(3):
      #check all cols to find a winner
      if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[i][0] != '-':
        return self.grid[0][i]
    if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[i][0] != '-':
      return self.grid[0][0]
    if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[i][0] != '-':
      return self.grid[0][0]
    return None

print('Hello World!')

