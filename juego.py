from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Edge()  # Cambia a tu navegador preferido (Chrome, Firefox, etc.)

try:
    # Abrir la página de Poki
    driver.get("https://poki.com/es")
    
    # Esperar hasta que el botón de búsqueda esté presente
    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Buscar"]')))
    
    # Hacer clic en el botón
    search_button.click()
    
    # Localizar el campo de búsqueda por su atributo 'placeholder'
    search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="¿Qué jugarás hoy?"]')))
    
    # Ingresar "Papa's Scooperia" en el campo de búsqueda y buscar
    search_input.send_keys("Papa's Scooperia")
    search_input.send_keys(Keys.RETURN)
    
    # Verificar si se encontró el juego
    result = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Papa's Scooperia")))
    print("¡Juego encontrado!: ", result.text)

    search_input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'By.CLASS_NAME, "I_N3HLb877sRrr2UZJfZ"')))
    search_input.send_keys(Keys.RETURN)
    
finally:
    # Cerrar el navegador
    driver.quit()
