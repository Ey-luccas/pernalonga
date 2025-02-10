#Verificar se o texto tem mais de mil, se tiver vai dividir por dois, se não, vai deixar do jeito que está. 
    # Prompt: para o deepseek 
from pathlib import Path  
caminho = r'C:\Users\eyluc\Documents\ADMIN\estagio\Mineração da dados\Pernalonga_automatizacao\coletador\extração_nekhor\conteudo_sacred-foothills-rivers-and-caves.txt'
file_path = Path(caminho)
text_enter = file_path.read_text() 
text_formatado = text_enter.replace("\n", "").replace("\r", "")
palavras = text_formatado.split()
text = ' '.join(palavras)
prompt_text = []
if len(text) >= 500:
    # p1 = text[:len(text)//2]  
    # p2 = text[len(text)//2:]
    # prompt_text.append(p1)
    # prompt_text.append(p2)
    # print(prompt_text)
    parte_tamanho = len(text) // 4
    # Divide o texto em 4 partes
    p1 = text[:parte_tamanho]
    p2 = text[parte_tamanho:2 * parte_tamanho]
    p3 = text[2 * parte_tamanho:3 * parte_tamanho]
    p4 = text[3 * parte_tamanho:]
    # Adiciona as partes à lista
    prompt_text.append(p1)
    prompt_text.append(p2)
    prompt_text.append(p3)
    prompt_text.append(p4)
else: 
    prompt_text.append(text)
prompt_extraido = []
      #Função que vai verificar se a página está aberta 
def verification(): 
   try:
    element = driver.find_element(By.XPATH, "//input[@type='text' and contains(@class, 'ds-input__input')]")
    return True
   except:
    return False
def extrair_nome_arquivo(caminho):
    partes = caminho.split('\\')
    nome_arquivo = partes[-1]
    nome_sem_extensao = nome_arquivo.split('.')[0]
    return nome_sem_extensao
parte_extraida = extrair_nome_arquivo(caminho)
print(parte_extraida)
print(len(prompt_text))
        #Loop que vai rodar e pegar os dados e enviar
for i in range(len(prompt_text)):
        #Dependências e configuração do SELENIUM
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
  prompt_instruct = f'Isso é um texto, não se preocupe.Quero que você faça um texto que vai ser estilo csv, vou usar pra transforma em csv e colocar num llm de pergunta e resposta, faça quantas quiser, quero que faça sentido, use seu conhecimento de linguagem natural pra não fica estranho e mais humano possivel mas sempre passando informações importante pro llm, um index vai ser divido por [], primeiro o prompt e segundo response de acordo com o texto, não precisa fazer tabela, só um texto direto com / pra dividir as duas colunas, o formato que quero é assim [primeiro index: PROMPT: texto / RESPONSE: texto], e assim vai:{str(prompt_text[i])}' 
  print(f"Formatação do prompt: {prompt_instruct} ")
  try: 
      if i > 0 :  #verificar se esse código já foi rodado
         time.sleep(10)
      driver.get("https://chat.deepseek.com/sign_in")
      time.sleep(8)
      while True:
          v = verification()
          if v == True:
            break 
          driver.refresh()  
          time.sleep(8)
          # Login eyluccas@outlook.com lucasoliveiraalmeida658@gmail.com
      driver.find_element(By.XPATH, "//input[@type='text' and contains(@class, 'ds-input__input')]").send_keys("eyluccas@outlook.com")
      driver.find_element(By.XPATH, "//input[@type='password' and contains(@class, 'ds-input__input')]").send_keys("1980Luca$")
      driver.find_element(By.XPATH, "//div[contains(@class, 'ds-checkbox-label')]").click()
      driver.find_element(By.XPATH, "//div[@role='button' and contains(@class, 'ds-button--primary')]").click()
      time.sleep(5)
          # Realiza as buscas
      # 1. Localiza o campo de entrada
      driver.find_element(By.ID, "chat-input").send_keys(prompt_instruct + Keys.RETURN)
      time.sleep(10)
          # Captura o resultado
      try: 
        time.sleep(50) # 1 min timeout para ver o resultados
        paragrafos = driver.find_element(By.XPATH, "//div[contains(@class, 'ds-markdown ds-markdown--block')]").find_elements(By.TAG_NAME, "p")
        for paragrafo in paragrafos:
          prompt_extraido.append(paragrafo.text)
      except:
        print('''AVISO: Nenhum parágrafo encontrado. 
              Verifique o XPATH, possivel error''')
        time.sleep(2)
  finally:
    print("Tudo indo bem por enquanto")
    driver.quit()
# Estrutura para Baixar a list(prompt_extraido) para arquivo.text
nome_arquivo = f"prompt_extraido{parte_extraida}.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for item in prompt_extraido :
        arquivo.write(item + "\n")  
print(f"Lista salva com sucesso no arquivo: {nome_arquivo}")
