<h1 align="center">Gerenciador de clientes de eventos</h1>
<p align="center">Sistema para prestadores de serviços em eventos gerenciar seus clientes e orçamentos</p>

## Sobre
Este sistema foi criado para avaliação para entrar em um projeto acadêmico no IFRN.
### Tecnologias
![Static Badge](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Static Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Static Badge](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)

## Instalação
Clone o repositório
```shell
git clone https://github.com/devwenderson/django-gestao-eventos.git
```

Execute o docker compose
```shell
docker compose up
```

## Execução

### Como funciona
- Os faturamentos são gerados quando o orçamento é criado. A quantidade de faturas é passada como parâmetro do orçamento.

### Rotas e JSON's
#### Clientes
##### POST
```json
{
    "nome": "Adriano",
    "telefone": "(84) 91234-5678"
}
```
##### GET
```json
{
    "id": 1,
    "nome": "Adriano",
    "telefone": "(84) 91234-5678",
    "eventos": [
        {
            "nome": "Amor no céu",
            "local": "Avenida Salgado Filho",
            "status": "pendente",
            "data_inicio": "2026-02-10",
            "data_fim": "2026-02-12"
        }
    ]
}
```
- `GET /api/clientes/` - Listar clientes
- `POST /api/clientes/` - Cadastrar cliente
- `GET /api/clientes/<id>` - Detalhar cliente
- `DELETE /api/clientes/<id>` - Deletar cliente
- `PUT /api/clientes/<id>` - Atualizar cliente

#### Eventos
##### POST
```json
{
	"nome": "Amor no céu",
	"cliente": 1,
	"data_inicio": "2026-02-10",
	"hora_inicio": "13:30",
	"data_fim": "2026-02-12",
	"hora_fim": "14:00",
	"status": "pendente",
	"local": "Avenida Salgado Filho"
}
```
##### GET
```json
{
    "id": 2,
    "nome": "Amor no céu",
    "cliente": "adriano",
    "data_inicio": "2026-02-10",
    "hora_inicio": "13:30:00",
    "data_fim": "2026-02-12",
    "hora_fim": "14:00:00",
    "status": "pendente",
    "local": "Avenida Salgado Filho"
}
```
- `GET /api/eventos/` - Listar eventos
- `POST /api/eventos/` - Cadastrar evento
- `GET /api/eventos/<id>` - Detalhar evento
- `DELETE /api/eventos/<id>` - Deletar evento
- `PUT /api/eventos/<id>` - Atualizar evento

#### Orçamentos
##### POST
```json
{
	"evento": 2,
	"valor": 5000.00,
	"status": "pendente",
	"numero_faturamentos": 5
}
```
##### GET
```json
{
    "id": 1,
    "evento": {
        "nome": "Amor no céu",
        "cliente": "adriano",
        "data_inicio": "2026-02-10",
        "data_fim": "2026-02-12"
    },
    "faturamentos": [
        {
            "id": 1,
            "orcamento": 1,
            "valor": "1000.00",
            "status": "em andamento",
            "data_vencimento": "2025-09-06",
            "data_pagamento": null
        },
        {
            "id": 2,
            "orcamento": 1,
            "valor": "1000.00",
            "status": "em andamento",
            "data_vencimento": "2025-10-06",
            "data_pagamento": null
        },
        {
            "id": 3,
            "orcamento": 1,
            "valor": "1000.00",
            "status": "em andamento",
            "data_vencimento": "2025-11-06",
            "data_pagamento": null
        },
        {
            "id": 4,
            "orcamento": 1,
            "valor": "1000.00",
            "status": "em andamento",
            "data_vencimento": "2025-12-06",
            "data_pagamento": null
        },
        {
            "id": 5,
            "orcamento": 1,
            "valor": "1000.00",
            "status": "em andamento",
            "data_vencimento": "2026-01-06",
            "data_pagamento": null
        }
    ],
    "valor": "5000.00",
    "data_criacao": "2025-08-06",
    "status": "pendente",
    "numero_faturamentos": 5
}
```
- `GET /api/orcamentos/` - Listar orcamentos
- `POST /api/orcamentos/` - Cadastrar orcamento
- `GET /api/orcamentos/<id>` - Detalhar orcamento
- `DELETE /api/orcamentos/<id>` - Deletar orcamento
- `PUT /api/orcamentos/<id>` - Atualizar orcamento

#### Faturamentos
##### GET
```json
{
    "id": 1,
    "orcamento": 1,
    "valor": "1000.00",
    "status": "em andamento",
    "data_vencimento": "2025-09-06",
    "data_pagamento": null
}
```
- `GET /api/orcamentos/` - Listar orcamentos
  

## Referências
- [Para criar diagrama do banco de dados](https://drawsql.app/)
- [Django](https://docs.djangoproject.com/en/5.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Instalação do Docker](https://docs.docker.com/engine/install/)
- [Uso efetivo de serializers](https://testdriven.io/blog/drf-serializers/)