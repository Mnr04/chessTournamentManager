import json
import os

class JsonManager:
    @staticmethod
    def load_data(file_path):
        if not os.path.exists(file_path):
            return [] 
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, ValueError):
            return []

    @staticmethod
    def save_data(file_path, data):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)