#**INTRODUCCIÓN**
Proyecto Selenium + Python


Detalles generales de la implementación:

+ Herramienta de automatización: PyCharm 2022.2.4 (Community Edition)
+ Compilador:  Python
+ Patrón de diseño:  POM


Prerequisitos:

+ Tener instalado y verificar su funcionamiento:
+ PyCharm 2022.2.4 (Community Edition) o superior.
+ python y variables de entorno configurada
+ pip  y variables de entorno configurada 
+ Tener GIT en su ultima versión.

Plugins implementados:

+ selenium
+ ddt (DATA DRIVEN)
+ pytest-html (Reportes de prueba HTML)

Escenario: Compra de Productos en DemoBlaze
Dado que ingreso a demoblaze
Cuando agrego Productos a la compra
Entonces realizo la finalizacion de la compra


Para ejecutar la automatización se abre la consola en la raíz del proyecto, y se pone el comando:

###python -m pytest -v  --html=reports/report.html DemoBlazeTestCase.py

###pytest -v  --html=reports/report.html DemoBlazeTestCase.py


## Autor ##
Yefri Ruiz Mosquera
