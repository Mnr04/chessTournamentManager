import json
import shortuuid
import os
import shutil
import random

class Player():

    def __init__(self, surname, name, age, ine):
        self.surname = surname
        self.name = name
        self.age = age
        self.ine = ine
        self.id = None 

    def get_all_players():
        file_path = os.path.join("data", "players_infos.json")

        try : 
            with open (file_path , "r") as file:
                return json.load(file)
        except (FileNotFoundError ,json.JSONDecodeError):   
            return []
    
    @classmethod
    def get_players_by_id(cls, id_to_find):
        players_list = cls.get_all_players()
        return next((p for p in players_list if p["id"] == id_to_find),None)

    @classmethod
    def update_players(cls, player_id, player_data):
       all_players = cls.get_all_players()
       player_found = False

       for player in all_players:
           if player['id'] == player_id:
               player["surname"] = player_data['surname']
               player["name"] = player_data['name']
               player["age"] = player_data['age']
               player["ine"] = player_data['ine']
               player_found = True
               break 

       if player_found:
           file_path = os.path.join('data', "players_infos.json")
           with open(file_path, "w") as file:
                json.dump(all_players, file, indent=2)
    
    def save_new_player(self):
        file_path = os.path.join('data', "players_infos.json")

        #Verify if exists
        os.makedirs("data", exist_ok=True)

        #Loads all players
        try : 
            all_players = []
            with open (file_path , "r") as file:
                all_players = json.load(file)
        except:
            all_players = []

        #Create new player 


        new_player = {
            "id" : shortuuid.uuid(),
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "ine": self.ine
        }

        all_players.append(new_player)

        #Modify the json files
        with open(file_path, "w") as file:
            json.dump(all_players, file, indent=2)

    @classmethod
    def delete_player(cls, target_id):
       all_players = [p for p in cls.get_all_players() if p['id'] != target_id]
       file_path = os.path.join('data', "players_infos.json")
       with open(file_path, "w") as file:
            json.dump(all_players, file, indent=2)

class Tournament():

    def __init__(self, name, city, total_round, players, description):

        # statemapping(0:"not_start", 1="in_progress", 2="finish")
        self.id = shortuuid.uuid()
        self.name = name
        self.city = city
        self.start = "Not Start"
        self.end = "Not Finish"
        self.actual_round = 0
        self.total_round = total_round
        self.players = players
        self.description = description
        self.start = "0"
        pass

    def tournament_to_dict(self):
        tournois_info = {
            "id" : self.id,
            "Name" : self.name,
            "City" : self.city,
            "Total_round": self.total_round,
            "Players": self.players,
            "Description": self.description,
            "Start": self.start
        }
        return tournois_info
        
    def save_tournament(self):
        #on recupere les donné 
        tournament_data = self.tournament_to_dict()

        directory = "data"
        file_path = os.path.join(directory, "tournament", self.id, "info.json")
        directory_to_create = os.path.dirname(file_path)
        os.makedirs(directory_to_create, exist_ok=True)

        with open(file_path, "w") as file:
            json.dump(tournament_data, file, indent=2)
    
    def get_tournaments_id_list():
        tournaments_list = []
        directory = "data"

        directory_path = os.path.join(directory, "tournament")
        
        try:
            for file_name in os.listdir(directory_path):
                #file_path = os.path.join(directory_path, file_name)
                tournaments_list.append(file_name)
            
            return tournaments_list

        except FileNotFoundError:
            print("Folder don't exist")
            return []
        
    @classmethod
    def get_tournament_by_id(cls, tournament_id):
        file_path = os.path.join('data', 'tournament', tournament_id, "info.json")
        with open(file_path, "r") as file:
            tournament_data = json.load(file)
    
        return tournament_data
    
    def get_all_tournement_info():
        all_tournament_data = []

        tournaments_name_list = Tournament.get_tournaments_id_list()
        for id in tournaments_name_list:
            file_path = os.path.join('data', 'tournament', id, "info.json")
            with open(file_path, "r") as file:
                tournament_data = json.load(file)
                all_tournament_data.append(tournament_data)

        return all_tournament_data

    @classmethod
    def update_tournament(cls, tournament_id, new_tournament_data, players_data):
       
       actual_tournement_data = cls.get_tournament_by_id(tournament_id)

       actual_tournement_data.update(new_tournament_data)
       actual_tournement_data["Players"] = players_data
              
      
       file_path = os.path.join('data', 'tournament', actual_tournement_data["id"], "info.json")
       with open(file_path, "w") as file:
            json.dump(actual_tournement_data, file, indent=2)

    @classmethod
    def delete_tournament(cls, target_id):

        path = os.path.join('data', "tournament",target_id)

        if os.path.isdir(path):
            shutil.rmtree(path)
            return True
        else :
            return False

    @classmethod     
    def update_tournament_statut(cls , tournament_id):
        tournament_to_start = cls.get_tournament_by_id(tournament_id)
        tournament_to_start["Actual_round"] = "1"
        file_path = os.path.join('data', 'tournament', tournament_to_start["id"], "info.json")
        with open(file_path, "w") as file:
            json.dump(tournament_to_start, file, indent=2)

     
class Round():
    @classmethod
    def create_round_1(cls, tournament_id):
        #Creer le dossier Round1
        directory = "data"
        file_path = os.path.join(directory, "tournament", tournament_id, "Round_1", "Ranking.json")
        directory_to_create = os.path.dirname(file_path)
        os.makedirs(directory_to_create, exist_ok=True)
        #Générer random player list with score and sort by  
        tournament_data = Tournament.get_tournament_by_id(tournament_id)
        player_list = [
            {"Name": p[0], "Surname": p[1], "Id": p[2], "Score": 0} 
            for p in tournament_data["Players"]
        ]
        random.shuffle(player_list)
        with open(file_path, "w") as file:
            json.dump(player_list, file, indent=2)

        #Create match list file
        directory = "data"
        file_path = os.path.join(directory, "tournament", tournament_id, "Round_1", "Match.json")
        directory_to_create = os.path.dirname(file_path)
        os.makedirs(directory_to_create, exist_ok=True)

        return player_list

    def create_match_list(player_list, tournament_id):
        match_list = []
        
        for i in range(0, len(player_list), 2):
            
            player_1 = player_list[i]
            player_2 = player_list[i + 1]

            match_player_1 = [player_1["Id"], player_1["Name"], player_1["Surname"], 0]
            match_player_2 = [player_2["Id"], player_2["Name"], player_2["Surname"], 0]

            match = (match_player_1, match_player_2)
            
            match_list.append(match)

            directory = "data"
            file_path = os.path.join(directory, "tournament", tournament_id, "Round_1", "Match.json")

        with open(file_path , "w") as file :
            json.dump(match_list, file, indent=2)
            
        return match_list

    def update_match_list(tournament_id, match_list):
        directory = "data"
        file_path = os.path.join(directory, "tournament", tournament_id, "Round_1", "Match.json")


        with open(file_path , "w") as file :
                json.dump(match_list, file, indent=2)
        pass

    @classmethod
    def update_ranking(cls, tournament_id, player_id, points_to_add):
        directory = "data"
        file_path = os.path.join(directory, "tournament", tournament_id, "Round_1", "Ranking.json")

        if not os.path.exists(file_path):
            return 

        with open(file_path, "r") as file:
            ranking = json.load(file)

        for p in ranking:
            if p["Id"] == player_id: 
                p["Score"] += points_to_add
                break
    
        with open(file_path, "w") as file:
            json.dump(ranking, file, indent=2)




