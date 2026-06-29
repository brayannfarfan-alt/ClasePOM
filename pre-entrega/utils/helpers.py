from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json

options = Options()

def get_driver():
    service = Service(ChromeDriverManager().install())
    optiuons.add_argument("--headless")
    driver = webdriver.Chrome(service=service)

    
    
    return driver



def load_user_csv( path ):
    users = []

    with open(path, newline="") as file:
        reader = csv.DictReader(file)

        # {
        #     "username":"",
        #     "password":""
        # }

        for row in reader:
            if row["username"] and row["password"]:
                users.append((row["username"],row["password"])) 
                
    return users


def load_user_json( path ):
    users = []

    with open(path) as file:
        data = json.load(file)

        for user in data:
            users.append((user["username"],user["password"]))

    return users
