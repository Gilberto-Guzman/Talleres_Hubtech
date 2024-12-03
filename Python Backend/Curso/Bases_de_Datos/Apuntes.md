### 1. ¿Que son las bases de datos y qué tipos hay?.

Base de datos ⮕ Es un sistema organizado para almacenar, gestionar y recuperar información.

Tipos:

- Relacionales ⮕ Organizan los datos con filas y columnas, ademas manejan relaciones entre tablas.
- No relacionales ⮕ Almacenan datos no estructurados o semiestructurados y no requieren esquemas rigidos.

### 2. ¿Qué es SQL?.

Para operar una base de datos informatica, es necesario contar con lo siguiente:

- Un motor de base de datos
- Un sistema de géstion de bases de datos (DBMS).

SQL ⮕ Es un lenguaje de programación utilizado para trabajar con bases de datos relacionales.

Permite:

- Consultar datos: Usando SELECT.
- Modificar datos: Usando INSERT, UPDATE y DELETE.
- Definir estructuras: Usando CREATE y ALTER.
- Administrar bases de datos: Configurar usuarios y permisos.

Ejemplo ⮕ SELECT nombre, edad FROM empleados WHERE departamento = 'Ventas';

### 3. Cláusula SELECT y primeras consultas.

https://sqlbolt.com/

    SELECT Title FROM Movies;

    SELECT Director FROM Movies;

    SELECT Title, Director FROM Movies;

    SELECT Title, Year FROM Movies;

    SELECT * FROM Movies;

### 4. Consultas con restricciones

    SELECT Id, Title FROM Movies
    WHERE Id = 6;

    SELECT Title, Year FROM Movies
    WHERE Year BETWEEN 2000 AND 2010;

    SELECT Title, Year FROM Movies
    WHERE Year < 2000 OR Year > 2010;

    SELECT Title, Year FROM Movies
    WHERE Year <= 2003;

### 5. Consultas con restricciones Case sensitive y Case insensitive

    SELECT Title, Director FROM Movies
    WHERE Title LIKE "Toy Story%";

    SELECT Title, Director FROM Movies
    WHERE Director = "John Lasseter";

    SELECT Title, Director FROM Movies
    WHERE Director != "John Lasseter";

    SELECT * FROM Movies
    WHERE Title LIKE "WALL-_";
