class Team:
    def __init__(self, input_name, input_players,input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def team_has_name(self):
        return self.name

    def team_has_players(self):
        return self.players

    def team_has_coach(self):
        return self.coach

    def add_player(self, name):
        self.players.append("name")

    def has_player(self, player_to_find):
        return self.players.count(player) > 0
# alternative way
        # for player in self.players:
        #     if player == player_to_find:
        #         return True
        # return False


    def play_game(self, game_won):
        if game_won:
            self.points += 3