from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

from pathlib import Path  
file_path = Path(r'C:\Users\eyluc\Documents\ADMIN\estagio\Mineração da dados\Pernalonga_automatizacao\coletador\extração_nekhor\conteudo_eight-great-sacred-sites.txt')
text = file_path.read_text()  # Transformar o texto em uma lista de caracteres text_list = list(text)
o = []
o.append(text)
print(type(o))
text_extraido = []
#PROMPT: para o deepseek
termo = f"Quero que você faça um texto que vai ser estilo csv, vou usar pra transforma em csv e colocar num llm de pergunta e resposta, faça quantas quiser, quero que faça sentido, use seu conhecimento de linguagem natural pra não fica estranho e mais humano possivel mas sempre passando informações importante pro llm, um index vai ser divido por [], primeiro o prompt e segundo response de acordo com o texto, não precisa fazer tabela, só um texto direto com / pra dividir as duas colunas, o formato que quero é assim [primeiro index: PROMPT: texto / RESPONSE: texto], e assim vai: {str(o)} "

# termo = "Me de uma seguência de 5 números dentro 1 a 100"
try:
    driver.get("https://chat.deepseek.com/sign_in")
    time.sleep(10)

    # Login
    driver.find_element(By.XPATH, "//input[@type='text' and contains(@class, 'ds-input__input')]").send_keys("lucasoliveiraalmeida658@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password' and contains(@class, 'ds-input__input')]").send_keys("1980Luca$")
    driver.find_element(By.XPATH, "//div[contains(@class, 'ds-checkbox-label')]").click()
    driver.find_element(By.XPATH, "//div[@role='button' and contains(@class, 'ds-button--primary')]").click()
    time.sleep(5)
    # Realiza as buscas
    driver.find_element(By.ID, "chat-input").send_keys(termo + Keys.RETURN)
    time.sleep(10)

        # Captura o resultado
    try:
      time.sleep(100)
      # Encontre o elemento div e todos os parágrafos dentro dele
      paragrafos = driver.find_element(By.XPATH, "//div[contains(@class, 'ds-markdown ds-markdown--block')]").find_elements(By.TAG_NAME, "p")

            # Itera sobre todos os parágrafos e imprime o texto
      for paragrafo in paragrafos:
        print(f"Texto encontrado: {paragrafo.text}")
        text_extraido.append(paragrafo.text)

    except:
      print("Nenhum parágrafo encontrado.")
      time.sleep(2)

finally:
    time.sleep(10)
    print(text_extraido.index)
    driver.quit()

