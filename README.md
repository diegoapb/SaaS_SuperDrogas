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


## Producción

Construimos el proyecto y lo corremos

```
docker-compose -f docker-compose.prod.yml up -d --build
```

Se agregan los datos iniciales a la BD

```
docker exec -it saas_pg_prod psql -U postgres -d multitenant -f /home/_datos_iniciales/2_tenant_publico.sql
```



## Tests

## Construido con:

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Jenkins](https://jenkins.io/doc/) - Dependency Management
* [Django-tenants](https://django-tenants.readthedocs.io/en/latest/) - Used to create SaaS app

## Autores


* [Laura Villan](https://github.com/laura2398)-01
* [Sebastian Lopez](https://github.com/sebas119)-02
* [Daniel Baltazar](https://github.com/terbas1)-03
* [Helen Bonilla](https://github.com/HelenBonilla)-04
* [Diego Parra](https://github.com/Diegoapb)-05
* [Carlos Acuaruri]()-06

## Licencia


# Documentación

tenant_command
~~~~~~~~~~~~~~

To run any command on an individual schema, you can use the special ``tenant_command``, which creates a wrapper around your command so that it only runs on the schema you specify. For example

.. code-block:: bash

    ./manage.py tenant_command loaddata

If you don't specify a schema, you will be prompted to enter one. Otherwise, you may specify a schema preemptively

.. code-block:: bash

    ./manage.py tenant_command loaddata --schema=customer1

create_tenant_superuser
~~~~~~~~~~~~~~~~~~~~~~~

The command ``create_tenant_superuser`` is already automatically wrapped to have a ``schema`` flag. Create a new super user with

.. code-block:: bash

    ./manage.py create_tenant_superuser --username=admin --schema=customer1


create_tenant
~~~~~~~~~~~~~

The command ``create_tenant`` creates a new schema

.. code-block:: bash

    ./manage.py create_tenant --domain_url=newtenant.net --schema_name=new_tenant --name=new_tenant --description="New tenant"

The argument are dynamic depending on the fields that are in the ``TenantMixin`` model.
For example if you have a field in the ``TenantMixin`` model called company you will be able to set this using --company=MyCompany.
If no argument are specified for a field then you be promted for the values.
There is an additional argument of -s which sets up a superuser for that tenant.
