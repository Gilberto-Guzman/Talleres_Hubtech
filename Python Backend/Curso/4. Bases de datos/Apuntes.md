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

### 4. Consultas con restricciones.

    SELECT Id, Title FROM Movies
    WHERE Id = 6;

    SELECT Title, Year FROM Movies
    WHERE Year BETWEEN 2000 AND 2010;

    SELECT Title, Year FROM Movies
    WHERE Year < 2000 OR Year > 2010;

    SELECT Title, Year FROM Movies
    WHERE Year <= 2003;

### 5. Consultas con restricciones Case sensitive y Case insensitive.

    SELECT Title, Director FROM Movies
    WHERE Title LIKE "Toy Story%";

    SELECT Title, Director FROM Movies
    WHERE Director = "John Lasseter";

    SELECT Title, Director FROM Movies
    WHERE Director != "John Lasseter";

    SELECT * FROM Movies
    WHERE Title LIKE "WALL-_";

### 6. Filtrado y ordenamiento de los resultados de las consultas.

    SELECT DISTINCT Director FROM Movies
    ORDER BY Director ASC;

    SELECT Title, Year FROM Movies
    ORDER BY Year DESC
    LIMIT 4;

    SELECT Title FROM Movies
    ORDER BY Title ASC
    LIMIT 5;

    SELECT Title FROM Movies
    ORDER BY Title ASC
    LIMIT 5 OFFSET 5;

### 7. Simple SELECT Queries

    SELECT City, Population FROM north_american_cities
    WHERE Country = "Canada";

    SELECT City, latitude FROM north_american_cities
    WHERE Country = "United States"
    ORDER BY latitude DESC;

    SELECT City, longitude FROM north_american_cities
    WHERE longitude < -87.629798
    ORDER BY longitude ASC;

    SELECT City, Population FROM north_american_cities
    WHERE Country LIKE "Mexico"
    ORDER BY Population DESC
    LIMIT 2;

    SELECT City, Population FROM north_american_cities
    WHERE Country LIKE "United States"
    ORDER BY Population DESC
    LIMIT 2 OFFSET 2;

### 8. Consulta de varias tablas con JOINS

    SELECT Title, Domestic_sales, International_sales
    FROM Movies
        JOIN boxoffice
            ON Movies.id = boxoffice.Movie_id;

    SELECT Title, Domestic_sales, International_sales
    FROM Movies
        JOIN boxoffice
            ON Movies.id = boxoffice.Movie_id
    WHERE International_sales > Domestic_sales;

    SELECT Title, Rating
    FROM Movies
        JOIN boxoffice
            ON Movies.id = boxoffice.Movie_id
    ORDER BY Rating DESC;

### 9. OUTER JOINS

    SELECT DISTINCT Building FROM Employees;

    SELECT * FROM buildings ;

    SELECT DISTINCT Building_name, Role
    FROM Buildings
    LEFT JOIN Employees
        ON Building_name = Building;

### 10. NULLS

    SELECT Name, Role FROM Employees
    WHERE Building IS NULL;

### 11. Consultas con Expresiones

    SELECT DISTINCT Building_name
    FROM Buildings
    LEFT JOIN Employees
        ON Building_name = Building
    WHERE Role IS NULL;

### 12. Aggregates

### 13. Orden de Ejecución de una Query

### 14. Inserting Rows

### 15. Updating Rows

### 16. Deleting Rows

### 17. Creating Tables

### 18. Altering Tables

### 19. Dropping Tables
