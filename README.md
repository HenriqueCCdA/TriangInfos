# TriangInfos

Projeto extremamente simples que calcula a área de Triangulo. Objetivo é apenas o integrar o `FastAPI`, `Vue` e `Docker`.

O frontend foi criado usando `vue`, `pinia` e `vuetify`. Como ferramentas de desenvolvimento temos foi `eslint`, `prettier` e `vite`.

Backend foi criado utilizando o `FastAPI`. O servidor de aplicação é `gunicorn + uvicorn`. Como ferramentas de desenvolvimento temos `black`, `ruff`, `taskipy` e `pytest`.

## Desenvolvimento local

Comandos para o desenvolvimento local sem docker.

### Frontend

Entrando na pasta do front

```bash
cd src/frontend
```

Instalando as dependencias

```bash
npm install
```

Subindo o servidor de desenvolvimento

```bash
npm run dev
```

Para formatar o codigo com `prettier`

```bash
npm run format
```

Para chamara o linter `ESlint`

```bash
npm run lint
```

### Backend

Entrando na pasta do backend

```bash
cd src/backend
```

Instalando as dependencias

```bash
poetry install --no-root
```

Subindo o servidor de desenvolvimento

```bash
poetry run task server
```

Para formatar o código com `black` e `ruff`

```bash
poetry run task fmt
```

Para o linter com `mypy` e `ruff`

```bash
poetry run task lint
```

Mais opções do `taskipy`

```bash
poetry run task -l
```

## Docker

Comandos para o desenvolvimento local com docker.

Gerando as imagens

```bash
docker compose build
```

Subindo os containers

```bash
docker compose up
```

Rodando os testes no `backend`

```bash
docker compose run backend task test
```

Entrando no container do `backend`

```bash
docker compose run backend bash
```

Para formatar o codigo com `prettier`

```bash
docker compose run frontend npm run format
```

Para chamara o linter `ESlint`

```bash
docker compose run frontend npm run lint
```
