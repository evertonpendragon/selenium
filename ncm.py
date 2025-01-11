from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time


# Configura o driver do navegador (neste exemplo, Chrome)

driver = webdriver.Chrome()


list_gtin=[7896003739374,7894900011517,7892840800079,7896843200201,7892840800567]



# Abre o site desejado

driver.get('https://cosmos.bluesoft.com.br/produtos/')


for gtin in list_gtin:

    # Localiza o elemento de entrada pelo ID

    search_input = driver.find_element(By.ID, 'search-input')

    time.sleep(1)

    # Envia o código de barras para o elemento de entrada

    search_input.send_keys(gtin)

    time.sleep(1)

    # Opcional: envia a tecla Enter para iniciar a pesquisa

    search_input.send_keys(Keys.RETURN)

    time.sleep(1)



    # Aguarda a página carregar e o elemento desejado estar presente

    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.description.ncm-name.label-figura-fiscal a')))


    # Extrai o texto do elemento

    element_text = element.text


    # Obtém o código do texto extraído

    codigo = element_text.split(' - ')[0]


    print(f"Produto: {gtin}\t NCM: {codigo}")

    time.sleep(1)



# Aguarda alguns segundos para ver o resultado (opcional)


time.sleep(50)


# Fecha o navegador

driver.quit()
