class Env(object):
    def __init__(self, grid_size=3):
        self.grid_size = grid_size
        self.reset()

    def _update_state(self, action):
        state = self.state
        self.action = action
        cell = int(action)
        if state[cell] == 0:
            if state.count(1) == state.count(-1):
                state[cell] = 1
            else:
                state[cell] = -1
        self.state = state

    def _check_win(self):
        state = self.state
        combinations = [
            # horizontal
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            # vertical
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            # crossed
            ((0, 0), (1, 1), (2, 2)),
            ((2, 0), (1, 1), (0, 2))
        ]
        for coordinates in combinations:
            letters = [state[3 * x + y] for x, y in coordinates]
            if sum(letters) == 3:
                return 1
            if sum(letters) == -3:
                return 2
        return 0

    def _get_reward(self, player):
        state = self.state
        count_O = state.count(1)
        count_X = state.count(-1)
        if self._check_win() == 1:
            if player == 'O':
                return reward_win
            else:
                return reward_loss
        elif self._check_win() == 2:
            if player == 'O':
                return reward_loss
            else:
                return reward_win
        elif count_O + count_X == 9:
            return reward_draw
        else:
            return reward_default

    def observe(self):
        return np.array(self.state).reshape((1, -1))

    def act(self, action, player):
        self._update_state(action)
        reward = self._get_reward(player)
        game_over = reward != 0
        return self.observe(), reward, game_over

    def reset(self):
        self.state = [0 for x in range(9)]