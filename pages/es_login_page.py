from framework.webapp import WebBrowser
from maps.es_login_map import EsLoginMap


class EsLoginPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.es_login_map = EsLoginMap()

    """ Esse metodo realiza login no sistema ES
        
        @param username
        @param password
    """

    def login(self, username, password):
        self.send_keys(self.es_login_map.login_field, username)
        self.send_keys(self.es_login_map.password_field, password)
        self.TakeScreenshot("Login step")
        self.click_on(self.es_login_map.login_button)

    """ Esse metodo verifica se o login foi realizado corretamente
        
        @param username
        @param password
    """

    def is_in_screen(self):
        message = self.wait_element(
            self.es_login_map.login_message, timeout=50)
        return "Login was done!" in message.text
