class View:
    def welcome_message(self):
        print("--- Welcome in Chess Manager ---")
    
    def finish_message(self):
        print("--- See you next time ---")

    def display_menu(self):
        print("\nMain Menu:")
        print(" [A] Players 👤")
        print(" [B] Tournament 🏆")
        print(" [C] Statistics 📊")
        print(" [Q] Quit ❌")
        reponse = input("Your choice: ")
        return reponse
    
    def display_players_menu(self):
        print(" [A] Add Players ➕")
        print(" [R] Return ⬅️")
        reponse = input("Your choice: ")
        return reponse

    def get_new_player_inputs(self):
        print("\n--- Add a new player ---")
        
        nom = input("Last Name: ")
        prenom = input("First Name: ")
        age = input("Age: ")
        ine = input("INE: ")

        return {"name": nom, "surname": prenom, "age": age, "ine": ine}
    
    def error(self, message):
        print(message)

    def success(self, message):
        print(message)