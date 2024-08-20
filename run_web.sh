#!/usr/bin/env bash
cd /webapps/

# Cria e ativa o ambiente virtual
python3.8 -m venv venv
source venv/bin/activate

# Instala as dependências do projeto dentro do ambiente virtual
pip install --use-pep517 psycopg2
pip install -r requirements.txt

ssh -f -N -i PorteiroConexao.pem -o StrictHostKeyChecking=no -o ServerAliveInterval=30 ec2-user@ec2-54-233-179-191.sa-east-1.compute.amazonaws.com -L 127.0.0.1:5432:rotolineapi.c446hggeg6nd.sa-east-1.rds.amazonaws.com:5432

# Executa os comandos do Django
python3.8 manage.py migrate
python3.8 manage.py collectstatic --noinput
python3.8 manage.py runserver 0.0.0.0:8000
