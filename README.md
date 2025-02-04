# Projeto Docker com Python, SQL e Flask

Este projeto utiliza Docker Compose para orquestrar os containers de um banco de dados MySQL e uma aplicação Python/Flask. Ele visa demonstrar como integrar uma aplicação Python com um banco de dados MySQL usando Docker, simplificando o processo de desenvolvimento e implantação.

## Tecnologias Utilizadas

- **Docker**: Para criar, testar e distribuir a aplicação e o banco de dados em containers.
- **Docker Compose**: Para orquestrar múltiplos containers e simplificar o gerenciamento dos serviços.
- **Python 3.x**: Linguagem de programação para a aplicação web.
- **Flask**: Framework de microserviço para construção da API web.
- **MySQL**: Banco de dados relacional.

## Estrutura do Projeto

- **`docker-compose.yml`**: Arquivo de configuração do Docker Compose que define os serviços (MySQL e Python/Flask).
- **`Dockerfile`**: Arquivo de configuração para a criação da imagem Docker do serviço Python/Flask.
- **`run.py`**: Arquivo de inicialização do Flask.
- **`src/`**: Código-fonte da aplicação Flask.
- **`.env`**: Arquivo para armazenar variáveis de ambiente, como senhas e configurações do banco de dados. **Não se deve versionar este arquivo no GitHub**.
- **`.gitignore`**: Arquivo para ignorar arquivos e diretórios que não devem ser versionados, como o arquivo `.env`.

## Arquitetura do Projeto
A arquitetura do projeto pode ser visualizada no diagrama abaixo:



## Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio 
```
### 2. Configurar as variáveis de ambiente
Crie um arquivo .env no diretório raiz do projeto com o seguinte conteúdo:
```
MYSQL_ROOT_PASSWORD=sua-senha-aqui
```
### 3. Construir e rodar os containers
```
docker-compose up --build
```

### 4. Acessar aplicação Flask
A aplicação Flask estará rodando na porta 3000. Você pode acessá-la no navegador com:
```
http://localhost:3000
```
