import pyautogui
from model.parametros import definir_opciones_escalamiento, definir_correos_mapping, definir_cooreos_copia
import time
import webbrowser
import pyperclip

class ReporteOulokk:
    def guardar_y_enviar_outlook(self, interfaz):
        if (interfaz.reporte_guardado):

            seleccion_gestores = interfaz.seleccionar_gestores_herramienta.currentText()
            correos_mapping = definir_correos_mapping().get(seleccion_gestores, "Opción no reconocida")
            copia_correos = definir_cooreos_copia().get(seleccion_gestores, "Opción no reconocida")
            escalamiento = definir_opciones_escalamiento().get(seleccion_gestores, "Opción no reconocida")
            

            correos_pp = f"{correos_mapping}"

            pyperclip.copy(correos_pp)

            webbrowser.open("https://outlook.office.com/mail/")
            
            time.sleep(2)
            
            pyautogui.hotkey('esc')
            
            time.sleep(3)

            pyautogui.hotkey('n')

            time.sleep(3)

            pyautogui.hotkey("ctrl", "v")

            correos_cc = f"{copia_correos}"
            pyperclip.copy(copia_correos)

            pyautogui.hotkey("tab")

            pyautogui.hotkey("ctrl", "v")

            asunto = f"REPORTE DE FALLA EN LA HERRAMIENTA {seleccion_gestores}"
            pyperclip.copy(asunto)

            pyautogui.hotkey("tab")

            pyautogui.hotkey("ctrl", "v")

            hora_seleccionada = interfaz.combobox_hora.currentText()
            minuto_seleccionado = interfaz.combobox_minuto.currentText()

            texto_completo = f"FOHOG_REPORTE_FALLA_PLATAFORMAS\nGESTORES Y HERRAMIENTAS: {seleccion_gestores}\nESCALAMIENTO: {escalamiento}\nTIPO DE FALLA: {interfaz.seleccionar_gestores_fallas.currentText()}\nDESCRIPCIÓN DE FALLA: {interfaz.descripcion_falla.text()}\nELEMENTO DE RED: {interfaz.elemento_red.text()}\nFECHA FALLA: {interfaz.fecha_falla.text()}\nHORA FALLA: {hora_seleccionada}:{minuto_seleccionado}"

            pyperclip.copy(texto_completo)

            pyautogui.hotkey("tab")

            pyautogui.hotkey("ctrl", "v")

        else:
            interfaz.mostrar_advertencia_reporte_no_guardado()