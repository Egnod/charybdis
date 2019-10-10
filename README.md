<p align="center">
  <h1 align="center">Charybdis</h1>
  </p>
 
 ![Travis (.org)](https://img.shields.io/travis/lemegetonx/charybdis)
 ![GitHub](https://img.shields.io/github/license/lemegetonx/charybdis)
 ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/lemegetonx/charybdis)
[![Join the chat at https://gitter.im/lemegetonx/charybdis](https://badges.gitter.im/lemegetonx/charybdis.svg)](https://gitter.im/lemegetonx/charybdis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

##  User manager for your projects
Charybdis is permissions and auth manager

# Expand

## Docker Compose
See charybdis.example.yml or copy this code
```yaml
version: '3.1'

services:
  charybdis:
    image: egnod/charybdis
    restart: always
    environment:
      - CHARYBDIS_DB_PASSWORD=charybdis_secrets
      - CHARYBDIS_DB_USER=charybdis
      - CHARYBDIS_DB_NAME=charybdis
      - CHARYBDIS_DB_PORT=
      - CHARYBDIS_DB_HOST=db
    ports:
      - 34004:8000
    depends_on:
      - db

  db:
    image: postgres
    restart: always
    environment:
      - POSTGRES_PASSWORD=charybdis_secrets
      - POSTGRES_USER=charybdis
      - POSTGRES_DB=charybdis
    ports:
      - 34006:5432

  redis:
    image: 'bitnami/redis:5.0'
  environment:
      - ALLOW_EMPTY_PASSWORD=no
      - REDIS_PASSWORD=charybdis_secrets
      - REDIS_DISABLE_COMMANDS=FLUSHDB,FLUSHALL
    ports:
      - 34007:6379
    volumes:
      - 'redis:/bitnami/redis/data'

volumes:
  redis:
    driver: local
```
###  Start compose

```bash
docker-compose -f <compose_filename.yml> up
```

## Legacy
###  Clone charybdis
```bash
git clone https://github.com/Egnod/charybdis.git
```
###  Configure Instruments
Install and start postgresql and redis databases.

###  Configure Charybdis
Set config vars in system env with prefix *CHARYBDIS*.
Example for Linux:
```bash
export CHARYBDIS_DB_PORT=34006
```
Variables list (for use with system providers):

 - CHARYBDIS_DB_PASSWORD
 - CHARYBDIS_DB_USER
 - CHARYBDIS_DB_NAME
 - CHARYBDIS_DB_PORT
 - CHARYBDIS_DB_HOST
 - CHARYBDIS_REDIS_HOST
 - CHARYBDIS_REDIS_PORT
 - CHARYBDIS_REDIS_PASSWORD
 - CHARYBDIS_LOGGING_FORMAT
 - CHARYBDIS_LOGGING_LEVEL

### Start Charybdis
Start Charybdis with gunicorn or native flask server.

## Defaults

On ***first start*** charybdis create defaults - user, domain and base **admin** role.

Domain:

    Name/Slug: Global/global
    UUID: 00000000-0000-0000-0000-000000000000

User:

    UserName: basic
    Password Hash/Password: $pbkdf2-sha512$25000$D.G8t/beGwOgdM4ZY8y5Vw$WsKIhGgwUyhEOp5LAaU/MQFTIQeD3Hzil5Lzuys95iKwhLOYdFw8WPt.BAASS9bTIPRIzebfMe3pRieDzbFCnQ / 123
    UUID: 00000000-0000-0000-0000-000000000000
    First/Last Names: 1/1
    Birthday: 2019-10-29
    Role: admin
    Domain: global

###  Connect
For use charybdis connect to server by RESTful API or **Scylla** client (url: ***comming soon***)
