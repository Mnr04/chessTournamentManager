from view import View
from models import Player

class Controller:
    def __init__(self):
        self.view = View()

    def run(self):
        while True:
            self.view.welcome_message()
            response = self.view.display_menu()

            if response == "A":
                self.players_menu()
                
            elif response == "D":
                 self.view.finish_message()
                 break
            
    def players_menu(self):
        response_display_players_menu = self.view.display_players_menu()
        if response_display_players_menu == "A":
            new_player = self.create_new_player()
        if response_display_players_menu == "R":
            self.view.display_menu()
        return new_player
            

    def create_new_player(self):
        player_data = self.view.get_new_player_inputs()

        try:
            nom = player_data["name"]
            prenom = player_data["surname"]
            age_str = player_data["age"]
            ine_str = player_data["ine"]

            if not nom or not prenom or not age_str or not ine_str:
                self.view.error("Name, surname, age, and INE cannot be empty.")
                return 

            age = int(age_str) 
            ine = int(ine_str)

        except ValueError:
            self.view.error(f"Error: The age '{age_str}' or INE '{ine_str}' is not a valid number.")
            return

        try:
            new_player = Player(surname=prenom, name=nom, age=age, ine=ine)
            new_player.save_new_player() 
            
            self.view.success(f"Player {nom} {prenom} saved successfully!")
            
        except Exception as e:
            self.view.error(f"Error while saving the player: {e}")

   

       
           