import random
class Player:

    def __init__(self, ID_player, name, position, fga_1_average, fga_2_average, fga_3_average, offense_participation, on_court):
        print("A player has been initialise")
        self.ID_player = ID_player
        self.name = name
        self.position = position
        self.offense_participation = offense_participation
        self.fga_1_average = fga_1_average #Ex. 0.50 -> Range between 0-1
        self.fga_2_average = fga_2_average
        self.fga_3_average = fga_3_average
        self.attempts_statistics = {
            "attempt_1": 0,
            "attempt_1_made":0,
            "attempt_2": 0,
            "attempt_2_made":0,
            "attempt_3": 0,
            "attempt_3_made":0,
        }
        self.rebounds_num = 0
        self.assists_num = 0
        self.steals_num = 0
        self.blocks_num = 0
        self.turnovers_num = 0
        self.fouls_num = 0
        self.fouled_out = False
        self.on_court = on_court
        self.seconds_played = 0
        #self.minutes_played = round(self.seconds_played / 60)  #the decimals are not used.
        #¿minutes played? Stage 2
    
    def __str__(self):
        return "This is the player with ID "+str(self.ID_player)+" and name "+self.name+"."
    
    def field_goal_attempt(self, type_shoot):   #a recommended % of sd = 0.25
        if type_shoot == 1:
            attempt_nd = self.fga_1_average
        elif type_shoot == 2:
            attempt_nd = self.fga_2_average
        elif type_shoot == 3:
            attempt_nd = self.fga_3_average
        
        attempt_result = False
        if random.random() <= attempt_nd:
            attempt_result = True
        
        return attempt_result
    
    def update_field_goal_attempt(self, type_shoot, result_shoot):
        
        #First, we fixed the type of shoot
        if type_shoot == 1:
            attempts_ls = ["attempt_1", "attempt_1_made"]
        elif type_shoot == 2:
            attempts_ls = ["attempt_2","attempt_2_made"]
        elif type_shoot == 3:
            attempts_ls = ["attempt_3","attempt_3_made"]
        
        #Second, we update the attempts_statistics dictionary 
        self.attempts_statistics[attempts_ls[0]] += 1
        if result_shoot == True:
            self.attempts_statistics[attempts_ls[1]] += 1

    
    def rebound_made(self):
        self.rebounds_num += 1
    
    def assist_made(self):
        self.assists_num += 1
    
    def steal_made(self):
        self.steals_num += 1
    
    def block_made(self):
        self.blocks_num += 1
    
    def turnover_made(self):
        self.turnovers_num += 1
    
    def foul_made(self):
        self.fouls_num += 1
        if self.fouls_num == 6:
            self.fouled_out = True
    
    def court_in(self):   #we use this function to change the status of a player and make him on court to play
        if self.fouls_num < 6 and self.on_court == False:
            self.on_court = True
        elif self.fouls_num == 6:
            print(f"The player {self.name} cannot play, has been fouled out.")
        elif self.on_court == True:
            print(f"The player {self.name} is already on the court.")

    def court_out(self):  #we use it to bench the player
        if self.on_court == True:
            self.on_court = False
            print(f"The player {self.name} has been benched.")
    
    #in every possession it is needed to update the seconds of the player that is "on_court"=True
    #self.seconds_played
    def add_seconds_played(self, posssession_seconds):
        if self.on_court == True:
            self.seconds_played += posssession_seconds
    
    def get_points_made(self):
        
        points_1 = self.attempts_statistics["attempt_1_made"]
        points_2 = self.attempts_statistics["attempt_2_made"]
        points_3 = self.attempts_statistics["attempt_3_made"]
        total_points = points_1 + points_2 + points_3
        return total_points

    




