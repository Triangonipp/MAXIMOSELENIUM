
import pyperclip
from model.parametros import definir_opciones_escalamiento

class GenerarReporte:
    def generar_reporte(self, interfaz):
        if (interfaz.seleccionar_gestores_herramienta.currentText() and
            interfaz.seleccionar_gestores_fallas.currentText() and
            interfaz.descripcion_falla.text() and
            interfaz.elemento_red.text() and
            interfaz.fecha_falla.text() and
            interfaz.combobox_hora.currentText() and
            interfaz.combobox_minuto.currentText()):

            seleccion_gestores = interfaz.seleccionar_gestores_herramienta.currentText()
            escalamiento = definir_opciones_escalamiento().get(seleccion_gestores, "Opción no reconocida")  

            hora_seleccionada = interfaz.combobox_hora.currentText()
            minuto_seleccionado = interfaz.combobox_minuto.currentText()


            texto_completo = f"FOHOG_REPORTE_FALLA_PLATAFORMAS\nGESTORES Y HERRAMIENTAS: {seleccion_gestores}\nESCALAMIENTO: {escalamiento}\nTIPO DE FALLA: {interfaz.seleccionar_gestores_fallas.currentText()}\nDESCRIPCIÓN DE FALLA: {interfaz.descripcion_falla.text()}\nELEMENTO DE RED: {interfaz.elemento_red.text()}\nFECHA FALLA: {interfaz.fecha_falla.text()}\nHORA FALLA: {hora_seleccionada}:{minuto_seleccionado}"

            interfaz.texto_cont.clear()
            interfaz.texto_cont.insertPlainText(texto_completo)
            pyperclip.copy(texto_completo)
        else:
            interfaz.mostrar_mensaje_incompleto()
        interfaz.reporte_guardado = True
