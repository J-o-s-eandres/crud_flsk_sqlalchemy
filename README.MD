```markdown
# CRUD de Contactos

Este es un proyecto CRUD (Crear, Leer, Actualizar, Borrar) de contactos desarrollado en Flask.

## Descripción

El objetivo de este proyecto es proporcionar una aplicación web simple para gestionar una lista de contactos. La aplicación permite realizar las siguientes operaciones:

- Crear un nuevo contacto
- Leer los contactos existentes
- Actualizar la información de un contacto
- Borrar un contacto

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
https://github.com/J-o-s-eandres/crud_flsk_sqlalchemy
```

2. Instala las dependencias necesarias usando pip:

```bash
pip install -r requirements.txt
```

## Configuración

1. Crea una base de datos MySQL llamada `contactsDB`.
2. Configura las credenciales de tu base de datos en el archivo `config.py`.
3. Ejecuta el siguiente comando para crear las tablas necesarias en la base de datos:

```bash
python create_tables.py
```

## Uso

1. Ejecuta la aplicación:

```bash
python app.py
```

2. Abre tu navegador web y visita [http://localhost:5000](http://localhost:5000) para ver la aplicación en funcionamiento.

## Funcionalidades

### Crear un nuevo contacto

- Ruta: `/new`
- Método: POST
- Parámetros: fullname, email, phone

### Actualizar un contacto existente

- Ruta: `/update/<int:id>`
- Método: POST
- Parámetros: fullname, email, phone

### Borrar un contacto

- Ruta: `/delete/<int:id>`
- Método: GET

### Ver todos los contactos

- Ruta: `/`
- Método: GET

## Sobre

Este proyecto fue desarrollado por [Joseandres Montesino] como parte de [Praçticas de programación]. 

```
