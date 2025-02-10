import re
import csv
from pathlib import Path  

# Defina o caminho da pasta onde os arquivos .txt estão localizados
folder_path = Path(r'C:\Users\eyluc\Documents\ADMIN\estagio\Mineração da dados\Pernalonga_automatizacao\dados_formatados')

# Procura por todos os arquivos .txt na pasta (se precisar de busca recursiva, use rglob('*.txt'))
txt_files = folder_path.glob('*.txt')

# Cria (ou sobrescreve) o arquivo CSV de saída
with open('dataset.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['prompts', 'responses'])  # Escreve o cabeçalho
    
    # Para cada arquivo .txt encontrado
    for txt_file in txt_files:
        # Lê o conteúdo do arquivo
        conteudo = txt_file.read_text(encoding='utf-8')
        # Define a expressão regular para extrair os prompts e responses
        padrao = r'PROMPT:\s*(.*?)\s*/\s*RESPONSE:\s*(.*?)\]'
        # re.DOTALL permite que o ponto (.) corresponda a quebras de linha, se necessário
        matches = re.findall(padrao, conteudo, re.DOTALL)
        
        # Escreve cada par extraído no arquivo CSV
        for prompt, response in matches:
            writer.writerow([prompt.strip(), response.strip()])

print("Arquivo CSV criado com sucesso!")
