# API_Agenda
# 📘 API de Hábitos

Projeto de uma API RESTful para gerenciamento de hábitos, semelhante a uma agenda, com operações de CRD completas (Create, Read, Delete), escrita com Django REST Framework.

## 🚀 Funcionalidades

- ✅ Criar hábitos
- 📋 Listar todos os hábitos
- ❌ Deletar um hábito específico
- 🧪 Testes automatizados com cobertura básica

## 📦 Endpoints

| Método | Rota           | Descrição                   |
|--------|----------------|-----------------------------|
| GET    | /agenda/       | Lista todos os hábitos      |
| POST   | /agenda/       | Cria um novo hábito         |
| DELETE | /agenda/{id}/  | Remove hábito pelo ID       |

##📁 Tecnologias
-Python 3
-Django
-Django REST Framework
-SQLite (banco de dados padrão)
-Postman (para testes manuais)

## 📄 Exemplo de JSON (POST)

```json
{
  "nome": "Estudar Redes",
  "frequencia": "diario",
  "desc": "Não entendi o que o professor falou",
  "status": "ativo"
}
```
##🛠️ Como rodar o projeto localmente
1. Clone o repositório e acesse a pasta
2. Crie o ambiente virtual (python -m venv venv, depois execute "venv/bin/activate" se estiver no Linux ou MacOS, e "venv\Scripts\activate" se for Windows)
3. instale as dependências
4. rode as migrações (python manage.py migrate)
5. Inicie o servidor e use o postman, a API estará disponivel aqui: http://localhost:8000/agenda/

## 💡 futuras melhoras
-  Adicionar a possibilidade de alterar os dados, o PUT (Update, para completar o CRUD)
- Adicionar HTML,CSS e JS para uma estilização
- Adicionar testes mais completos para campos e valores inválidos
