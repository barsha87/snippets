
class TicTacToe:
    n = 3
    arr = [['-']*n for _ in range(n)]
    player = 1
    moves = 0

    def populate(self, x_pos, y_pos, char):
        if self.arr[x_pos][y_pos] == '-':
            self.arr[x_pos][y_pos] = char
            return True
        else:
            return False


    def display(self):
        for row in self.arr:
            for item in row:
                print item,
            print('\n')


    def play(self):
        if self.moves == self.n**2:
            print ('It\'s a Draw. Oh well!')
            return False
        char = 'X' if self.player == 1 else 'O'
        populated = False
        while not populated:
            pos = map(int, raw_input().split())
            populated = self.populate(pos[0], pos[1], char)
        if self.check_win(pos[0], pos[1]):
            print ('Player %s Wins!!' % self.player)
            return False
        self.player = 2 if self.player == 1 else 1
        self.moves += 1
        return True

    def get_player(self):
        return self.player

    def check_win(self, x, y):
        if self._all_row(x, y) or self._all_column(x,y) or \
            self._all_diag(x, y):
            return True
        else:
            return False

    def _all_row(self, x, y):
        char = self.arr[x][y]
        if all(item == char for item in self.arr[x]):
            return True
        return False

    def _all_column(self, x, y):
        char = self.arr[x][y]
        if all(item == char for item in
               [self.arr[i][2] for i in range(self.n)]):
            return True
        return False

    def _all_diag(self, x, y):
        char = self.arr[x][y]
        if x == y:
            if all(item == char for item in
                   [self.arr[i][i] for i in range(self.n)]):
                return True
        elif x == self.n-1-y:
            if all(item == char for item in
                   [self.arr[i][self.n-1-i] for i in range(self.n)]):
                return True
        return False


if __name__ == '__main__':
    tictac = TicTacToe()
    tictac.display()
    play = True
    while play:
        print ('Player %s\'s turn' %tictac.get_player())
        play = tictac.play()
        tictac.display()
