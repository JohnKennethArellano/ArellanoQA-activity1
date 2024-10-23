import requests
import random
from datetime import datetime, timedelta

class Users():
    
    def api_get_user(self): 
        response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)

        users = response.json()

        for user in users:
            random_days = random.randint(0, 365 * 50)
            randomt_date = datetime(1970, 1, 1) + timedelta(days=random_days)
            user['birthday'] = randomt_date.strftime('%m%d%Y')
            user['address']['state'] = self.get_random_word()
            user['create'] = 'new'
        return users
    
    def get_random_word(self):
        response = requests.get("https://random-word-api.herokuapp.com/word", verify=False)
        return response.json()[0].title()
    

    def get_details(self): 
        response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)

        users = response.json()

        for user in users:
            user['create'] = 'new'
            user['last_seen'] = '22 hours ago'
            user['last_seen'] = '22 hours ago'
            user['last_seen'] = '22 hours ago'
        return users