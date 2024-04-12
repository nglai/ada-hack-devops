# API de Consulta sobre Animais

Esta API fornece informações sobre uma variedade de animais, incluindo o que comem, com o que gostam de brincar e onde vivem.

**Utilize python versão 3.10 ou superior.**

## Estrutura do Projeto

```plaintext
/pasta-raiz
│
├── /app                    # Pasta principal da aplicação, onde está localizado o código-fonte da API.
│   ├── __init__.py         # Arquivo para tornar este diretório um pacote Python.
│   ├── main.py             # Arquivo principal da aplicação que inicializa a API e inclui as rotas.
│   ├── models.py           # Modelos de dados usados pela API, definidos usando Pydantic.
│   └── /routes             # Diretório contendo as rotas/endpoints da aplicação.
│       ├── __init__.py     # Arquivo para tornar este diretório um pacote Python.
│       └── animal.py       # Arquivo contendo as rotas específicas para operações de animais.
│
├── /tests                  # Pasta contendo os testes para a API.
│   ├── __init__.py         # Arquivo para tornar este diretório um pacote Python.
│   └── test_animal_api.py  # Testes automatizados para as rotas da API.
│
├── .gitignore              # Lista de arquivos e diretórios que o Git deve ignorar.
├── README.md               # Documentação do projeto, detalhando a estrutura e instruções de uso.
└── requirements.txt        # Arquivo listando as dependências necessárias para rodar a aplicação.
```

## Como Rodar a Aplicação

Certifique-se de que você tem Python instalado e siga os passos abaixo:

1. Clone o repositório e navegue até o diretório do projeto.
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv env
   source env/bin/activate  # No Windows use 'env\Scripts\activate'
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

A API estará rodando em `http://127.0.0.1:8000`.

## Documentação da API

Depois de iniciar a aplicação, acesse `http://127.0.0.1:8000/docs` para visualizar a documentação da API Swagger UI, onde você pode testar os endpoints diretamente pelo navegador.
