import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
# from data.users import USERS
# from data.checkout_data import usuarios_checkou
from utils.helpers import load_user_csv , load_user_json

load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")


# import time
@pytest.mark.parametrize("username, password", load_json)
# @pytest.mark.parametrize("checkout_data",usuarios_checkout )

def test_checkout_sacedemo(driver, username, password):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login(username, password)

    checkout_page.agregar_producto()
    checkout_page.ir_al_carrito()
    checkout_page.iniciar_carrito()
    # assert "cart.html" in driver.current_url
    # time.sleep(3) => esto es opcional , solo para cerrar la ventana de google que estropea el flujo del codigo, al cerrarlo van a poder tener exito en el test, sino va a fallar.
    checkout_page.completar_formulario()
    checkout_page.continuar()
    checkout_page.finish()
    checkout_page.mensaje_exito()
