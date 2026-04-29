# DEX — Developer Explorer ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) 

Plataforma de pesquisa técnica para desenvolvedores com IA local.
Pesquise conceitos de programação e receba respostas estruturadas com explicação, código e contexto de uso. Todas as pesquisas ficam salvas no seu histórico pessoal.

Projeto que pode ficar mais robusto conforme uso de IA paga para prompts mais dinâmicos e adaptativos deixando o software mais versátil.

## Tecnologias

- Python / Django
- LangChain + Ollama (IA local, sem custo)
- Mistral (modelo de linguagem)
- SQLite

## Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com/download) instalado na máquina

## Instalação

1. Clone o repositório
\```bash
git clone https://github.com/gattini0928/DEX
cd DEX
\```

2. Crie e ative o ambiente virtual
\```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
\```

3. Instale as dependências
\```bash
pip install -r requirements.txt
\```

4. Configure as variáveis de ambiente — crie um arquivo `.env` na raiz:
\```env
SECRET_KEY=sua_secret_key_django
DEBUG=True
\```

5. Rode as migrações
\```bash
python manage.py migrate
\```

6. Baixe o modelo de IA
\```bash
ollama pull mistral
\```

7. Inicie o servidor
\```bash
python manage.py runserver
\```

Acesse em `http://localhost:8000`

## Funcionalidades

- Cadastro e login de usuários
- Pesquisa técnica com IA local (sem custo, sem API key)
- Respostas estruturadas: O que é, Como funciona, Código Exemplo e Quando usar
- Histórico de pesquisas por usuário
- Filtro por tags de tecnologia (Go, Python, SQL, Docker...)

## Como usar

1. Crie sua conta
2. Digite um tópico de programação no campo de busca
3. A IA retorna uma resposta estruturada e salva no seu histórico
4. Acesse seu perfil para ver e filtrar pesquisas anteriores

## Licença

MIT
