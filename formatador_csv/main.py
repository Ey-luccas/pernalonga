import re
import csv
from pathlib import Path  
file_path = Path(r'C:\Users\eyluc\Documents\ADMIN\estagio\Mineração da dados\prompt_extraidoconteudo_eight-great-sacred-sites.txt')
texto = file_path.read_text() 
# Expressão regular para extrair os prompts e responses
padrao = r'PROMPT:\s*(.*?)\s*/\s*RESPONSE:\s*(.*?)\]'

# Encontrar todas as correspondências no texto
matches = re.findall(padrao, texto)
# Criar um arquivo CSV
with open('dataset.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['prompts', 'responses'])  # Escrever o cabeçalho
    for match in matches:
        writer.writerow([match[0], match[1]])  # Escrever cada linha
print("Arquivo CSV criado com sucesso!")