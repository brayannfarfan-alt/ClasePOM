from pages.login_page import LoginPage
from data.users import USERS
from utils.helpers import load_user_csv , load_user_json
import pytest
from faker import Faker


load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")
fake = Faker()

@pytest.mark.parametrize("username, password", load_json)
def test_login( driver, username, password ):
    # LoginPage(driver).open()
    # LoginPage(driver).login(
    #     "standard_user",
    #     "secret_sauce"
    # )

    login_page = LoginPage(driver)
    

    login_page.open()
    login_page.login(username, password)

    name = fake.name()       
    first_name = fake.first_name()   
    last_name = fake.last_name()   
    email = fake.email()
    codigo_postal = fake.postalcode()

    print("DATOS GENERADOS POR FAKER",name,first_name,last_name,email,codigo_postal)
    




