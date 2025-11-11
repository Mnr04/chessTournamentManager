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

    def get_all_players():
        players_list = []
        directory = "data"
        file_path = os.path.join(directory, "players_infos.json")

        try : 
            with open (file_path , "r") as file:
                    all_players = json.load(file)

            for players in all_players:
                full_name = players['name'] + ' '  + players['surname']
                players_list.append(full_name)

            return players_list

        except:
            print("Player list empty")
            return players_list
        
    def save_new_player(self):
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
