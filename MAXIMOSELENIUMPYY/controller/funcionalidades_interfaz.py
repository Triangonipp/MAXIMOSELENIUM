from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate

class FuncionalidadesInterfaz:
    def agregar_tooltips_a_combobox(self, combobox):
        for index in range(combobox.count()):
            combobox.setItemData(index, combobox.itemText(index), Qt.ToolTipRole)


    def limpiar_campos(self, interfaz):
        interfaz.seleccionar_gestores_herramienta.setCurrentText("NCE-FAN")
        interfaz.seleccionar_gestores_fallas.setCurrentText("Clareo de Alarmas")
        interfaz.descripcion_falla.clear()
        interfaz.elemento_red.clear()
        interfaz.fecha_falla.setDate(QDate.currentDate())
        interfaz.combobox_hora.setCurrentText("00")
        interfaz.combobox_minuto.setCurrentText("00")
        interfaz.texto_cont.clear()
        interfaz.reporte_guardado = False

    def mostrar_popup(self, title, message):
        popup = QMessageBox(self)
        popup.setWindowTitle(title)
        popup.setText(message)
        popup.exec_()
    
    def mostrar_advertencia_reporte_no_guardado(self):
        mensaje = "Por favor genera el reporte primero."
        self.mostrar_popup("REPORTE NO GENERADO", mensaje)

    def mostrar_mensaje_incompleto(self):
        mensaje = "Por favor complete todos los campos antes de guardar y copiar."
        self.mostrar_popup("Campos incompletos", mensaje)
        
    def mostrar_usuario_contraseña_incompleto(self):
        mensaje = "Por favor ingrese su Usuario y Contraseña antes de enviar el reporte."
        self.mostrar_popup("Campos incompletos", mensaje)