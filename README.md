# Examen de la primera unidad - Backend
---

## Tecnológico de Software

## Materia: Fundamentos de arquitectura de software y desarrollo backend

## Profesor: Gimer Almicar Cervera Evia

## Alumna: Giovana Ruby Díaz Anduze

## Cuarto cuatrimestre

---

# EJERCICIO 3

## *Preguntas*

1. Explica dos diferencias entre una API REST y un servidor GraphQL.

Con lo que estuve estudiando, considero que las dos diferencias clave entre API REST y un servidor GraphQL es que con respecto a lo que hace REST es que utiliza operaciones CRUD para poder ejecutar los endpoints, mientras que en GrapghQL lo que entiendo es que se apoya principalmente de métodos GET para Queries y POST para Mutations.

Otra diferencia que he observado es que el uso de REST lo que identifico es que cada recurso cuenta con un propio endpoint, es como el ejemplo que vimos en clase que REST puede compararse como si fuera un restaurante con menú a la carta, esto principalmente porque es el servidor el que decide la forma en la que se va a devolver una respuesta y muchas veces lo que ocurre es que se recibe más de lo que se requiere.

Es por eso que se creó GraphQL porque resuelve una de las limitantes de REST pues lo que hace es que como mencioné de REST funciona como un menú a la carta, GraphQL funciona como un restaurante buffet, ya que en un sólo recorrido se arma la "comida".

2. Indica una situación en la que conviene usar REST y otra en la que conviene usar GraphQL.

Por lo que entiendo, REST más que nada se usa principalmente para cuando una API es pública para terceros, cuando el caché es crítico y es un sistema simple con pocos recursos; mientras que para usar GraphQL se puede utilizar cuando hay muchos clientes que tienen necesidades distintas y tiene datos tienen muchas relaciones.

3. ¿Qué diferencia hay entre una imagen y un contenedor? ¿Qué papel cumple el Dockerfile en esa relación?

La diferencia que hay entre una imagen y un contenedor es que así como el profe lo explicó, una imagen es básicamente una plantilla la cuál contiene los archivos para desarrollar el ambiente, o sea que actúa como una receta o un molde; mientras que un contenedor pues es la instancia que se ejecuta a partir de la imagen.

Y por lo que entiendo, el Dockerfile lo que hace es definir los pasos para que se cree la imagen así que viéndolo como parte de la análogía, sería algo como la lista pasos e ingredientes (dockerfile) para la receta (imagen) para que se prepare el postre (contenedor).

4. ¿Para qué sirve Docker Compose? En el mapeo 8000:8000, ¿qué representa el primer 8000 y qué representa el segundo?

5. ¿Por qué las laptops del ejercicio 1 se guardan en MySQL y no en una lista de Python? ¿Qué identifica la llave primaria id?