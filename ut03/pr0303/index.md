## Práctica 0303

* Para la realización de esta práctica tendremos que utilizar distintos comandos:
    
    * Primero pararemos el servicio con el comando: __service postgresql stop__
    * A continuación creamos la copia de seguridad con el comando: __pg-dump -U odoo dbodoo > backup.sql__. El primer odoo hará referencia al nombre del usuario y el segundo al nombre de la BBDD
    * Borramos todo el contenido de las carpetas filestore, addons y sessions
    * Para poder acceder a la terminal de postgres se utilizará el comando: __docker compose exec odoo bash__.
    * Después se sacará la copia de seguridad del contenedor a una ruta nuestra con el siguiente comando: __docker cp 1e50:/backup.sql .__
    * Crearemos otra vez los contenedores mediante el comando docker compose.
    * Utilizaremos __su postgres__ para iniciar sesión con el usuario que tiene permisos en la base de datos.
    * Crearemos la base de datos mediante el comando: __create -U odoo -O odoo dbodoo__. El primer odoo es el usuario, el segundo es para indicar el propietario y el tercero es el nombre de la base de datos
    * Finalmente,  metemos todo el contendio de la copia de seguridad mediante el comando: __psql -U odoo dbodoo < backup.sql__.

* __Anotación__: Quitando el último punto lo demás fue bien, se creó la copia de seguridad  y los contenedores, pero nunca se volcó el contenido de la copia de seguridad en la base de datos.