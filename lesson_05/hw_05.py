class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.positions = []


class TicTacGame:

    def __init__(self, name_1="Alice", name_2="Bob"):
        self.player_1 = Player(name_1)
        self.player_2 = Player(name_2)
        self.board = [" " for _ in range(9)]
        self.win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                                 [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def update_player_positions(self):
        self.player_1.positions = []
        self.player_2.positions = []

    def update_board(self):
        self.board = [" " for _ in range(9)]

    def show_board(self):
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")
            print("-" * 13)

    def validate_input(self, input_idx):
        return self.board[input_idx] == " "

    def correct_input(self, input_idx):
        return 1 <= input_idx <= 9

    def print_meta(self):
        print("----------------------------------------")
        print("               Score board              ")
        print("----------------------------------------")
        print(f"        {self.player_1.name}:           {self.player_1.wins}")
        print(f"        {self.player_2.name}:             {self.player_2.wins}")
        print("----------------------------------------")

    def player_turn(self, player):
        temp_pos = int(input(f"{player.name}, choose your block: "))

        while not self.correct_input(temp_pos):
            temp_pos = int(input(f"The position {temp_pos} is located out of game field, please try again: "))

        while not self.validate_input(temp_pos - 1):
            temp_pos = int(input(f"The position {temp_pos} was already occupied, please choose another one: "))

        player.positions.append(temp_pos)

        if player == self.player_1:
            self.board[temp_pos - 1] = "X"
        else:
            self.board[temp_pos - 1] = "O"

        self.show_board()
        if self.check_winner(player.positions):
            print(f"{player.name} wins!!!")
            player.wins += 1
            self.print_meta()
            self.update_player_positions()
            self.update_board()
            return True

        return False

    def start_game(self):
        print("The game is started...")
        self.print_meta()
        end = False
        current_player = 1
        while not end:

            if current_player == 1:
                end = self.player_turn(self.player_1)
                current_player = 2

            else:
                end = self.player_turn(self.player_2)
                current_player = 1

    def check_winner(self, players_list):
        for win_comb in self.win_combinations:
            if all(j in players_list for j in win_comb):
                return True
        return False

if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()