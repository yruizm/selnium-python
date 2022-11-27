from selenium.webdriver.common.by import By

class MainPageLocators(object):

    LNK_CATEGORIA_TELEFONO = (By.LINK_TEXT, 'Phones')
    LNK_CATEGORIA_PORTATIL = (By.LINK_TEXT, 'Laptops')
    LNK_CATEGORIA_MONITORES = (By.LINK_TEXT, 'Monitors')

    LNK_IR_HOME = (By.XPATH, "//a[contains(text(), 'Home')]")
    LNK_IR_CARRITO = (By.XPATH, "//a[contains(text(), 'Cart')]")

class TelefonosPageLocators(object):

    LNK_HTC_ONE_M9 = (By.LINK_TEXT, 'HTC One M9')
    LNK_SONY_XPERIA_Z5 = (By.LINK_TEXT, 'Sony xperia z5')

class PortatilPageLocators(object):

    LNK_MACBOOK_PRO = (By.LINK_TEXT, 'MacBook Pro')
    LNK_SONY_VAIO_I7 = (By.LINK_TEXT, 'Sony vaio i7')

class MonitoresPageLocators(object):
    LNK_APPLE_MONITOR = (By.LINK_TEXT, 'Apple monitor 24')
    LNK_ASUS_FULLHD = (By.LINK_TEXT, 'ASUS Full HD')

class DetallesProductoPageLocators(object):

    BTN_AÑADIR_PRODUCTO = (By.XPATH, "//a[contains(text(),'Add to cart')]")

class CarritoProductosPageLocators(object):

        TABLA_PRODUCTOS = (By.ID, "tbodyid")
        FILAS_TABLA_PRODUCTOS = (By.TAG_NAME, "tr")
        BTN_ORDENAR_PRODUCTOS = (By.XPATH, "//button[contains(text(), 'Place Order')]")



class FormularioOrdenProductosPageLocators(object):

    TXT_NOMBRE = (By.ID, "name")
    TXT_PAIS = (By.ID, "country")
    TXT_CIUDAD = (By.ID, "city")
    TXT_NUMERO_TC = (By.ID, "card")
    TXT_MES_TC = (By.ID, "month")
    TXT_AÑO_TC = (By.ID, "year")
    BTN_FINALIZAR_ORDEN = (By.XPATH, "//button[contains(text(), 'Purchase')]")
    MSG_CONFIRMACION_ORDEN = (By.XPATH, "//*[@class='lead text-muted ']")

pass