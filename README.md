# Curso de FastAPI do ZERO com o 🦖 Dunossauro
FastAPI é um framework Python moderno, projetado para simplicidade, velocidade e eficiência. A combinação de diversas funcionalidades modernas do Python como anotações de tipo e suporte a concorrência, facilitando o desenvolvimento de APIs.

# Aula 01 Configurando o Ambiente de Desenvolvimento
## Configurando o Ambiente de Desenvolvimento

Verificando a instalação do Python.
~~~shell
python --version
~~~

Instalação do pyenv no Windows, recomendo usar o pyenv-windows.
~~~shell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
~~~

Após o pyenv-windows instalado, verificar qual versão do python deseja e instale.
~~~shell
pyenv update
pyenv install 3.12:latest
~~~

Definiar uma versão global do Python.
~~~shell
pyenv global 3.12.x
~~~

Instalação de ferramentas recomendadas.
~~~shell
pip install pipx
~~~

~~~shell
pipx install poetry
~~~

Após o poetry instalado é necessário executar o comando abaixo, feche e reabra o terminal:
~~~shell
pipx ensurepath
~~~

~~~shell
pipx install ignr
~~~

## Criação do Projeto FastAPI e Instalação das Dependências
Entrar no diretório onde criará o projeto.
~~~shell
cd C:\projetos\projetos-GIT\
~~~

Criando o projeto.
~~~shell
poetry new fast_zero_v2
~~~

Entrar no projeto.
~~~shell
cd fast_zero_v2
~~~

Definir qual a versão do Python será utilizada nesse projeto/diretório. O script abaixo criará um arquivo que contém a versão do Python.
~~~shell
pyenv local 3.12.4
~~~

Esse comando criará um arquivo oculto chamado `.python-version` na raiz do projeto.

Configurar o arquivo `pyproject.toml`.
[...]

Crie o ambiente virtual do projeto.
~~~shell
poetry install
~~~

Instalando a biblioteca Python do FastAPI.
~~~shell
poetry add fastapi
~~~

## Primeira Execução de um "Hello, World!"
Criação do app.
~~~shell
echo > fast_zero_v2/app.py
~~~
[melhorar esta criação pelo terminal]


Acessando e codificando no app.
~~~shell
code fast_zero_v2/app.py
~~~
[... codificando ...]

Executar a função pelo terminal em modo interativo para chamar a função.
~~~shell
python -i .\fast_zero_v2\app.py
~~~

Depois execute a função para obter o resultado.
~~~shell
>>> read_root()
~~~

[... codificando ...]

Antes de iniciar a aplicação, habilitar o ambiente virtual, para que o python consiga enxergar as dependências instaladas.
~~~shell
poetry shell
~~~

## Testando o ambiente: iniciar nosso servidor FastAPI para iniciar nossa aplicação
~~~shell
fastapi dev fast_zero_v2/app.py
~~~

## Instalando + ferramentas de desenvolvimento
~~~shell
poetry add --group dev pytest pytest-cov taskipy ruff httpx
~~~

Após a instalação das ferramentas de desenvolvimento, precisamos definir as configurações de cada uma individualmente no arquivo `pyproject.toml`.
[... atentar para os nomes dos projetos que influencia neste arqvuivo ...]


Após arquivo configurado, pode testar os comandos criados para o taskipy:
~~~shell
task lint
~~~

~~~shell
task format
~~~

~~~shell
task lint
~~~

## Introdução ao Pytest: Testando o "Hello, World!"
~~~shell
task test
~~~

Gera um relatório de cobertura de testes em formato HTML. Pode abrir esse arquivo no navegador e entender exatamente quais linhas do código não estão sendo testadas.
~~~shell
coverage html
~~~

### Escrevendo o teste
Criação dos arquivos de teste.
~~~shell
echo > tests/test_app.py
~~~
[...]

~~~shell
task test
~~~

Por não coletar nenhum teste, o pytest ainda retornou um "erro". Para ver a cobertura, precisaremos executar novamente o post_test manualmente:
~~~shell
task post_test
~~~

### Criando nosso repositório no git

[... deu muito ruim nessa parte do git, refazer outro projeto com cuidado]

Criar um arquivo `.gitignore` para não adicionar o ambiente virtual e outros arquivos desnecessários no versionamento de código.
~~~shell
ignr -p python > .gitignore
~~~

Criar um novo repositório no Git local para versionar o código e definir a branch main como padrão.
~~~shell
git init -b main
~~~


Para criar um repositório remoto no GitHub externo caso não exista.
~~~shell
gh repo create
~~~


#### Respostas do gh
- Create a new repository on GitHub from scratch
- fast_zero_sync_v2
- Código das aulas aprendidas no curso do Dunossauro (FASTAPI)
- Public
- N
- N
- y
- GNU General Public License v3.0
- Y
- Y

~~~shell
git remote add origin https://github.com/LuizPerciliano/fast_zero_sync_v2.git
~~~

~~~shell
git pull origin main
~~~

~~~shell
git add .
~~~

~~~shell
git commit -m "Configuração inicial do projeto"
~~~

~~~shell
git push
~~~

[... deu muito ruim nessa parte do git, refazer outro projeto com cuidado]



# Aula 02 Introdução ao desenvolvimento WEB

## Usando o fastapi na rede local
~~~shell
fastapi dev fast_zero_v2/app.py --host 0.0.0.0
~~~

ou com o comando abaixo para o mesmo resultado
~~~shell
task run --host 0.0.0.0
~~~

Assim, você pode acessar a aplicação de outro computador na sua rede usando o endereço IP da sua máquina.

Descobrindo o ip local no Windows
~~~shell
ipconfig
~~~

Descobrindo o seu endereço local usando python pelo interpretador
~~~shell
python
~~~

~~~python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
s.getsockname()[0]
~~~


Agora basta acessar a aplicação pelo endereço: http://192.168.0.5:8000/, ficando acessível também por outras máquinas dentro dessa rede, assim como o celular.

[... desenvolvendo e incrementando o projeto ...]


Criando novo arquivo para testes e aprendizado de endpoints.
~~~shell
type nul > fast_zero_v2/aula_00.py
~~~

Abrir o arquivo `fast_zero_v2/aula_00.py` e copiar o script abaixo.
~~~python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
~~~

Executar o arquivo específico.
~~~shell
fastapi dev fast_zero_v2/aula_00.py
~~~

## Pydantic
~~~shell
echo > fast_zero_v2/schemas.py
~~~

[... desenvolvendo e incrementando o projeto ...]


# Aula 03 Estruturando o Projeto e Criando Rotas CRUD
## Implementando endpoints

### Rota do POST
Arquivo `fast_zero_v2/app.py`.
~~~python
@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user():
    ...
~~~

### Modelo de dados
Arquivo `fast_zero_v2/schemas.py`.
~~~python
class UserSchema(BaseModel):
    username: str
    email: str
    password: str
~~~

[... desenvolvendo e incrementando o projeto ... estudar mais esta aula]

## Validação e pydantic

Validação de email
Instalando + ferramentas de desenvolvimento 
~~~shell
poetry add "pydantic[email]"
~~~

## Criando um banco de dados falso


### Não se repita (DRY)
Arquivo `tests/conftest.py`.

~~~shell
echo > tests/conftest.py
~~~

## Implementando a Rota GET


## Implementando a Rota PUT

## Implementando a Rota DELETE

# Aula 04 Configurando o Banco de Dados e Gerenciando Migrações com Alembic

Instalando + ferramentas de desenvolvimento 
~~~shell
poetry add sqlalchemy
~~~

~~~shell
poetry add pydantic-settings
~~~

Agora definiremos nosso modelo User. No diretório fast_zero, crie um novo arquivo chamado models.py e incluiremos o seguinte código no arquivo:

~~~shell
echo > fast_zero_v2/models.py
~~~
[...]

## Testando as Tabelas
Criaremos uma fixture para a conexão com o banco de dados chamada session no arquivo `tests/conftest.py`.
[...]

### Criando um Teste para a Nossa Tabela
Agora, no arquivo test_db.py, escreveremos um teste para a criação de um usuário. Este teste adiciona um novo usuário ao banco de dados, faz commit das mudanças, e depois verifica se o usuário foi devidamente criado consultando-o pelo nome de usuário. Se o usuário foi criado corretamente, o teste passa. Caso contrário, o teste falha, indicando que há algo errado com nossa função de criação de usuário.

~~~shell
echo > tests/test_db.py
~~~
[...]

#### Executando o teste

~~~shell
exit
~~~

~~~shell
task format
~~~

~~~shell
task test
~~~

O ideal é ter pelo menos dois terminais ativos, um para rodar a aplicação e outro para os testes e demais comandos.
~~~shell
task run
~~~

## Configuração do ambiente do banco de dados
~~~shell
echo > fast_zero_v2/settings.py
~~~
[...]

Agora, definiremos o DATABASE_URL no nosso arquivo de ambiente .env. Crie o arquivo na raiz do projeto e adicione a seguinte linha:
~~~shell
echo > .env
~~~
[...]

~~~shell
echo 'database.db' >> .gitignore
~~~

## Instalando o Alembic e Criando a Primeira Migração
~~~shell
poetry add alembic
~~~

Após a instalação do Alembic, precisamos iniciá-lo em nosso projeto. O comando de inicialização criará um diretório migrations e um arquivo de configuração alembic.ini:
~~~shell
alembic init migrations
~~~

### Criando uma migração automática
Com o Alembic devidamente instalado e iniciado, agora é o momento de gerar nossa primeira migração. Mas, antes disso, precisamos garantir que o Alembic consiga acessar nossas configurações e modelos corretamente. Para isso, faremos algumas alterações no arquivo migrations/env.py.
[...]

Para criar a migração, utilizamos o seguinte comando:
~~~shell
alembic revision --autogenerate -m "create users table"
~~~

### Analisando a migração automática
Vamos abrir e analisar o arquivo de migração `migrations/versions/f3577cecc9f1_create_users_table.py`.

~~~shell
code migrations/versions/f3577cecc9f1_create_users_table.py
~~~

Vamos acessar o console do sqlite e verificar se isso foi feito. Precisamos chamar sqlite3 nome_do_arquivo.db ou usar uma aplicativo que abre diversos tipos de banco de dados como o DBeaver:
~~~shell
sqlite3 database.db
~~~
[...]


Para aplicar as migrações, usamos o comando upgrade do CLI Alembic. O argumento head indica que queremos aplicar todas as migrações que ainda não foram aplicadas:
~~~shell
alembic upgrade head
~~~
[...]


Agora, se examinarmos nosso banco de dados novamente:
[...]

## Commit
Primeiro, verificaremos o status do nosso repositório para ver as mudanças que fizemos:
~~~shell
git status
~~~

~~~shell
git add . 
~~~

![alt text](image.png)

~~~shell
git commit -m "Adicionada a primeira migração com Alembic. Criada tabela de usuários."
~~~

~~~shell
git push
~~~


# Aula 05 Integrando Banco de Dados a API
Para isso, criaremos a função get_session e também definiremos Session no arquivo `database.py`.
~~~shell
echo > .\fast_zero_v2\database.py
~~~

## Modificando o Endpoint POST /users
[...]

### Testando o Endpoint POST /users com Pytest e Fixtures
Alteraremos a nossa fixture client para substituir a função get_session que estamos injetando no endpoint pela sessão do banco em memória que já tínhamos definido para banco de dados.
[...]

Dá erro, logo ...
[...]


## Modificando o Endpoint GET /users
[...]
### Testando o Endpoint GET /users
[...]
### Criando uma fixture para User
[...]

### Integrando o Schema ao Model
ajustando o arquivo `fast_zero/schemas.py` <p>
[...]

## Modificando o Endpoint PUT /users
[...]

### Adicionando o teste do PUT
[...]

## Modificando o Endpoint DELETE /users
[...]
### Adicionando testes para DELETE
[...]


## Atualizando o repositório - Commit
Primeiro, verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Revisando as aulas com um novo projeto criado.Atualizando endpoints para usar o banco de dados real."
git push
~~~



# Aula 06 Autenticação e Autorização com JWT
## Gerando tokens JWT
Para gerar tokens JWT, precisamos de duas bibliotecas extras: pyjwt e pwdlib. A primeira será usada para a geração do token, enquanto a segunda será usada para criptografar as senhas dos usuários. Para instalá-las, execute o seguinte comando no terminal:
~~~shell
poetry add pyjwt "pwdlib[argon2]"
~~~

Agora, criaremos uma função para gerar nossos tokens JWT. Criaremos um novo arquivo para gerenciar a segurança: security.py. Nesse arquivo iniciaremos a geração dos tokens:

~~~shell
echo > .\fast_zero_v2\security.py
~~~

## Testando a geração de tokens
~~~shell
echo > .\tests\test_security.py
~~~

## Modificando o endpoint de POST para encriptar a senha
[...]

### Sobre o teste da POST /users/


## Modificando o endpoint de atualização de usuários

## Criando um endpoint de geração do token
### Utilizando OAuth2PasswordRequestForm
~~~shell
poetry add python-multipart
~~~

### Criando um endpoint de geração do token
[...]

### Testando /token

## Protegendo os Endpoints
[...]


### Aplicação da proteção ao endpoint

## Atualizando os Testes



## Atualizando o repositório - Commit
Caso seja um repositório de desenvolvimento compartilhado, verificar se no repositório remoto há algo novo e pedir para baixar.
~~~shell
git pull
~~~

Verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Revisando as aulas com um novo projeto criado. Aula 06. Protege os endpoints PUT e DELETE com autenticação"
git push
~~~




# Aula 07 Refatorando a Estrutura do Projeto

## Criando Routers
Criaremos inicialmente uma nova estrutura de diretórios chamada routers dentro do seu projeto fast_zero. Aqui, teremos subaplicativos dedicados a funções específicas, como gerenciamento de usuários e autenticação.

├── fast_zero  
│  ├── app.py  
│  ├── database.py  
│  ├── models.py  
│  ├── routers  
│  │  ├── auth.py  
│  │  └── users.py  

### Implementando um Router para Usuários
~~~shell
mkdir routers
~~~

~~~shell
echo > fast_zero_v2\routers\users.py
~~~

### Criando um router para Auth
~~~shell
echo > fast_zero_v2\routers\auth.py
~~~


O comando abaixo deu erro, verificar*
~~~shell
task serve
~~~

#### Alteração no teste do token
Arquivo `tests/test_app.py`



## Plugando as rotas em app

## Reestruturando os arquivos de testes

### Ajustando os testes para Auth
~~~shell
echo > tests\test_auth.py
~~~


### Ajustando os testes para User
~~~shell
echo > tests\test_users.py
~~~


#### Executando os testes
~~~shell
task test
~~~


Resolver o trauma abaixo*
![alt text](image-1.png)



## Refinando a Definição de Rotas com Annotated

## Movendo as constantes para variáveis de ambiente

### Adicionando as constantes a Settings

### Removendo as constantes do código

## Testando se tudo funciona
~~~shell
task test
~~~

erro, meu Swagger não aparece usuários, verificar*
![alt text](image-2.png)

## Atualizando o repositório - Commit
Caso seja um repositório de desenvolvimento compartilhado, verificar se no repositório remoto há algo novo e pedir para baixar.
~~~shell
git pull
~~~

Verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Refatorando estrutura do projeto: Criado routers para Users e Auth; movido constantes para variáveis de ambiente." 
git push 
~~~



# Aula 08 Tornando o sistema de autenticação robusto

## Testes para autenticação

### Testando a alteração de um usuário não autorizado

#### Criando modelos por demanda com factory-boy

O factory-boy é uma biblioteca que nos permite criar objetos de modelo de teste de forma rápida e fácil. Com ele, podemos criar uma "fábrica" de usuários que produzirá novos objetos de usuário sempre que precisarmos. Isso nos permite criar múltiplos usuários de teste com facilidade, o que é perfeito para nosso cenário atual.

~~~shell
poetry add --group dev factory-boy
~~~

Executando os testes abaixo em diante, o meu deu erro em alguns, logo, os testes seguintes não foi possível avaliar, verificar* (No final copiei tudo e vi que um arquivo precisava estar diferente, porém preciso rever sobre o token, pois isso está quebrando meus testes)

![alt text](image-3.png)


### Testando o DELETE com o usuário errado


### Testando a expiração do token


### Testando o usuário não existente e senha incorreta


#### Testando a exceção para um usuário inexistente


#### Testando a exceção para uma senha incorreta



## Implementando o refresh do token



~~~shell
poetry add --group dev freezegun
~~~


## Atualizando o repositório - Commit
Caso seja um repositório de desenvolvimento compartilhado, verificar se no repositório remoto há algo novo e pedir para baixar.
~~~shell
git pull
~~~

Verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Implementando o refresh do token e testes de autorização." 
git push --set-upstream origin main 
~~~


# Aula 09 Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI
## Criando a migração da nova tabela

- Criação das rotas para as operações CRUD das tarefas
- Fazer com só o usuário dono da tarefa possa acessar e modificar suas tarefas
- Escrita e execução dos testes para cada operação das tarefas

## Estrutura inicial do código
Primeiro, criaremos um novo arquivo chamado todos.py no diretório de routers:
~~~shell
echo > fast_zero_v2\routers\todos.py
~~~

## Implementação da tabela no Banco de dados

### Testando as novas implementações do banco de dados

como verificar o coverage html?*


## Schemas para Todos


## Endpoint de criação

### Testando o endpoint de criação
~~~shell
echo > .\tests\test_todos.py
~~~

Para executar este teste, você deve usar o comando abaixo no terminal:
~~~shell
task test tests/test_todos.py
~~~

Deu erro no teste, verificar

![alt text](image-4.png)


## Criando a migração da nova tabela
~~~shell
alembic revision --autogenerate -m "create todos table"
~~~


Depois que a migração for criada, precisamos aplicá-la ao nosso banco de dados. Execute o comando alembic upgrade head para aplicar a migração.

~~~shell
alembic upgrade head
~~~

Agora que a migração foi aplicada, nosso banco de dados deve ter uma nova tabela de tarefas. Para verificar, você pode abrir o banco de dados com o comando sqlite3 database.db e depois executar o comando .schema para ver o esquema do banco de dados.

~~~shell
sqlite3 database.db
# ...
sqlite> .schema
# ...
~~~

## Endpoint de listagem

### Criando uma factory para simplificar os testes

#### Testes para esse endpoint

#### Testando a Paginação

#### Testando o Filtro por Título

#### Testando o Filtro por Descrição

#### Testando o Filtro por Estado

#### Testando a Combinação de Filtros de Estado, Título e Descrição

#### Executando os testes
~~~shell
task format  
task test tests/test_todos.py  
~~~

Meu teste deu erro, depois voltar aqui e rever o código*


## Endpoint de Alteração

### Testes para o Endpoint de Alteração
~~~shell
task format  
task test tests/test_todos.py  
~~~

Meu teste deu erro, depois voltar aqui e rever o código*

## Endpoint de Deleção

### Testes para o Endpoint de Deleção

~~~shell
task format  
task test tests/test_todos.py  
~~~

Meu teste deu erro, depois voltar aqui e rever o código* (não dá para executar todas as aulas sem o vídeo, essa aqui por exemplo cria o arquivo `tests.factories` e não vi no documento)
~~~shell
echo > .\tests\factories.py
~~~


## Atualizando o repositório - Commit
Caso seja um repositório de desenvolvimento compartilhado, verificar se no repositório remoto há algo novo e pedir para baixar.
~~~shell
git pull
~~~

Verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Implementado os endpoints de tarefas." 
git push --set-upstream origin main 
~~~



<!--
Rememorar como é para se autenticar e talvez por isso não aparece o swgger com [users] usuários*
-->

# Aula 10 Dockerizando a nossa aplicação e introduzindo o PostgreSQL
<!-- Não assisti o vídeo dessa aula 
https://www.youtube.com/watch?v=bpBbbUgmdMs&list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP
-->
Objetivos da aula:

- Compreender os conceitos básicos do Docker
- Entender como criar uma imagem Docker para a nossa aplicação FastAPI
- Aprender a rodar a aplicação utilizando Docker
- Introduzir o conceito de Docker Compose para gerenciamento de múltiplos contêineres
- Aprender o que é um Dockerfile e sua estrutura
- Entender os benefícios e motivos da mudança de SQLite para PostgreSQL

### pré-requisitos
Para este caso específico, tenho o Docker Desktop instalado no windows com o serviço sempre parado, logo, precisa iniciar o serviço do docker.

## Criando nosso Dockerfile

### Introduzindo o postgreSQL
#### Usar a Sintaxe Correta para cada SO Continuação de Linhas no PowerShell
~~~shell
# Sintaxe para windows
docker run `
    --name app_database_v2 `
    -e POSTGRES_USER=app_user `
    -e POSTGRES_DB=app_db `
    -e POSTGRES_PASSWORD=app_password `
    -p 5432:5432 `
    postgres
~~~

#### Comando para Unix/Linux
~~~shell
docker run \
    --name app_database_v2 \ #nome da imagem docker
    -e POSTGRES_USER=app_user \
    -e POSTGRES_DB=app_db \ #nome do banco de dados
    -e POSTGRES_PASSWORD=app_password \
    -p 5432:5432 \
    postgres
~~~

Com o banco de dados criado, que pode ser verificado no Docker Desktop, vamos testar acesso com uma ferramenta de BD, neste caso é o DBeaver.

Verificando o banco de dados docker via linha de comando:
~~~shell
docker ps -a -q # verifica os containers existentes inclusive os desligados
docker container start 6c13bcfa5e5f # iniciar o container
docker ps # verifica os containers iniciados
~~~

### Adicionando o suporte ao PostgreSQL na nossa aplicação
~~~shell
poetry add "psycopg[binary]"
~~~

Para ajustar a conexão com o PostgreSQL, modifique seu arquivo `.env` para incluir a seguinte string de conexão:
~~~shell
DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
~~~


Atualizar o banco de dados com suas respectivas tabelas com o comando abaixo.
~~~shell
alembic upgrade head
~~~

Abrir o Dbeaver para ver o banco de dados e as tabelas

Agora testar ver se a aplicação está rodando.
~~~shell
task run
~~~

Testando, abrir a aplicação e tentar criar um usuário no http://127.0.0.1:8000/docs
Caso tenha sido criando tentar logar com o usuário criado.

{
  "username": "user@example.com",
  "password": "string"
}

Agora tentar criar um todo e se tudo ok, ir novamente no banco de dados para ver se também salvou em base de dados.

Oh Glória, tudo ok por aqui até o momento.


## Resolvendo os testes que estavam rodando no sqlite
<!-- Vídeo Aula 10 - 00:27:09 -->

### Ajustando o arquivo `conftest.py`
Agora todos os meus testes passaram, mas dependem do banco de dados em pé.


### Testando com Docker
Existe uma biblioteca python que gerencia as dependências de containers externos
para que a aplicação seja executada. O TestContainers
~~~shell
poetry add --group dev testcontainers
~~~

Ajustando programa ... e testando novamente ...
~~~shell
task test -s
~~~


## Parte 2 - Criando a imagem do nosso projeto
<!-- Vídeo Aula 10 - 00:51:28 -->

Criando na raiz o arquivo `Dockerfile`
~~~shell
echo > Dockerfile
~~~


Aqui está um exemplo de Dockerfile para criar o ambiente e executar nossa aplicação:
~~~shell
FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_zero_v2.app:app
~~~

## Criando a imagem
Para criar uma imagem Docker a partir do Dockerfile, usamos o comando docker build. O comando a seguir cria uma imagem chamada "fast_zero":
~~~shell
docker build -t "fast_zero_v2" .
~~~

No terminal funcionou mas no VSCODe não, deu acesso negado em algum arquivo, e o terminal está como adm.


Então verificaremos se a imagem foi criada com sucesso usando o comando:
~~~shell
docker images
~~~

## Executando o container
~~~shell
docker run -it --name fastzeroappv2 -p 8000:8000 fast_zero_v2:latest
~~~

~~~shell
curl http://localhost:8000
~~~

## Parte 3 - Simplificando nosso fluxo com docker-compose
Criação do compose.yaml
~~~shell
echo > compose.yaml
~~~

~~~shell
services:
  fastzero_database:
    image: postgres
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: app_user
      POSTGRES_DB: app_db
      POSTGRES_PASSWORD: app_password
    ports:
      - "5432:5432"

  fastzero_app:
    image: fastzero_app_v2
    entrypoint: ./entrypoint.sh
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - fastzero_database
    environment:
      DATABASE_URL: postgresql+psycopg://app_user:app_password@fastzero_database:5432/app_db

volumes:
  pgdata:
~~~

~~~shell
docker-compose up
~~~

Caso dê algum erro de porta, derrube as imagens e crie o compose novamente.

<!-- Vídeo Aula 10 - 01:24:41 o meu está dando erro com portas já usadas-->

![alt text](image-5.png)

Extra
~~~shell
poetry add ... tolong #biblioteca que auxilia olhar e pesquisar os logs
~~~


## Implementando o Entrypoint
Criamos um script chamado entrypoint.sh que irá preparar nosso ambiente antes de a aplicação iniciar:
~~~shell
echo > entrypoint.sh
~~~


~~~shell
#!/bin/sh

# Executa as migrações do banco de dados
poetry run alembic upgrade head

# Inicia a aplicação
poetry run uvicorn --host 0.0.0.0 --port 8000 fast_zero.app:app
~~~


## Adicionando o Entrypoint ao Docker Compose:

Incluímos o entrypoint no nosso serviço no arquivo compose.yaml, garantindo que esteja apontando para o script correto:

~~~shell
docker-compose up --build
~~~

Caso dê algum erro de execução no arquivo entrypoint, precisa dar poder de execução no mesmo.

~~~shell
docker-compose up -d fastzero_database
~~~

~~~shell
poetry add --group dev testcontainers
~~~

## Atualizando o repositório - Commit
Caso seja um repositório de desenvolvimento compartilhado, verificar se no repositório remoto há algo novo e pedir para baixar.
~~~shell
git pull
~~~

Verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Dokerizando o projeto." 
git push --set-upstream origin main 
~~~

Conferindo se subiu tudo ok
~~~shell
git log
~~~




[🐍 INICIO VOLTAR DAQUI ...🐍]
# Aula 11 Automatizando os testes com Integração Contínua (CI)
<!-- https://fastapidozero.dunossauro.com/11/ 
https://github.com/features/actions
-->
<!-- Minha aplicação não está rodando por erro de porta, verificar 
qd for iniciar a aula, reiniciar a máquina.
-->

## Preparando o ambiente
<!-- No projeto do duno tem o diretório `.git` que não sei de onde é.
-->
Criando os diretórios
~~~shell
mkdir .github
~~~

~~~shell
mkdir .github/workflows
~~~

~~~shell
echo > .github/workflows/pipeline.yaml
~~~

Configurando o workflow de CI
As configurações dos workflows no GitHub Actions são definidas em um arquivo YAML localizado em um path especificado pelo github no repositório .github/workflows/. Dentro desse diretório podemos criar quantos workflows quisermos. Iniciaremos nossa configuração com um único arquivo que chamaremos de pipeline.yaml:
~~~shell
name: Pipeline
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
~~~

Atualizando o repositório.
~~~shell
git add . 
git commit -m "Instalação do Python no CI" 
git push 
~~~

Atualizando as dependencias de arquivos do projeto `.github/workflows/pipeline.yaml`

Atualizando o repositório e ver se executou os testes
~~~shell
git add .\.github\workflows\pipeline.yaml
git commit -m "Executando os testes" 
git push 
~~~

## Configuração de variáveis de ambiente no Actions
Com erro nos testes precisa configurar as variáveis de ambiente usando o gh. No código abaixo ele vai criar segredo para todas as variáveis do arquivo.

~~~shell
gh secret set -f .env
~~~

Verificando os segredos
~~~shell
cat .env
~~~

Agora ir no repositório https://github.com/LuizPerciliano/fast_zero_sync_v2/actions/runs/10501322321/job/29091123627 e atualizar "Re-run jobs" apertando o botão na aplicação.

Deu erro pois faltou atualizar os segredos no `.github/workflows/pipeline.yaml`

## Atualizando o repositório - Commit
Caso seja um repositório de desenvolvimento compartilhado, verificar se no repositório remoto há algo novo e pedir para baixar.
~~~shell
git pull
~~~

Verificar o status do repositório para ver as mudanças realizadas:
~~~shell
git status
~~~

Se tudo estiver ok, adicionar os arquivos, comitar e por fim enviar para o repositório remoto.
~~~shell
git add . 
git commit -m "Adicionando as variáveis de ambiente para o CI"
git push --set-upstream origin main 
~~~




git add . 
git commit -m "ajustando erro no arquivo conftest"
git push --set-upstream origin main 













[🐍 FIM VOLTAR DAQUI ...🐍]
# Aula 12 Fazendo deploy no Fly.io
[...]

~~~shell
git add .
git commit -m "Adicionando arquivos gerados pelo Fly"
git push
~~~

# Aula 13 Despedida e próximos passos
[... ainda vai ter esta aula ...]


# Final da Aplicação: passos para subir a aplicação após tudo finalizado 
1. Entrar no diretório do projeto
1. Ativar o ambiente virtual
3. 

# Projeto final

---

XXX
~~~shell

~~~



~~~python
s = "Sintaxe do Pythong"
print s
~~~

    

