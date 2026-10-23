# UD1. Práctica: diseño del juego «adivina el número»

Módulo 5098. Entornos y sintaxis en Python.
_Pepe Calo_

<!-- TOC -->
* [UD1. Práctica: diseño del juego «adivina el número»](#ud1-práctica-diseño-del-juego-adivina-el-número)
  * [1. Requisitos previos](#1-requisitos-previos)
  * [2. Enunciado](#2-enunciado)
    * [2.1. Contenido de `DISENO.md`](#21-contenido-de-disenomd)
    * [2.2. Diagrama](#22-diagrama)
    * [2.3. Historial](#23-historial)
  * [3. Comprobaciones automáticas](#3-comprobaciones-automáticas)
  * [4. Evaluación](#4-evaluación)
  * [5. Entrega](#5-entrega)
<!-- TOC -->

Este repositorio procede de la plantilla de la tarea.
El archivo **`ENUNCIADO.md` y las carpetas `.github` y `tests` forman parte de la plantilla y no deben modificarse**.

El trabajo de la **tarea debe escribirse en el documento `DISENO.md` y en la carpeta `diagramas`**.


## 1. Requisitos previos

1. Se debe comprobar que este repositorio es **privado** y que está en la cuenta personal, con el nombre `5098-ud1-<usuario>` (donde `usuario` es el nombre de la cuenta de GitHub).
2. **Invitar como colaborador a la cuenta del profesorado** indicada en el aula virtual: **Settings**, **Collaborators**, **Add people**.
3. **Clonar el repositorio en el equipo local** para trabajar siempre dentro de la carpeta clonada.

Es típico repetir estos errores durante la práctica y no realizar esos requisitos previos. Sin ellos no podré corregir la tarea, que no será evaluada.


## 2. Enunciado

Esta práctica consiste en realizar el diseño completo del juego **«adivina el número»**, sin programarlo (sé que a los que ya saben programar les resultará mu sencillo, pero no todos partimos de la misma base). El programa elige un número secreto entre 1 y 100 y, en cada intento de la persona que juega, indica si el número buscado es mayor o menor, hasta que se acierta. Al final muestra **cuántos intentos** se han necesitado.

Es una **tarea de diseño**, por lo que no se pide código Python ejecutable. Si alguien ya sabe Python, y sin uso de IA (con ella sería un trabajo inutil), puede usarlo para **verificar** que el diseño es correcto y como ampliación no evaluable. 

### 2.1. Contenido de `DISENO.md`

Se trata del documento de trabajo para completar. El archivo ya contiene los nueve encabezados, con una explicación de lo que se pide en cada uno. Se debe completar cada línea marcada como *Pendiente* por el contenido asociado. El contenido de cada apartado es el siguiente:

1. **Análisis del entorno**: dónde y por quién se usaría el juego y qué condiciona eso.
2. **Análisis del problema**: tabla de entrada, proceso y salida.
3. **Estrategia**: descomposición o refinamiento sucesivo en, al menos, dos niveles.
4. **Dificultades y casos de prueba**: lista de dificultades y tabla con, al menos, cuatro casos de prueba.
5. **Pseudocódigo** de la solución, en un bloque de código.
6. **Diagrama de flujo**: imagen enlazada desde `DISENO.md` o bloque Mermaid.
7. **Pruebas**: tabla con un número secreto y, al menos, tres intentos que recorran todos los caminos del diagrama.
8. **Alternativa y selección**: una segunda forma de resolver algún aspecto, comparada con la elegida mediante una tabla de valoración.
9. **Verificación en Python**: tabla con la construcción de Python **que corresponde a cada símbolo** y los detalles que habrá que cuidar al programarlo, sin la codificación completa (como he comentado, puede realizarse como ampliación no evaluable).

### 2.2. Diagrama

De las estrategias de diseño vistas en la unidad, nos centraremos en el **diagrama de flujo** con dos herramientas posibles: [Excalidraw](https://excalidraw.com) (o [draw.io](https://draw.io)) y [Mermaid](https://mermaid.js.org). Recordad que excalidraw dispone de una versión web y de otra de escritorio, además de existir bibliotecas que os pueden ayudar a generar diagramas de flujo a partir de pseudocódigo. Mermaid Se integra mejor con Markdown y permite generar diagramas de flujo a partir de un bloque de código, pero no es tan flexible como Excalidraw y dependemos de versiones concretas que a veces no son compatibles.

El diagrama debe reflejar el pseudocódigo y ser coherente con él. Se recomienda que el diagrama sea **claro, legible y completo**.

Se permiten dos formas válidas de presentar el diagrama:

- **Excalidraw** (o draw.io): **la imagen exportada (`.svg` o `.png`) y su archivo fuente (`.excalidraw` o `.drawio`)** en la carpeta `diagramas`, y la imagen enlazada desde el apartado 6 de `DISENO.md`, por ejemplo `![Diagrama del juego](diagramas/adivina.svg)`.
- **Mermaid**: un bloque de código `mermaid` dentro del apartado 6 de `DISENO.md`. En ese caso no hace falta imagen, pero se puede guardar también el código en `diagramas/adivina.mmd`.

### 2.3. Historial

- Al menos deben existir **tres commits propios**, repartidos a lo largo del trabajo y con mensajes descriptivos (por ejemplo, uno por bloque: análisis, diseño, comprobación). Un único commit final no se considerará correcto.

## 3. Comprobaciones automáticas

Tras cada `git push`, GitHub Actions ejecuta las **comprobaciones de la carpeta `tests`**. El resultado aparece junto a cada commit en la página del repositorio: **marca verde si se superan todas y cruz roja si alguna falla**. La pestaña **Actions** indica cuál y por qué.

Las comprobaciones revisan la **forma** del trabajo (que estén todos los apartados, las tablas, el pseudocódigo, el diagrama y su fuente), no si el diseño es correcto: **orientan, pero no califican**. También pueden ejecutarse en el equipo:

```bash
python -m pip install pytest
python -m pytest -v tests
```

## 4. Evaluación

| Aspecto | CE | Peso orientativo |
|---|:--:|:--:|
| Análisis del entorno y del problema | a | 10 % |
| Estrategia y descomposición | b | 15 % |
| Dificultades y casos de prueba | c | 20 % |
| Pseudocódigo y diagrama de flujo correctos y coherentes | d | 25 % |
| Alternativa y justificación de la elección | e | 15 % |
| Verificación en Python | f | 10 % |
| Presentación, Markdown y uso de Git | | 5 % |


## 5. Entrega

1. Enviar **todo el trabajo con `git push` y comprobar con `git status` que la rama está al día con `origin/main`**.
2. Abrir la página del repositorio en GitHub y copiar el hash abreviado del último commit (siete caracteres). Si aparece en GitHub, está enviado.
3. Entregar en la tarea del aula virtual, antes de la fecha de cierre, un texto con estas dos líneas:

```text
Repositorio: https://github.com/usuario/5098-ud1-usuario
Commit: a1b2c3d
```

La versión corregida es la del commit indicado, aunque después se añadan otros. Si el plazo sigue abierto, la entrega se puede actualizar con un hash nuevo.
