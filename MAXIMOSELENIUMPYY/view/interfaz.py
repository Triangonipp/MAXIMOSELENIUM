from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox, QTextEdit, QLineEdit, QDateEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate
from controller.funcionalidades_interfaz import FuncionalidadesInterfaz
from model.generar_reporte import GenerarReporte
from model.reporte_maximo import ReporteMaximo
from model.reporte_outlook import ReporteOulokk

class Interfaz(QMainWindow,FuncionalidadesInterfaz,GenerarReporte,ReporteMaximo,ReporteOulokk):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reporte Fallas Herramientas")
        self.setGeometry(100, 100, 600, 500)

        self.init_ui()

    def init_ui(self):
        # Crear etiquetas
        self.resize(380, 600)

        titulo_label = QLabel("Reportar Falla", self)
        titulo_label.setGeometry(120, 0, 1000, 30)

        fuente = QFont("Arial", 16)
        titulo_label.setFont(fuente)
        
        usuario_maximo_label = QLabel("USUARIO MAXIMO", self)
        usuario_maximo_label.setGeometry(10, 40, 200, 30)
        
        contraseña_maximo_label = QLabel("CONTRASEÑA MAXIMO", self)
        contraseña_maximo_label.setGeometry(10, 80, 200, 30)

        gestores_herramientas_label = QLabel("GESTORES HERRAMIENTAS", self)
        gestores_herramientas_label.setGeometry(10, 120, 200, 30)
        
        gestores_fallas_label = QLabel("TIPO DE FALLA", self)
        gestores_fallas_label.setGeometry(10, 160, 160, 30)

        descripcion_falla_label = QLabel("DESCRIPCIÓN DE LA FALLA", self)
        descripcion_falla_label.setGeometry(10, 200, 200, 30)

        fecha_falla_label = QLabel("FECHA DE LA FALLA", self)
        fecha_falla_label.setGeometry(10, 240, 240, 30)

        hora_falla_label = QLabel("HORA DE LA FALLA", self)
        hora_falla_label.setGeometry(10, 280, 280, 30)

        elemento_red_label = QLabel("ELEMENTO DE RED", self)
        elemento_red_label.setGeometry(10, 320, 200, 30)

        
        self.usuario_maximo = QLineEdit(self)
        self.usuario_maximo.setGeometry(220, 40, 150, 30)
        
        self.contraseña_maximo = QLineEdit(self)
        self.contraseña_maximo.setEchoMode(QLineEdit.Password)
        self.contraseña_maximo.setGeometry(220, 80, 150, 30)
        
        # Crear opciones y cuadros de texto
        opciones_herramientas = ["NCE-FAN", "AMS NOKIA", "NETNUMEN", "BOSSC", "KOU", "DIAGNOSTICADOR RESIDENCIAL",
                                 "DIAGNOSTICADOR DE NODOS", "TR69 (ACS)", "MODULO DE GESTION", "SECURE CRT",
                                 "PNM PATHTRAK", "RR", "MODULO DE AGENDAMIENTO", "MAXVIEW EQ8096",
                                 "MAXVIEW HARMONIC", "MAXVIEW ROSA VCM", "MAXVIEW ROSA CENTRY","CALIDAD Y GESTIÓN","HIVE - IVR","NETCOOL CMTS", "NETCOOL NODOS" , "NETCOOL OLT", "NETCOOL RPHY" , "NETCOOL SDS","MAXIMO","ROSA","AURORA"]

        self.seleccionar_gestores_herramienta = QComboBox(self)
        self.seleccionar_gestores_herramienta.addItems(opciones_herramientas)
        self.seleccionar_gestores_herramienta.setGeometry(220, 120, 150, 30)
        self.agregar_tooltips_a_combobox(self.seleccionar_gestores_herramienta)

        opciones_fallas = ["Clareo de Alarmas", "Asociación de alarmas fuera de los 15 minutos", "No llegan alarmas",
                           "Falla de automatismo (Llegan alarmas y no se genera INC/OT/TAS)",
                           "Falla de automatismo (No documenta el campo de fechas finalización prevista/fin falla)",
                           "Falla de automatismo (Duplicidad por Automatismos)",
                           "No crea OT/TAS dentro de los tiempos establecidos", "TR69 (ACS)",
                           "Caida total de la plataforma", "Error de Plataforma (Troncal caida pero en estado online en gestor",
                           "Error de plataforma (Inconsistencia en las telemetrias)", "Lentitud en la plataforma"]

        self.seleccionar_gestores_fallas = QComboBox(self)
        self.seleccionar_gestores_fallas.addItems(opciones_fallas)
        self.seleccionar_gestores_fallas.setGeometry(220, 160, 150, 30)
        self.agregar_tooltips_a_combobox(self.seleccionar_gestores_fallas)

        self.descripcion_falla = QLineEdit(self)
        self.descripcion_falla.setGeometry(220, 200, 150, 30)

        self.fecha_falla = QDateEdit(self)
        self.fecha_falla.setGeometry(220, 240, 150, 30)
        self.fecha_falla.setCalendarPopup(True)
        self.fecha_falla.setDate(QDate.currentDate())

        self.combobox_hora = QComboBox(self)
        self.combobox_hora.addItems([str(i).zfill(2) for i in range(24)])
        self.combobox_hora.setGeometry(220, 280, 70, 30)

        self.combobox_minuto = QComboBox(self)
        self.combobox_minuto.addItems([str(i).zfill(2) for i in range(60)])
        self.combobox_minuto.setGeometry(300, 280, 70, 30)

        self.elemento_red = QLineEdit(self)
        self.elemento_red.setGeometry(220, 320, 150, 30)

        limpiar_button = QPushButton("Limpiar", self)
        limpiar_button.setGeometry(8, 360, 90, 30)
        limpiar_button.clicked.connect(lambda: self.limpiar_campos(self))

        guardar_y_copiar_button = QPushButton("Guardar Reporte", self)
        guardar_y_copiar_button.setGeometry(98, 360, 90, 30)
        guardar_y_copiar_button.clicked.connect(lambda: self.generar_reporte(self))

        enviar_reporte_button = QPushButton("Enviar Reporte", self)
        enviar_reporte_button.setGeometry(188, 360, 90, 30)
        enviar_reporte_button.clicked.connect(lambda: self.enviar_reporte_maximo(self)) 
         
        enviar_correos_button = QPushButton("Enviar Correos", self)
        enviar_correos_button.setGeometry(278, 360, 90, 30)
        enviar_correos_button.clicked.connect(lambda: self.guardar_y_enviar_outlook(self))

              
        texto_cont_label = QLabel("Texto cont", self)
        texto_cont_label.setGeometry(160, 390, 150, 30)

        self.texto_cont = QTextEdit(self)
        self.texto_cont.setGeometry(10, 420, 360, 210)
        

        self.reporte_guardado = False

# Instancia de la interfaz
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    interfaz = Interfaz()
    interfaz.show()
    sys.exit(app.exec_())
