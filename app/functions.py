import datetime
import re

def clean_category_name(category_name):
    """
    Realiza a limpeza e padronizacao do nome da categoria do produto.
    Aplica letras minusculas, remove espacos extras e elimina caracteres especiais.
    """
    if not category_name or category_name.strip() == "":
        return "Sem Categoria"
    
    # Converte para minusculo e remove espacos nas extremidades
    cleaned = category_name.lower().strip()
    
    # Expressao regular para manter apenas letras, numeros e espacos
    # O sinal ^ dentro de [] significa "negacao", ou seja, substitui o que NAO for alfanumerico ou espaco
    cleaned = re.sub(r"[^\w\s]", "", cleaned)
    
    return cleaned

def handle_physical_dimension(value):
    """
    Trata os valores ausentes de dimensoes fisicas (peso, comprimento, largura, altura).
    
    Justificativa Tecnica: Optou-se por atribuir o valor numerico 0 (zero) para registros nulos.
    Em um pipeline de Machine Learning ou analise estatistica, descartar a linha inteira faria
    com que perdessemos outras metricas validas do produto. Atribuir 0 sinaliza de forma clara
    a ausencia do dado sem quebrar a tipagem numerica flutuante (float) necessaria para calculos.
    """
    if not value or value.strip() == "":
        return 0.0
    
    try:
        return float(value)
    except ValueError:
        return 0.0

def format_approved_date(date_string):
    """
    Converte uma string de data no formato ISO (YYYY-MM-DD HH:MM:SS) 
    para o formato simplificado brasileiro (DD/MM/YYYY).
    """
    if not date_string or date_string.strip() == "":
        return "N/A"
    
    try:
        # Transforma a string original em um objeto datetime do Python
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        # Formata o objeto para o padrao brasileiro desejado
        return parsed_date.strftime("%d/%m/%Y")
    except ValueError:
        # Retorna a string original caso haja falha na conversao por formato incompativel
        return date_string
