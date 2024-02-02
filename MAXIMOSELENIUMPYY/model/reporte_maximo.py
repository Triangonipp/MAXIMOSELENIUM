from model.parametros import definir_opciones_escalamiento, definir_num_art_configuracion
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
class ReporteMaximo:
    def enviar_reporte_maximo(self, interfaz):
        seleccion_gestores = interfaz.seleccionar_gestores_herramienta.currentText()
        escalamiento = definir_opciones_escalamiento().get(seleccion_gestores, "Opción no reconocida") 
        num_art_conf = definir_num_art_configuracion().get(seleccion_gestores, "Opción no reconocida") 
        hora_seleccionada = interfaz.combobox_hora.currentText()
        minuto_seleccionado = interfaz.combobox_minuto.currentText()        
        usuario = interfaz.usuario_maximo.text()
        contraseña = interfaz.contraseña_maximo.text()

        if (interfaz.reporte_guardado):
            # Verificar si los campos están llenos
            if usuario.strip() == '' or contraseña.strip() == '':
                interfaz.mostrar_usuario_contraseña_incompleto()
                return

            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-extensions")  

            driver_path = "C:\\Users\aguem\\Downloads\\chromedriver.exe"

            # Iniciar navegador
            driver = webdriver.Chrome(options=options)

            try:
                # Declarar variables de usuario y contraseña
                user_maximo = usuario
                password_maximo = contraseña

                # Construir la URL con las variables
                url = f"http://{user_maximo}:{password_maximo}@100.126.20.133/maximo/ui/login"

                # Abrir la URL
                driver.get(url)

                # Esperar a que aparezca el elemento (puedes ajustar el selector según sea necesario)
                enlace_incidencia_nueva = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "QuickInsert_INCIDENT"))
                )

                # Hacer clic en el enlace "Incidencia nueva"
                enlace_incidencia_nueva.click()

                # Resumen 
                resumen = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "m8672e47c-tb"))
                )
                resumen.send_keys(f"FOHOG_REPORTE_FALLA_PLATAFORMAS {seleccion_gestores}")

                time.sleep(3)
                # Detalles
                # Esperar a que aparezca el elemento iframe
                iframe_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "m1f7bb5c6-rte_iframe"))
                )

                # Cambiar al contexto del iframe
                driver.switch_to.frame(iframe_element)

                div_element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "dijitEditorBody"))
                )
                texto_completo = f"FOHOG_REPORTE_FALLA_PLATAFORMAS. GESTORES_Y_HERRAMIENTAS: {seleccion_gestores}. ESCALAMIENTO: {escalamiento}. TIPO_DE_FALLA: {interfaz.seleccionar_gestores_fallas.currentText()}. DESCRIPCIÓN_DE_FALLA: {interfaz.descripcion_falla.text()}. ELEMENTO_DE_RED: {interfaz.elemento_red.text()}. FECHA_FALLA: {interfaz.fecha_falla.text()}. HORA_FALLA: {hora_seleccionada}:{minuto_seleccionado}."  
                script = f"arguments[0].innerHTML = '{texto_completo}';"
                driver.execute_script(script, div_element)

                # Cambiar de nuevo al contexto principal del navegador
                driver.switch_to.default_content()

                time.sleep(3)
                # Ruta de clasificacion
                ruta = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "mc76799fb-tb"))
                )
                ruta.send_keys("REQUERIMIENTOS INTERNOS \ HOGARES")

                time.sleep(3)

                # Ubicacion 
                ubicacion_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "mad5af16c-tb"))
                )
                ubicacion_input.send_keys("SDS-ORTEZAL")
                time.sleep(2)

                # Articulo de configuracion
                artconfig = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "m43b117ce-tb"))
                )
                artconfig.clear()
                artconfig.send_keys(num_art_conf)
                artconfig.send_keys(Keys.RETURN)
                time.sleep(2)

                # Simular un clic en el elemento
                elemento_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "mdb4f724f-tb"))
                )
                elemento_input.click()

                # Impacto
                impacto = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "m9afef2b2-tb"))
                )
                impacto.clear()
                impacto.send_keys("1")
                impacto.send_keys(Keys.RETURN)
                time.sleep(2)

                # Urgencia
                urgencia = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "m3ecd474c-tb"))
                )
                urgencia.clear()
                urgencia.send_keys("1")
                urgencia.send_keys(Keys.RETURN)
                elemento_a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "m8f3f68c5-tab_anchor"))
                )
                elemento_a.send_keys(Keys.ENTER)

                time.sleep(2)

                # Notas
                elemento_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "madcef749_bg_button_addrow-pb"))
                )
                elemento_button.click()

                time.sleep(2)

                elemento_textarea = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "mdbe533fd-ta"))
                )
                elemento_textarea.clear()
                elemento_textarea.send_keys(f"FOHOG_REPORTE_FALLA_PLATAFORMAS\nGESTORES_Y_HERRAMIENTAS: {seleccion_gestores}\nESCALAMIENTO: {escalamiento}\nTIPO_DE_FALLA: {interfaz.seleccionar_gestores_fallas.currentText()}.\nDESCRIPCIÓN_DE_FALLA: {interfaz.descripcion_falla.text()}\nELEMENTO_DE_RED: {interfaz.elemento_red.text()}\nFECHA_FALLA: {interfaz.fecha_falla.text()}\nHORA_FALLA: {hora_seleccionada}:{minuto_seleccionado}")

                # Bucle para verificar si la ventana sigue abierta
                while True:
                    if not driver.window_handles:  # Si no hay manejadores de ventana, significa que la ventana se cerró
                        break
                    time.sleep(0.1)

            except WebDriverException:
                # WebDriverException puede ocurrir si el usuario cierra manualmente la ventana
                pass

            except Exception as e:
                print(f"Error: {e}")

            finally:
                driver.quit()  # Asegúrate de cerrar el navegador al finalizar

        else:
            interfaz.mostrar_advertencia_reporte_no_guardado()    