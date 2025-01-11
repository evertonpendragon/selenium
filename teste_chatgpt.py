from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Carregar o conteúdo do arquivo input.txt
with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Separar o conteúdo pelo caractere '§'
sections = content.split('§')

# Configuração do Selenium e inicialização do navegador
options = webdriver.ChromeOptions()



# Conectar-se a uma janela de navegador previamente aberta
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Porta do debugger

# Substitua 'path_to_chromedriver' pelo caminho correto do seu ChromeDriver
#driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=options)
#driver = webdriver.Chrome(executable_path='"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"', options=options)
driver = webdriver.Chrome(options=options)
#options.add_argument("--start-maximized")





try:
    # Abrir a URL do ChatGPT (substitua pela URL correta)
    #driver.get("https://chatgpt.com/g/g-p-678262d318e08191be6602396bf29dba-narrador/c/674fd392-cd60-800e-8810-14d2902d20c0")
    #time.sleep(5)
    if "chatgpt.com" not in driver.current_url:
        raise Exception("Certifique-se de que a janela do navegador já está na página do ChatGPT.")


    # Aguarde o carregamento completo da página
    time.sleep(5)  # Ajuste conforme necessário

    for index, section in enumerate(sections):
        print(f"Enviando trecho {index + 1}/{len(sections)}")

        # Localizar o campo de entrada do prompt (substitua pelo seletor correto)
        prompt_box = driver.find_element(By.ID, "prompt-textarea")

        # Enviar o texto no campo de entrada
        prompt_box.send_keys(section)
        time.sleep(30)
        prompt_box.send_keys(Keys.RETURN)

        # Aguarde a resposta (ajuste o tempo conforme necessário ou use um método mais robusto)
        time.sleep(180)

    print("Todos os trechos foram enviados.")

finally:
    # Fechar o navegador
    driver.quit()
