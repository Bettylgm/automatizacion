from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def take_screenshot(driver, step_name):
    """Función para tomar una captura de pantalla."""
    driver.save_screenshot(f'{step_name}.png')

# Configuración del navegador
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    # Caso 1: Abrir la página principal
    driver.get("https://poki.com/es")
    take_screenshot(driver, "case1_step1_open_home")
    print("Caso 1: Página principal cargada con éxito.")
    
    # Caso 2: Buscar un juego
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Buscar"]')))
    search_button.click()
    take_screenshot(driver, "case2_step1_search_button_clicked")
    
    search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="¿Qué jugarás hoy?"]')))
    search_input.send_keys("Papa's Scooperia")
    search_input.send_keys(Keys.RETURN)
    take_screenshot(driver, "case2_step2_game_searched")
    print("Caso 2: Juego buscado con éxito.")
    
    # Caso 3: Verificar que el juego está en los resultados
    game_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/es/g/papas-scooperia']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", game_link)
    take_screenshot(driver, "case3_step1_game_visible")
    print("Caso 3: El juego está visible en los resultados.")

    # Caso 4: Abrir el juego
    game_link.click()
    take_screenshot(driver, "case4_step1_game_opened")
    print("Caso 4: El juego se abrió con éxito.")

    # Caso 5: Verificar la carga del juego
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "game-container")))  # Selector ajustado según sea necesario.
    take_screenshot(driver, "case5_step1_game_loaded")
    print("Caso 5: La interfaz del juego cargó correctamente.")

except Exception as e:
    print(f"Error durante la ejecución: {e}")

finally:
    driver.quit()
