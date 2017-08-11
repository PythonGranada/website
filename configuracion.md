# Variables de entorno

Se recomienda trabajar con un entorno vitual.

## Secret key

La clave secreta que usa Django se almacena en una variable de entorno.
Imprescindible asignar una en producción.

** Durante la fase de desarrollo no hace falta crear una variable de entorno **

## Integración con github

En el sistema actual cuando alguien envía una propuesta de charla, se acordó que
esta apareciese como `issue` en el repositorio de organización de Python Granada.

Para ello cuando alguien rellena el formulario se conecta con la api de github
y se crea un nuevo issue. Este repositorio es privado por lo que es necesario
que la clave de acceso de github sea de alguien miembro de la comunidad.

Una vez obtenida esta clave la aplicación usa la variable de entorno `GITHUB`.
Es suficiente con crear una variable con este nombre y que contenga la clave.

Documentación de github sobre la [creación de issues](https://developer.github.com/v3/issues/#create-an-issue)
Para obtener la clave vamos a la configuración de nuestro perfil > Personal access tokens

** Sin esta clave el servicio no funciona **

## Envio de e-mail

El formulario de contacto funciona enviando un correo. Para ello es necesario
configurar la información básica de acuerdo a la
[documentación de Django](https://docs.djangoproject.com/en/1.11/topics/email/#smtp-backend).

Las variables de entorno tienen los nombres

"""
EMAIL_BACKEND
EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_PORT
EMAIL_USE_TLS
"""

El el archivo `views.py`, en la clase que controla el envio del e-mail, está
la lista de destinatarios del mismo.

** Sin estas variables el servicio no funciona **
