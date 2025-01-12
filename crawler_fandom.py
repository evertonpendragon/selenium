#pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def extract_text_from_page(url):
    try:
        # Faz a requisição para obter o conteúdo da página
        response = requests.get(url)
        response.raise_for_status()  # Garante que não houve erro na requisição

        # Cria o objeto BeautifulSoup para análise do HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove elementos com a classe 'thumb tright show-info-icon'
        for element in soup.find_all(class_="thumb tright show-info-icon"):
            element.decompose()

        for element in soup.find_all(class_="toc"):
            element.decompose()

        for element in soup.find_all(class_="trfc161"):
            element.decompose()

        for element in soup.find_all(class_="ad-slot-placeholder incontent-leaderboard is-loading"):
            element.decompose()

        # Define as tags a serem extraídas
        tags_to_extract = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p','dl']

        # Encontra e extrai o texto das tags especificadas
        extracted_text = []
        sopinha = soup.find_all(tags_to_extract)

        for element in soup.find_all(tags_to_extract):
            if element.name in tags_to_extract:
                extracted_text.append(element.get_text(strip=False))

        return extracted_text

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []

# URL da página a ser extraída
url = "https://warhammer40k.fandom.com/wiki/Fulgrim"

# Extrai o texto
text_content = extract_text_from_page(url)

# Salva o conteúdo extraído em um arquivo de texto
with open("text.txt", "w", encoding="utf-8") as file:
    for line in text_content:
        file.write(line + "\n")

print("Conteúdo salvo em 'text.txt'")
