import json
import uuid
import os

class Player():
    def __init__(self, surname, name, age, ine):
        self.surname = surname
        self.name = name
        self.age = age
        self.ine = ine
        self.id = None 

    def save_new_joueur(self):
        directory = "data"
        file_path = os.path.join(directory, "players_infos.json")

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
            "id" : str(uuid.uuid4()),
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "ine": self.ine
        }

        all_players.append(new_player)

        #Modify the json files
        with open(file_path, "w") as file:
            json.dump(all_players, file, indent=2)

        print(f"user : {self.name} {self.surname} registred with sucess")


class Tournament():
    def __init__(self, name, city, date, tournament_tour_number, actual_tour, tour_list, registred_player, description):
        self.name = name
        self.city = city
        self.date = date
        self.tournament_tour_number = tournament_tour_number
        self.actual_tour = actual_tour
        self.tour_list = tour_list
        self.registred_player = registred_player
        self.description = description
        pass

class Database():
    def __init__():
        pass

class Tours():
    def __init__():
        pass

class Match():
    def __init__():
        pass

#test creer new joueur :
newplayer = Player("jean","bernard","a","a")
newplayer.save_new_joueur()