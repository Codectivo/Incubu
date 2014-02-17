Incubu
======

Guarda tus cuentas de manera segura. Proyecto que nacio en consecuencia
a que se tenian muchas cuentas y muchas claves que recordar. Entonces
se necesitaba de un lugar unificado para que se pudieran consultar esas
cuentas/claves de manera segura.

La informacion se cifra antes de ser guardada en el cliente, es decir, 
en el navegador. Asi cuando la informacion llega a la BD ya llega encriptada.

Instalación
===========

°Descargar proyecto

	git clone https://github.com/Codectivo/Incubu.git

°Instalar virtualenv

    $ virtualenv env

°Activar virtualenv

    $ source /env/bin/activate

°Instalar requeriments.

    $ pip install -r requeriments.txt

°Crear un archivo config.json, similar a config.json-src

    $ cp config.json-src config.json

°Crear archivo en la raiz del proyecto de la Base de Datos (Nombre que se puso a la BD en config.json)

    $ touch incubu.db

°Sincronizar BD.

    $ python manage.py syncdb

°Ejecutar migraciones South para BD.

    $ python manage.py migrate

°Ejecutar proyecto y abrir http://127.0.0.1:8000

    $ python manage.py runserver 8000

