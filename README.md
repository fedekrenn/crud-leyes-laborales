# Proyecto Integrador - CRUD de leyes y normativas 

Proyecto grupal para el módulo "programador" de la tecnicatura en desarrollo web y aplicaciones digitales | ISPC . Está compuesto por tres espacios curriculares, que integran el módulo “Programador”, estos son: Introducción a la Programación, Base de Datos, y Ética y Deontología
Profesional.

## Descripción del proyecto 

Se trata de un programa desarrollado en Python el cual ejecuta un menú en loop que te permite manipular mediante un CRUD leyes/normativas de Argentina, el menú está diagramado de la siguiente manera:

```
########################### MENÚ ###########################
1.- Traer Leyes
2.- Traer Ley por N° de Ley
3.- Traer Ley por palabra clave
4.- Registrar Ley
5.- Actualizar Ley
6.- Borrar Ley
7.- Salir
#############################################################
```

Una vez seleccionada la acción y seguidos los pasos correspondientes de c/u, el menú vuelve a ejecutarse, dando así la funcionalidad de un programa en constante ejecución y sólo finaliza si el usuario marca la opción 7 para Salir.

### Anexos
En la carpeta db_files se puede encontrar:

- El Der en formato PDF
- El modelo relacional también en formato PDF
- El archivo .sql con la base de datos

## Pasos para ejecutar

1 - Clonar el proyecto

`git clone https://github.com/proyecto-modulo-programador/programador.git`

2- Instalar el Connector de MySQL

` pip install mysql-connector-python ` 

3 - Ejecutar el archivo main.py

## Puntos a tener en cuenta

- Para hacer el programa más óptimo y ejecutable en cualquier entorno, se optó por subir la base de datos a un servidor en la nube, el mismo es [Clevercloud](https://www.clever-cloud.com/) y los datos de conexión están en el archivo de configuración, el cual a su vez modificando sólo los datos por el localhost puede ejecutarse con una DB local. De igual manera, en la carpeta db_files está el archivo "database.sql" con todas las query que crean la db para poder ejecutarla en local

- Cuando se da de alta una nueva normativa, la clase posee una validación para que el usuario no tenga que seleccionar manualmente el dato del órgano legislativo, esto es debido a que si la ley es nacional, el órgano legislativo es el Congreso de la Nación. Por el contrario, si la ley es provincial, corresponde la Legislatura de Córdoba. Entonces el usuario al seleccionar la jurisdicción, el órgano legislativo se selecciona automáticamente.


<br>

## 🙋‍♂️ Hola, Soy Federico Krenn
:nerd_face: Desarrollador web Fullstack
<br>
👨‍🎓 Realizando la Tecnicatura en Desarrollo Web en ISPC y Tecnicatura en Software Libre en la UNL
<br>
📫 Conectemos en Linkedin: https://www.linkedin.com/in/fkrenn/
