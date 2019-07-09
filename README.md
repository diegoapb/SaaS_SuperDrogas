# Super Drogas SaaS

Aplicacion saas para la gestion de medicamentos en una fatmacia

## Empezando

Estas instrucciones le brindarán una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba. Consulte la implementación para ver las notas sobre cómo implementar el proyecto en un sistema en vivo.

### Prerequisitos

Para implementar la aplicacion debe tener instalado:

```
docker
docker compose
```

### Instalacion

* [Video guia run django y postgres](https://drive.google.com/file/d/1is8GQPV8OirDKri0nduiNaRYXNkZySsc/view?usp=sharing) - es la guia para poner a correr el servidor web con su base de datos

* [Video guia run pgAdmin](https://drive.google.com/file/d/10g_Z-gAQm9-UfOscYdswJng74zJDKH4h/view?usp=sharing) - Para monitorizar la base de datos.


Para ejecutar el entorno de desarrollo debe de hacer el siguiente paso a paso.

Clonar repositorio de github

```
git clone https://github.com/diegoapb/SaaS_SuperDrogas.git
```
si las migraciones estan listas usa el docker compose

```
docker-compose up
```

#### Si no existe una base de datos debe ser creada ####

Debes tener una base de datos llamada **multitenant** se creara **automaticamente**, de lo contrario ejecutaras este comando.

```Sh
docker exec -it saas_pg psql -U postgres -c "create database multitenant"
```
#### Si no has hecho las migraciones de la base de datos debes hacer los siguientes pasos

Luego de que el proceso halla finalizado, a migrar los esquemas a labase de datos

```
docker-compose run web python manage.py migrate_schemas
```
Agregar datos iniciales a postgres:

agrege los datos iniciales a la base de datos, estos se encuentran en la siguiente direccion ``` ./_datos_iniciales ``` para agregarlos usa el sgte comando.

```
docker exec -it saas_pg psql -U postgres -d multitenant -f /home/_datos_iniciales/1_tenant_publico.sql
```
Ahora debemos reiniciar todos los servicios para subir el servidor junto con la base de datos actualizada

```
docker-compose restart
```

Para finalizar solo debemos ingresar al localhost mencionado por el servidor para ver nuestra aplicacion corriendo

```
http://localhost:8000
```

## Tests

## Construido con:

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Jenkins](https://jenkins.io/doc/) - Dependency Management
* [Django-tenants](https://django-tenants.readthedocs.io/en/latest/) - Used to create SaaS app

## Autores

## Licencia