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

    driver.save_screenshot('screenshot_name1.png')
    
    # Localizar el campo de búsqueda por su atributo 'placeholder'
    search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="¿Qué jugarás hoy?"]')))
    
    # Ingresar "Papa's Scooperia" en el campo de búsqueda y buscar
    search_input.send_keys("Papa's Scooperia")
    search_input.send_keys(Keys.RETURN)
    
    driver.save_screenshot('screenshot_name2.png')
    # Verificar si se encontró el juego
    result = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Papa's Scooperia")))
    print("¡Juego encontrado!: ", result.text)
    driver.save_screenshot('screenshot_name3.png')

    game_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '<a href="/es/g/papas-scooperia" class="I_N3HLb877sRrr2UZJfZ xCChko93rfK8hvsE5sNR DvDiN9SUs6oLdmDamX1x XxuAeockFFccwluXvlEw"><img src="https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=204,height=204,fit=cover,f=auto/7da94623f93b04e8cf801e6a0803fb76.png" srcset="https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=204,height=204,fit=cover,f=auto/7da94623f93b04e8cf801e6a0803fb76.png 1x, https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=408,height=408,fit=cover,f=auto/7da94623f93b04e8cf801e6a0803fb76.png 2x" alt="Papa's Scooperia" loading="eager" decoding="async" width="204" height="204" class="omIThBX9w3QarB_pnFby"><span class="MHaP7Us7V6KqGxb8muHM global-cq-title">Papa's Scooperia</span></a>')
    game_link.click()
    print("¡Juego 'Papa's Scooperia' abierto!")

finally:
    # Cerrar el navegador
    driver.quit()
