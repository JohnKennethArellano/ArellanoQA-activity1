import requests
import random
from datetime import datetime, timedelta

class Users:
    
    def api_get_user(self):
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
            response.raise_for_status()  
            users = response.json()

            for user in users:
                random_days = random.randint(0, 365 * 50)
                random_date = datetime(1970, 1, 1) + timedelta(days=random_days)
                user['birthday'] = random_date.strftime('%Y-%m-%d')  
                user['address']['state'] = self.get_random_word()
                user['create'] = 'new'
                
            return users
        
        except requests.RequestException as e:
            print(f"An error occurred while fetching users: {e}")
            return []  
    
    def get_random_word(self):
        try:
            response = requests.get("https://random-word-api.herokuapp.com/word", verify=False)
            response.raise_for_status()  
            return response.json()[0].title()
        
        except requests.RequestException as e:
            print(f"An error occurred while fetching a random word: {e}")
            return "Unknown"  
