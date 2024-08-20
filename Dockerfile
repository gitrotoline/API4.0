# Usar a imagem oficial do Fedora com Python 3.8
FROM fedora:latest

# Instalar o Python 3.8, pip e outras dependências
RUN dnf -y update && dnf -y install python38 python3-pip python3-devel sqlite-devel postgresql-devel gcc openssh-clients

# Instalar o pacote libpq-dev para compilar psycopg2
RUN dnf -y install libpq-devel --allowerasing

# Criar o diretório do projeto e definir o diretório de trabalho
RUN mkdir /webapps
WORKDIR /webapps

# Definir a variável de ambiente para não-bufferizar a saída do Python
ENV PYTHONUNBUFFERED 1

# Atualizar o pip e o setuptools
RUN pip install -U pip setuptools

# Copiar o arquivo requirements.txt e instalar as dependências Python
COPY requirements.txt /webapps/
RUN pip install -r requirements.txt

# Copiar todo o código-fonte do projeto para o diretório de trabalho do contêiner
COPY . /webapps/

# Expor a porta 8000 para acesso ao servidor Django (se necessário)
EXPOSE 8000

RUN chmod 400 PorteiroConexao.pem

# Definir permissões de execução para o script "run_web.sh" (se aplicável)
RUN chmod +x /webapps/run_web.sh

# Definir o comando padrão para iniciar o serviço Django (ou o comando que você usa para iniciar o servidor)
CMD ["/webapps/run_web.sh"]
