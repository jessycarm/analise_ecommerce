# Análise de Ecommerce

Este repositório contém a estrutura inicial de um projeto de análise de dados focado em **ecommerce**, com ênfase na qualidade dos dados e na organização do fluxo de trabalho.

## Estrutura do Projeto

analise_ecommerce/
├── data/ # Dados utilizados nas análises (não versionados)
├── notebooks/ # Notebooks Jupyter para exploração e análise de dados
├── reports/ # Relatórios gerados e visualizações finais
├── src/ # Scripts e funções auxiliares para processamento de dados
├── .gitignore # Arquivos e pastas ignorados pelo Git
├── README.md # Descrição do projeto


## Objetivos

- **Qualidade dos dados**: identificação e tratamento de duplicatas, devoluções e valores ausentes.
- **Organização modular**: estrutura de pastas clara para facilitar manutenção e expansão do projeto.
- **Boas práticas**: utilização de `.gitignore` para ignorar arquivos temporários e ambientes virtuais.

⚙️ Etapas do Projeto

1.  Coleta de Dados
- Base de e-commerce obtida do Kaggle.

2. Tratamento e Limpeza (Python + Pandas)
- Correção de tipos de dados (datas, preços, IDs).
- Substituição de valores ausentes.
- Criação de colunas derivadas (order_year, order_month, order_dayofweek, order_hour).

3.Análise Exploratória (Python)
- Verificação de dados faltantes.
- Identificação de devoluções (is_return).

4. Visualização (Power BI)
- Dashboard interativo com os principais indicadores:
   * Receita Total
   * Volume de Vendas
   * Taxa de Devolução
   * Distribuição de clientes conhecidos x desconhecidos
   * Novo: Percentual de Devolução por Produto 📊

📊 Destaques do Dashboard

- KPIs no topo: visão rápida de receita, vendas e devoluções.
- Tendência temporal: receita por mês/ano.
- Comportamento do cliente: vendas por dia da semana e por hora.
- Top 10 produtos: mais vendidos e mais devolvidos.
- Gráfico de Percentual de Devolução por Produto: identifica produtos problemáticos com maior índice de devolução.

🚀 Tecnologias Utilizadas

- Python (Pandas, NumPy, Matplotlib)
- Power BI (ETL, DAX, dashboards interativos)
- Git & GitHub (versionamento e portfólio)

💡 Próximos Passos:

- Expandir a análise para categorias de produto.
- Melhorar storytelling do dashboard para tomada de decisão.

## Como usar

1. **Clonar o repositório**:

git clone https://github.com/jessycarm/analise_ecommerce.git
cd analise_ecommerce

2. **Criar e ativar ambiente virtual (opcional, recomendado)**:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. **Instalar dependências (se houver requirements.txt)**:

pip install -r requirements.txt


**Observações

- A pasta data/ contém exemplos ou dados já tratados; dados grandes reais não estão versionados.
- Use a pasta reports/ para armazenar relatórios ou gráficos finais.
- A pasta src/ é destinada a scripts reutilizáveis de limpeza, transformação e análise de dados.


**Licença
Este projeto está sob a licença MIT – veja o arquivo LICENSE
para detalhes.









