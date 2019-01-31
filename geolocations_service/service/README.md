# Português-BR

## Descrição

Este serviço fornece CRUDs para as geolocalizações

Atualmente conta com três endpoints:

* `/api/geolocations/` para cadastro e recuperação de posições geográficas contendo latitude e longitude;

* `/api/visited_locations/` para cadastro e recuperação de posições geográficas ja visitadas;

* `/api/found_people/` para cadastro e recuperação de pessoas localizadas em uma geolocalização;


## Instalando

Clone o repositório para um dretório da sua preferencia

Instale os requerimentos para o servidor funcionar (preferencialmente em um ambiente virtual).


### Desenvolvimento
    pip install -r service.requirements.txt

### Rode as migrations já existentes.
    
    python manage.py migrate


## Rodando:

### Desenvolvimento

    make run

Acesse o servidor local em `localhost:5002/api/`

## HELP NEEDED

Tem muita coisa que pode ser feita aqui ainda, toda ajuda é necessária.


<hr />

# English

## Description

This service serves CRUD for geoposition data.

For now it only have three endpoints:

* `/api/geolocations/` for creating and retrieving of groposition information (latitude and longitude));

* `/api/visited_locations/` for creating and retrieving already visited geopositions;

* `/api/found_people/` for creating and retrieving found people in a geoposition coordinate;

## Installing

Clone repo to a workspace.

Install requeriments (preferably in a virtual environment)

### Development
    pip install -r service.requirements.develop.txt

### Migrate the database

    python manage.py migrate

## Running:

### Development

    make run_dev

Acess local server at `localhost:5002/api/`



## HELP NEEDED

There are a lot of work to do here yet, all help is needed.

<hr />
