import requests
from bs4 import BeautifulSoup

def extrair_parte_da_url(url):
    # Divide a URL pelas barras '/'
    partes = url.split('/')
    
    # Pega a última parte, que é o que vem depois da última barra
    parte_final = partes[-1]
    
    # Remove caracteres inválidos para nome de arquivo
    parte_final = "".join(c for c in parte_final if c.isalnum() or c in ('-', '_'))
    
    return parte_final

def extrair_conteudo(url, parte_extraida):
    try:
        # Faz a requisição HTTP para a URL
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção se a requisição falhar
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return
    
    # Parseia o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lista para armazenar o conteúdo extraído
    conteudo = []
    
    # Extrai todos os títulos (h1, h2, h3) e parágrafos
    for elemento in soup.find_all(['h1', 'h2', 'h3', 'p']):
        if elemento.name in ['h1', 'h2', 'h3']:
            # Se for um título, adiciona ao conteúdo
            conteudo.append(f"\n{elemento.text.upper()}\n")
        elif elemento.name == 'p':
            # Se for um parágrafo, adiciona ao conteúdo
            conteudo.append(elemento.text)
    
    # Junta todo o conteúdo em uma única string
    conteudo_completo = "\n".join(conteudo)
    
    # Define o nome do arquivo
    nome_arquivo = f"conteudo_{parte_extraida}.txt"
    
    # Salva o conteúdo em um arquivo .txt
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_completo)
    
    print(f"Conteúdo extraído e salvo em '{nome_arquivo}'")

# Exemplo de uso
urls = ['https://www.lotsawahouse.org/topics/abhidharma/', ]
for urluni in urls: 
    url = urluni
parte_extraida = extrair_parte_da_url(url)
extrair_conteudo(url, parte_extraida)