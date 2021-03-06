# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/lcnodc/wttd_projetos.svg?branch=master)](https://travis-ci.org/lcnodc/wttd_projetos)
[![Code Health](https://landscape.io/github/lcnodc/wttd_projetos/master/landscape.svg?style=flat)](https://landscape.io/github/lcnodc/wttd_projetos/master)
[![CodeFactor](https://www.codefactor.io/repository/github/lcnodc/wttd_projetos/badge)](https://www.codefactor.io/repository/github/lcnodc/wttd_projetos)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os teste.

```console
git clone git@github.com:lcnodc/wttd_projetos.git wttd
cd wttd
python -m env .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
# configuro o email
git push heroku master --force
```
