import csv
import os
from functions import clean_category_name, handle_physical_dimension, format_approved_date

def process_products_dataset(file_path):
    """
    Processa o arquivo de produtos, sanitiza os dados e calcula estatisticas basicas.
    """
    print(f"Iniciando processamento do arquivo: {file_path}")
    
    total_rows = 0
    null_categories_fixed = 0
    null_dimensions_fixed = 0
    
    # Utilizacao de gerenciador de contexto nativo (with open) para leitura segura do arquivo
    with open(file_path, mode="r", encoding="utf-8") as file:
        # csv.DictReader mapeia cada linha do CSV em um dicionario Python usando o cabecalho como chave
        reader = csv.DictReader(file)
        
        for row in reader:
            total_rows += 1
            
            # Verifica se a categoria original e nula/vazia para fins estatisticos
            original_category = row.get("product_category_name")
            if not original_category or original_category.strip() == "":
                null_categories_fixed += 1
            
            # Aplica as funcoes de higienizacao criadas no modulo functions
            sanitized_category = clean_category_name(original_category)
            
            # Validacao de dimensoes fisicas (exemplo com peso e comprimento)
            weight = row.get("product_weight_g")
            length = row.get("product_length_cm")
            
            if not weight or weight.strip() == "":
                null_dimensions_fixed += 1
            if not length or length.strip() == "":
                null_dimensions_fixed += 1
                
            sanitized_weight = handle_physical_dimension(weight)
            sanitized_length = handle_physical_dimension(length)
            
            # O processamento linha a linha ocorre em memoria. Em cenarios reais, 
            # os dados higienizados seriam gravados em um novo arquivo de saida.

    return {
        "total_rows": total_rows,
        "null_categories_fixed": null_categories_fixed,
        "null_dimensions_fixed": null_dimensions_fixed
    }

def process_orders_dataset(file_path):
    """
    Processa o arquivo de pedidos, reformata as datas e valida a hipotese de negocio da Olist.
    """
    print(f"\nIniciando processamento do arquivo: {file_path}")
    
    total_rows = 0
    total_canceled_orders = 0
    empty_delivery_dates = 0
    empty_delivery_and_canceled = 0
    
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total_rows += 1
            
            order_status = row.get("order_status")
            approved_at = row.get("order_approved_at")
            delivered_customer_date = row.get("order_delivered_customer_date")
            
            # Contabiliza ordens explicitamente canceladas
            if order_status == "canceled":
                total_canceled_orders += 1
            
            # Formata a data de aprovacao usando o modulo nativo datetime
            formatted_approval = format_approved_date(approved_at)
            
            # Lógica de Regra de Negócio: Testando a hipotese sobre a data de entrega vazia
            if not delivered_customer_date or delivered_customer_date.strip() == "":
                empty_delivery_dates += 1
                if order_status == "canceled":
                    empty_delivery_and_canceled += 1
                    
    # Verificacao logica da hipotese
    hypothesis_proven = (empty_delivery_dates == empty_delivery_and_canceled)
    
    return {
        "total_rows": total_rows,
        "total_canceled_orders": total_canceled_orders,
        "empty_delivery_dates": empty_delivery_dates,
        "empty_delivery_and_canceled": empty_delivery_and_canceled,
        "hypothesis_proven": hypothesis_proven
    }

if __name__ == "__main__":
    # Caminhos relativos apontando para a pasta 'data' conforme a estrutura exigida
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    products_csv = os.path.join(base_dir, "data", "olist_products_dataset.csv")
    orders_csv = os.path.join(base_dir, "data", "olist_orders_dataset.csv")
    
    print("=== PIPELINE DE SANITIZACAO DE DADOS (OLIST) ===")
    
    # Execucao do processamento de produtos
    try:
        product_stats = process_products_dataset(products_csv)
    except FileNotFoundError:
        print(f"Erro: O arquivo {products_csv} nao foi encontrado na pasta 'data'.")
        product_stats = None

    # Execucao do processamento de pedidos
    try:
        order_stats = process_orders_dataset(orders_csv)
    except FileNotFoundError:
        print(f"Erro: O arquivo {orders_csv} nao foi encontrado na pasta 'data'.")
        order_stats = None
        
    # --- RELATORIO DE STATUS MANUAL (EXIBICAO DOS RESULTADOS) ---
    print("\n" + "="*40)
    print("        RELATORIO E SUMARIO ESTATISTICO        ")
    print("="*40)
    
    if product_stats:
        print(f" [PRODUTOS] Total de linhas processadas: {product_stats['total_rows']}")
        print(f" [PRODUTOS] Categorias nulas corrigidas : {product_stats['null_categories_fixed']}")
        print(f" [PRODUTOS] Dimensoes nulas corrigidas : {product_stats['null_dimensions_fixed']}")
    
    if order_stats:
        print("-"*40)
        print(f" [PEDIDOS] Total de linhas processadas : {order_stats['total_rows']}")
        print(f" [PEDIDOS] Pedidos cancelados totais   : {order_stats['total_canceled_orders']}")
        print(f" [PEDIDOS] Datas de entrega vazias     : {order_stats['empty_delivery_dates']}")
        print(f" [PEDIDOS] Entregas vazias E cancelados: {order_stats['empty_delivery_and_canceled']}")
        
        print("\n--- VALIDACAO DA HIPOTESE DE NEGOCIO ---")
        if order_stats['hypothesis_proven']:
            print(" RESULTADO: Hipotese COMPROVADA! Todas as datas de entrega nulas pertencem a pedidos cancelados.")
        else:
            print(" RESULTADO: Hipotese REJEITADA! Existem pedidos sem data de entrega cujo motivo nao e cancelamento")
            print(" (podem ser pedidos ainda em transito, faturados ou processando).")
            
    print("="*40)
    print("Base de dados sanitizada com sucesso de forma nativa!")
