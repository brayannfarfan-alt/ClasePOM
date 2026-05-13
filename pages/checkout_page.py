
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    ADD_TO_CART = (By.ID,"add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRT_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_SUCCESS = (By.CLASS_NAME, "complete-header")
    
    
    
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def agregar_producto(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def iniciar_carrito(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def completar_formulario(self,usuario):
        # con esto anda
        self.driver.find_element(*self.FIRT_NAME).send_keys(usuario["first_name"])
        self.driver.find_element(*self.LAST_NAME).send_keys(usuario["last_name"])
        self.driver.find_element(*self.POSTAL_CODE).send_keys(usuario["postal_code"])

        # CON ESTO TAMBIEN Y SERIA MAS PROFESIONAL
        # self.wait.until(
        #     EC.presence_of_element_located(self.FIRT_NAME)
        # ).send_keys(usuario["first_name"])
        # self.wait.until(
        #     EC.presence_of_element_located(self.LAST_NAME)
        # ).send_keys(usuario["last_name"])
        # self.wait.until(
        #     EC.presence_of_element_located(self.POSTAL_CODE)
        # ).send_keys(usuario["postal_code"])


    def continuar(self):
        self.driver.find_element(*self.CONTINUE).click()

    def finish(self):
        self.driver.find_element(*self.FINISH).click()

    def mensaje_exito(self):
        self.driver.find_element(*self.COMPLETE_SUCCESS).click()