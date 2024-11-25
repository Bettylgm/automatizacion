from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

driver = webdriver.Edge() 
wait = WebDriverWait(driver, 10)

reporte = []

def agregar_resultado(prueba, resultado, detalles):
    reporte.append(f"<tr><td>{prueba}</td><td>{resultado}</td><td>{detalles}</td></tr>")

try:
    driver.get("https://poki.com/es")
    logotipo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test='logo']")))
    agregar_resultado("Carga de página principal", "Éxito", "El logotipo está presente.")
except Exception as e:
    agregar_resultado("Carga de página principal", "Fallo", str(e))

try:
    search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Buscar"]')))
    search_button.click()
    search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="¿Qué jugarás hoy?"]')))
    search_input.send_keys("Papa's Scooperia")
    search_input.send_keys(Keys.RETURN)
    resultado = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-root"]/div[1]/section/div[3]/div/div/a[1]')))
    agregar_resultado("Búsqueda de juego existente", "Éxito", f"Juego encontrado: {resultado.text}")
except Exception as e:
    agregar_resultado("Búsqueda de juego existente", "Fallo", str(e))

try:
    search_input.clear()
    search_input.send_keys("JuegoInventado")
    search_input.send_keys(Keys.RETURN)
    no_results = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No se encontraron resultados')]")))
    agregar_resultado("Búsqueda de juego inexistente", "Éxito", "Mensaje de sin resultados mostrado.")
except Exception as e:
    agregar_resultado("Búsqueda de juego inexistente", "Fallo", str(e))

try:
    search_input.clear()
    search_input.send_keys("Papa's Scooperia")
    search_input.send_keys(Keys.RETURN)
    game_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Papa's Scooperia")))
    game_link.click()
    game_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
    agregar_resultado("Navegar a juego", "Éxito", f"Página del juego cargada: {game_title.text}")
except Exception as e:
    agregar_resultado("Navegar a juego", "Fallo", str(e))

try:
    play_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test='play-button']")))
    play_button.click()
    agregar_resultado("Probar botón Jugar", "Éxito", "El botón Jugar funciona correctamente.")
except Exception as e:
    agregar_resultado("Probar botón Jugar", "Fallo", str(e))

driver.quit()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
reporte_path = os.path.join(os.getcwd(), f"reporte_pruebas_{timestamp}.html")

with open(reporte_path, "w", encoding="utf-8") as file:
    file.write("<html><head><title>Reporte de Pruebas</title></head><body>")
    file.write("<h1>Reporte de Pruebas - Poki</h1>")
    file.write("<table border='1'><tr><th>Prueba</th><th>Resultado</th><th>Detalles</th></tr>")
    file.writelines(reporte)
    file.write("</table></body></html>")

print(f"Reporte generado: {reporte_path}")
