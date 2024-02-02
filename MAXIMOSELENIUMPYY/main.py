from PyQt5.QtWidgets import QApplication
from view.interfaz import Interfaz

if __name__ == "__main__":
    app = QApplication([])
    interfaz = Interfaz()
    interfaz.show()
    app.exec_() 
