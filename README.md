# Automação de Cadastro de Produtos
Este projeto é uma **automação de cadastro de produtos** desenvolvida 100% em Python, utilizando **PyAutoGUI** para automação de tarefas repetitivas e **Pandas** para leitura e manipulação de dados a partir de arquivos CSV.

O objetivo do projeto é simular e automatizar um processo que normalmente seria feito manualmente por um usuário, economizando tempo e reduzindo erros humanos.



##  Tecnologias Utilizadas

- **Python**
- **PyAutoGUI** – Automação de interações com teclado e mouse
- **Pandas** – Manipulação de dados e leitura de arquivos CSV
- **CSV** – Fonte de dados dos produtos



##  Funcionalidades

- Leitura automática de produtos a partir de um arquivo CSV
- Cadastro automatizado de produtos em um sistema web
- Preenchimento automático de campos como:
  - Código do produto
  - Marca
  - Tipo
  - Categoria
  - Preço unitário
  - Custo
  - Observações
- Simulação fiel de ações humanas (cliques, digitação e navegação)
- Estrutura reutilizável para outros projetos de automação



##  Estrutura do Projeto

```bash
├── codigo.py        # Script principal de automação
├── auxiliar.py      # Funções auxiliares e apoio ao script principal
├── produtos.csv     # Base de dados dos produtos
└── README.md
