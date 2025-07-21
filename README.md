# Arquitetura Padrão MVC com Flask, SQLite e Pydantic

Este projeto demonstra uma arquitetura limpa e escalável utilizando o padrão MVC (Model-View-Controller) em Python, com Flask como framework web, SQLite como banco de dados e Pydantic para validação de dados.

## ✨ Funcionalidades

- **Cadastro e busca de pessoas** com validação de dados.
- **Listagem e remoção de pets**.
- **Validação de requisições** com Pydantic.
- **Tratamento centralizado de erros** e respostas padronizadas.
- **Estrutura modular** e fácil de manter, seguindo boas práticas de arquitetura.

## 🏗️ Tecnologias Utilizadas

- Python 3.11+
- Flask
- Flask-Cors
- SQLAlchemy
- SQLite
- Pydantic
- Pytest (testes)
- Pre-commit + Pylint (qualidade de código)

## 🚀 Como rodar o projeto

1. **Clone o repositório**
   ```bash
   git clone <url-do-repo>
   cd <nome-da-pasta>
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   # Ative no Windows:
   venv\Scripts\activate
   # Ou no Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o servidor**
   ```bash
   python run.py
   ```
   O servidor estará disponível em: [http://localhost:3000](http://localhost:3000)

## 📬 Exemplos de uso (via Postman ou similar)

### Criar pessoa (POST `/people`)
```json
{
  "first_name": "Lucas",
  "last_name": "Silva",
  "age": 25,
  "pet_id": 1
}
```

### Listar pets (GET `/pets`)
Retorna todos os pets cadastrados.

## 🗂️ Estrutura de Pastas

- `src/`
  - `controllers/` — Lógica de negócio (Controllers)
  - `models/` — Modelos e acesso ao banco (ORM)
  - `views/` — Camada de apresentação (Views/Responses)
  - `validators/` — Validação de dados com Pydantic
  - `erros/` — Tratamento e tipos de erros customizados
  - `main/` — Inicialização do servidor e rotas

## 🧪 Testes

Execute todos os testes com:
```bash
pytest
```

## 💡 Aprendizados

- Organização de projetos Python com MVC.
- Validação robusta de dados com Pydantic.
- Boas práticas de tratamento de erros e respostas HTTP.
- Integração de testes e ferramentas de qualidade de código. 