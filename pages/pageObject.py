import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, CarritoProductosPageLocators, FormularioOrdenProductosPageLocators, \
    TelefonosPageLocators, PortatilPageLocators, MonitoresPageLocators, DetallesProductoPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):


    def validacionTituloPagina(self):

        return "STORE" in self.driver.title

    def clickHome(self):
        element = self.driver.find_element(*MainPageLocators.LNK_IR_HOME)
        element.click()

    def clickCarrito(self):
        element = self.driver.find_element(*MainPageLocators.LNK_IR_CARRITO)
        element.click()

    def clickCategoriaTelefonos(self):
        element = self.driver.find_element(*MainPageLocators.LNK_CATEGORIA_TELEFONO)
        element.click()

    def clickCategoriaPortatiles(self):
        element = self.driver.find_element(*MainPageLocators.LNK_CATEGORIA_PORTATIL)
        element.click()

    def clickCategoriaMonitores(self):
        element = self.driver.find_element(*MainPageLocators.LNK_CATEGORIA_MONITORES)
        element.click()

class ProductosPage(BasePage):

    def clickTelefonoHtcOneM9(self):
        element = self.driver.find_element(*TelefonosPageLocators.LNK_HTC_ONE_M9)
        element.click()

    def clickPortatilMacbookPro(self):
        element = self.driver.find_element(*PortatilPageLocators.LNK_MACBOOK_PRO)
        element.click()

    def clickMonitorAsusFull(self):
        element = self.driver.find_element(*MonitoresPageLocators.LNK_ASUS_FULLHD)
        element.click()

class DetallesProductoPage(BasePage):

    def clickAñadirProducto(self):
        element = self.driver.find_element(*DetallesProductoPageLocators.BTN_AÑADIR_PRODUCTO)
        element.click()

class CarritoPage(BasePage):

            def validarNuevoProductoCarro(self, cantidad):
                MainPage.clickCarrito(self)
                time.sleep(2)
                table_id = self.driver.find_element(*CarritoProductosPageLocators.TABLA_PRODUCTOS)
                rows = table_id.find_elements(*CarritoProductosPageLocators.FILAS_TABLA_PRODUCTOS)
                return cantidad == len(rows)

            def clickOrdenarProductos(self):
                element = self.driver.find_element(*CarritoProductosPageLocators.BTN_ORDENAR_PRODUCTOS)
                element.click()

            def formularioOrdenes(self, nombre, pais, ciudad, numeroTC, mesTC, añoTC):
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.TXT_NOMBRE)
                    element.send_keys(nombre)
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.TXT_PAIS)
                    element.send_keys(pais)
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.TXT_CIUDAD)
                    element.send_keys(ciudad)
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.TXT_NUMERO_TC)
                    element.send_keys(numeroTC)
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.TXT_MES_TC)
                    element.send_keys(mesTC)
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.TXT_AÑO_TC)
                    element.send_keys(añoTC)
                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.BTN_FINALIZAR_ORDEN)
                    element.click()

                    element = self.driver.find_element(*FormularioOrdenProductosPageLocators.MSG_CONFIRMACION_ORDEN)
                    time.sleep(2)
                    return numeroTC in element.text

class Alertas(BasePage):

    def alertAceptar(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert.accept()

