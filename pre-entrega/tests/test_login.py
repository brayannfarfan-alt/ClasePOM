from pages.login_page import LoginPage
from data.users import USERS
from utils.helpers import load_user_csv , load_user_json
import pytest
from faker import Faker # pip install faker


load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")
fake = Faker()

@pytest.mark.parametrize("username, password", USERS)
def test_login( driver, username, password ):
    # LoginPage(driver).open()
    # LoginPage(driver).login(username,password)

    login_page = LoginPage(driver)
    

    login_page.open()
    login_page.login(username, password)

    assert False

#     name = fake.name()       
#     first_name = fake.first_name()   
#     last_name = fake.last_name()   
#     email = fake.email()
#     codigo_postal = fake.postalcode()

#     print("DATOS GENERADOS POR FAKER",name,first_name,last_name,email,codigo_postal)
    


# @pytest.mark.parametrize("i",range(3)) #=> [0,1,2,3,4]
# def test_login_usuario_invalido(driver,i):
#     login_page = LoginPage(driver)

#     fake_username = fake.user_name()
#     fake_password = fake.password()
    
#     login_page.open()
#     login_page.login(fake_username, fake_password )

#     assert "Epic sadface" in login_page.obtener_error()