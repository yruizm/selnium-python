import unittest
from selenium import webdriver
from pages import pageObject
from ddt import ddt, data, unpack

@ddt
class DemoBlazeTestCase(unittest.TestCase):

    #Dado que ingreso a demoblaze
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.assertIn('STORE', self.driver.title)

    #Cuando agrego Prpductos a la compra

    @data(("JUAN PEREZ SOZA", "COLOMBIA", "MEDELLIN", "9807555312612", "12", "32"))
    @unpack
    def test_prodcut_demo_blaze(self, nombre, pais, ciudad, numeroTC, mesTC, añoTC):
        mainPage = pageObject.MainPage(self.driver)
        productPage = pageObject.ProductosPage(self.driver)
        detailsProductPage = pageObject.DetallesProductoPage(self.driver)
        alertMan = pageObject.Alertas(self.driver)
        carritoPage = pageObject.CarritoPage(self.driver)
        self.assertTrue(mainPage.validacionTituloPagina(), "El titulo no coincide.")
        mainPage.clickCategoriaTelefonos()
        productPage.clickTelefonoHtcOneM9()
        detailsProductPage.clickAñadirProducto()
        alertMan.alertAceptar()
        self.assertTrue(carritoPage.validarNuevoProductoCarro(1), "Cantidad con Primer Producto no coincide")

        mainPage.clickHome()
        mainPage.clickCategoriaPortatiles()
        productPage.clickPortatilMacbookPro()
        detailsProductPage.clickAñadirProducto()
        alertMan.alertAceptar()
        self.assertTrue(carritoPage.validarNuevoProductoCarro(2), "Cantidad con Segundo Producto no coincide")

        mainPage.clickHome()
        mainPage.clickCategoriaMonitores()
        productPage.clickMonitorAsusFull()
        detailsProductPage.clickAñadirProducto()
        alertMan.alertAceptar()
        self.assertTrue(carritoPage.validarNuevoProductoCarro(3), "Cantidad con Tercer Producto no coincide")


    #Entonces realizo la finalizacion de la compra
        carritoPage.clickOrdenarProductos()
        self.assertTrue(carritoPage.formularioOrdenes(nombre, pais, ciudad, numeroTC, mesTC, añoTC), "Orden Fallida, Informacion no coincide")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
