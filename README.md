# Mini-Projeto-Avaliativo: Pipeline de Sanitização de Dados

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
python3 app/app.py```

5. Execução no Windows (Prompt de Comando ou PowerShell)
Abra o terminal (CMD ou PowerShell) na raiz do projeto e execute o seguinte comando:
```cmd
python app\app.py```

### 💡 OBS: Este projeto utiliza apenas as bibliotecas nativas do Python. Nenhuma instalação externa será necessária.

## 🧠 Reflexão Teórica: Qualidade de Dados e Machine Learning

No desenvolvimento de Inteligência Artificial, existe uma regra de ouro: *"Lixo Entra, Lixo Sai"* (do inglês, *Garbage In, Garbage Out*). Isso significa que um modelo de Machine Learning é como um aluno: ele só aprende bem se o material de estudo for bom. Se alimentarmos a IA com dados bagunçados, incompletos ou cheios de erros, as previsões dela também serão ruins.

Quando os dados contêm muitas falhas (como valores nulos ou textos despadronizados), o algoritmo fica confuso e tenta encontrar lógica onde não existe, o que gera dois grandes problemas. O primeiro é o **Overfitting (Superajuste)**, no qual a IA acaba "decorando" os erros e as imperfeições da base de treino, parecendo perfeita nos testes, mas falhando drasticamente ao lidar com situações do mundo real. O segundo são os **Vieses**, que ocorrem quando o modelo aprende padrões errados, gerando decisões automatizadas distorcidas que podem prejudicar diretamente o negócio.

Por isso, a etapa de limpeza que desenvolvemos neste projeto é o coração de qualquer sistema inteligente. Ao padronizar os textos e tratar os valores vazios de forma consciente, garantimos que a IA aprenda apenas padrões reais e seguros. O resultado são previsões confiáveis e prontas para funcionar perfeitamente mesmo em dias de acessos extremos, como na Black Friday.