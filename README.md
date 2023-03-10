# Talana Kombat

Talana Kombat es una app para pelea.

# Owner

- Karina Vargas Gonzalez

# New Features!

- App para obtener descripcion y ganador de una pelea

### Requeriments

- Python 3.8

### Installation

Instalaciones de dependencias y devDependencias para empezar.
Para la instalación, tu debes clonar el siguiente repositorio:

- [Repositorio](https://github.com/kary1806/talana_kombat.git)

#### Para el ambiente de desarrollo

- **Contenedor docker:**

```sh
$ git clone <repositorio>
$ docker-compose build
$ docker-compose up
```

_Nota: verificar que se ejecuten todas las migraciones (probablemente se deba correr docker-compose up nuevamente)._

```sh
# Para correr el shell de django
$ docker-compose run talanakombat python manage.py shell
```

Para entrar en la consola del contenedor, en otra terminal, ejecutar:

```sh
# Tiene que estar corriendo el contenedor para poder ejecutar
$ docker-compose exec monet bash
```

```sh
# Para ejecutar los test unitarios
$ docker-compose run talanakombat python manage.py test
```

Para interactuar con los endpoints se necesita un Api Key puede ser generada desde el backoffice:

```sh
$ url_backoffice = http://0.0.0.0:8000/
```

# Url Documentacion Endpoints

```sh
$ url_docs_swagger = http://0.0.0.0:8000/docs/
```
