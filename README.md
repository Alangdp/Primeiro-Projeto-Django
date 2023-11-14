# Projeto Django de Revenda Simples com Sistema de Login e Chat Bot usando API GPT

## Descrição do Projeto

Este é um projeto inicial Django em Python que simula uma aplicação de revenda simples. O projeto inclui um sistema de autenticação para usuários, permitindo que eles acessem recursos exclusivos. Além disso, integra um chat bot utilizando a API GPT-3 para interações mais inteligentes e dinâmicas.

## Funcionalidades

1. **Sistema de Login:**
   - Página de login para autenticação de usuários.
   - Página de registro para novos usuários.
   - Recuperação de senha para usuários esquecidos.

2. **Revenda Simples:**
   - Página inicial com produtos em destaque.
   - Catálogo de produtos com informações detalhadas.
   - Carrinho de compras para seleção de produtos.
   - Processo de checkout básico.

3. **Chat Bot com API GPT:**
   - Integração com a API GPT-3 para um chat bot inteligente.
   - Respostas dinâmicas e contextuais para perguntas dos usuários.
   - Suporte a comandos específicos, como informações sobre produtos, ajuda no processo de compra, etc.

## Configuração do Ambiente

1. **Pré-requisitos:**
   - Python 3.x instalado.
   - Pipenv instalado (opcional, mas recomendado).

2. **Configuração do Ambiente Virtual (usando Pipenv):**
   ```bash
   pipenv install
   pipenv shell

## Pré-requisitos

- Python 3.x instalado.
- Pipenv instalado (opcional, mas recomendado).

## Como Iniciar

1. **Configuração do Ambiente Virtual (usando Pipenv):**
    ```bash
    pipenv install
    pipenv shell
    ```

2. **Aplicar Migrações do Banco de Dados:**
    ```bash
    python manage.py migrate
    ```

3. **Executar o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

    O servidor estará disponível em [http://localhost:8000/](http://localhost:8000/).

## Configuração da API GPT-3

1. **Obtenha uma Chave de API da OpenAI GPT-3:**
    - Visite [https://beta.openai.com/signup/](https://beta.openai.com/signup/) para se inscrever no programa beta da OpenAI e obter uma chave de API.

2. **Configure a Chave no Projeto:**
    - Abra o arquivo `settings.py` e insira sua chave da API GPT-3 na variável `GPT3_API_KEY`.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
