# Mini-Projeto-Avaliativo: Pipeline de Sanitização de Dados (Olist)

## 📝 Descrição do Projeto
Este projeto consiste no desenvolvimento de um pipeline de ETL (Extract, Transform, Load) nativo em Python para limpar e padronizar os datasets públicos da Olist (`olist_products_dataset.csv` e `olist_orders_dataset.csv`). O objetivo principal é remover inconsistências, tratar dados nulos e formatar campos temporais sem a utilização da biblioteca Pandas, garantindo a integridade dos relatórios automatizados da empresa.

## 🚀 Guia de Execução
1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. Garanta que os arquivos de dados estejam na pasta correta:
   - `data/olist_products_dataset.csv`
   - `data/olist_orders_dataset.csv`

4. Execução em Sistemas UNIX (Linux / macOS)
Abra o terminal na raiz do projeto e execute o seguinte comando:
```bash
python3 app/app.py

5. Execução no Windows (Prompt de Comando ou PowerShell)
Abra o terminal (CMD ou PowerShell) na raiz do projeto e execute o seguinte comando:
```cmd
python app\app.py

### 💡 OBS: Este projeto utiliza apenas as bibliotecas nativas do Python. Nenhuma instalação externa será necessária.