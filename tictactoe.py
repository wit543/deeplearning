class TicTacToeGame():
    def __init__(self):
        self.state = '         ' # current board status
        self.player = 'X' # current player
        self.winner = None # winner

    def allowed_moves(self):
        """
            check if player can choose the this the slot or not
        """
        states = []
        for i in range(len(self.state)):
            if self.state[i] == ' ':
                states.append(self.state[:i] + self.player + self.state[i+1:])
        return states

    def make_move(self, next_state):
        """
            Player choose the slot 
        """
        next_state = self.get_move(next_state)
        if self.winner:
            raise(Exception("Game already completed, cannot make another move!"))
        if not self.__valid_move(next_state):
            raise(Exception("Cannot make move {} to {} for player {}".format(
                    self.state, next_state, self.player)))

        self.state = next_state
        self.winner = self.predict_winner(self.state)
        if self.winner:
            self.player = None
        elif self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def playable(self):
        """
            Check if the game is ended or not
        """
        return ( (not self.winner) and any(self.allowed_moves()) )

    def predict_winner(self, state):
        """
            Check the board for a winner.
        """
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        winner = None
        for line in lines:
            line_state = state[line[0]] + state[line[1]] + state[line[2]]
            if line_state == 'XXX':
                winner = 'X'
            elif line_state == 'OOO':
                winner = 'O'
        return winner

    def __valid_move(self, next_state):
        """
            Check if able to move or not
        """
        allowed_moves = self.allowed_moves()
        if any(state == next_state for state in allowed_moves):
            return True
        return False

    def get_move(self, idx):
        # print(self.state[:idx-1])
        # print(self.state[idx:])
        return self.state[:idx-1] + self.player + self.state[idx:]


    def print_board(self):
        s = self.state
        print('     {} | {} | {} '.format(s[0],s[1],s[2]))
        print('    -----------')
        print('     {} | {} | {} '.format(s[3],s[4],s[5]))
        print('    -----------')
        print('     {} | {} | {} '.format(s[6],s[7],s[8]))