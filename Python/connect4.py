
class Board:
    WIDTH = 7
    HEIGHT = 6
    WIN_CON = 4
    def __init__(self):
        self.board = [[] for _ in range(Board.WIDTH)]
    
    def __getitem__(self, index: int) -> list:
        return self.board[index]

    def insert(self, column: int, player: int):
        self.board[column].append(player)

    def print(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if (self.HEIGHT - (i+1)) >= len(self.board[j]):
                    print("|", end=" ")
                else:
                    print(f'|{self.board[j][self.HEIGHT - (i+1)]}', end="")
            print("|")
    
    def did_player_win(self, player: int) -> bool:

        # check horizontal
        for i in range(self.HEIGHT):
            temp = 0
            for j in range(self.WIDTH):
                pos = self.HEIGHT - (i + 1)
                if pos < len(self.board[j]) and self.board[j][pos] == player:
                    temp += 1
                    if temp == self.WIN_CON:
                        return True
                else:
                    temp = 0

        # check vertical
        for i in range(self.WIDTH):
            if len(self.board[i]) >= self.WIN_CON:
                temp = 0
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    temp += 1
                    if temp == self.WIN_CON:
                        return True
                    else:
                        temp = 0
        
        # check diagonal (descending)
        for i in range(self.WIDTH - self.WIN_CON):
            for j in range(len(self.board[i])):
                i_pos, j_pos, temp = i, j+self.WIN_CON, 0
                for _ in range(self.WIN_CON):
                    if len(self.board[i_pos]) <= j_pos:
                        break
                    elif self.board[i_pos][j_pos] == player:
                        temp += 1
                        if temp == self.WIN_CON:
                            return True
                    else:
                        temp = 0
                    i_pos += 1
                    j_pos -= 1
                    
        # check diagonal (ascending)
        for i in range(self.WIDTH - self.WIN_CON):
            for j in range(len(self.board[i])):
                i_pos, j_pos, temp = i, j, 0
                for _ in range(self.WIN_CON):
                    if len(self.board[i_pos]) <= j_pos:
                        break
                    elif self.board[i_pos][j_pos] == player:
                        temp += 1
                        if temp == self.WIN_CON:
                            return True
                    else:
                        temp = 0
                    i_pos += 1
                    j_pos += 1

        return False

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [1, 2]

    def get_user_input(self) -> int:
        column = int(input(f"enter the column you want from 0 to {Board.WIDTH - 1}: "))
        while column < 0 or column > Board.WIDTH -1 or len(self.board[column]) > Board.HEIGHT - 1:
            column = int(input(f"invalid input! Please enter the column you want from 0 to {Board.WIDTH - 1}: "))
        return column

    def run(self):
        for _ in range(Board.WIDTH * Board.HEIGHT):
            for player in self.players:
                column = self.get_user_input()
                self.board.insert(column, player)
                if self.board.did_player_win(player):
                    print(f"Connect {Board.WIN_CON}! Player {player} won!")
                    return
                self.board.print()

if __name__ == "__main__":
    game = Game()    
    game.run()