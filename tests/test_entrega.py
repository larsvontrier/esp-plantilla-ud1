"""
Comprobaciones automaticas de la practica integradora de la UD1.

Se ejecutan en GitHub Actions tras cada push. Revisan la forma del trabajo
(apartados, tablas, pseudocodigo, diagrama y su fuente, historial), no si el
diseno es correcto: una comprobacion superada no garantiza la calificacion,
que pone el profesorado.

Para ejecutarlas en el equipo:
    python -m pip install pytest
    python -m pytest -v tests
"""

import json
import re
import subprocess
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
DISENO = RAIZ / "DISENO.md"
DIAGRAMAS = RAIZ / "diagramas"
COMMITS_PROPIOS = 3  # sin contar el commit inicial que crea la plantilla
PALABRAS_MINIMAS = 15

APARTADOS = {
    1: "Análisis del entorno",
    2: "Análisis del problema",
    3: "Estrategia",
    4: "Dificultades y casos de prueba",
    5: "Pseudocódigo",
    6: "Diagrama de flujo",
    7: "Prueba de escritorio",
    8: "Alternativa y selección",
    9: "Verificación en Python",
}

IMAGENES = (".svg", ".png", ".jpg", ".jpeg")
FUENTES = (".excalidraw", ".drawio", ".mmd")


def git(*args):
    proceso = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)
    return proceso.stdout.strip()


def leer_diseno():
    assert DISENO.is_file(), "Falta el archivo DISENO.md."
    texto = DISENO.read_text(encoding="utf-8")
    # los comentarios HTML no cuentan como contenido
    return re.sub(r"<!--.*?-->", "", texto, flags=re.DOTALL)


def apartados():
    """Devuelve un diccionario {numero: texto del apartado}."""
    texto = leer_diseno()
    partes = re.split(r"^##\s+(\d+)\.", texto, flags=re.MULTILINE)
    # partes = [preambulo, num1, texto1, num2, texto2, ...]
    resultado = {}
    for i in range(1, len(partes) - 1, 2):
        resultado[int(partes[i])] = partes[i + 1]
    return resultado


def filas_de_tabla(texto):
    """Filas de datos de las tablas Markdown (sin cabecera ni separador)."""
    filas = [l.strip() for l in texto.splitlines() if l.strip().startswith("|")]
    datos = [f for f in filas if not re.fullmatch(r"\|[\s:|-]+\|?", f)]
    # la primera fila de cada tabla es la cabecera: se descuenta una por tabla
    tablas = sum(1 for f in filas if re.fullmatch(r"\|[\s:|-]+\|?", f))
    return max(len(datos) - tablas, 0)


def palabras(texto):
    # cuentan tambien las palabras de los bloques de codigo (pseudocodigo, refinamiento)
    sin_marcas = re.sub(r"```[a-z]*", " ", texto)
    return len(re.findall(r"\w+", sin_marcas))


def test_estan_los_nueve_apartados():
    encontrados = apartados()
    faltan = [f"{n}. {t}" for n, t in APARTADOS.items() if n not in encontrados]
    assert not faltan, "Faltan apartados numerados en DISENO.md: " + "; ".join(faltan)


@pytest.mark.parametrize("numero", list(APARTADOS))
def test_apartado_completado(numero):
    texto = apartados().get(numero, "")
    nombre = f"{numero}. {APARTADOS[numero]}"
    assert "_Pendiente._" not in texto, f"El apartado «{nombre}» sigue marcado como pendiente."
    assert palabras(texto) >= PALABRAS_MINIMAS, (
        f"El apartado «{nombre}» está vacío o es demasiado breve."
    )


def test_tabla_entrada_proceso_salida():
    texto = apartados().get(2, "")
    assert filas_de_tabla(texto) >= 1, (
        "El apartado 2 debe incluir una tabla de entrada, proceso y salida."
    )


def test_casos_de_prueba():
    texto = apartados().get(4, "")
    filas = filas_de_tabla(texto)
    assert filas >= 4, f"El apartado 4 debe tener una tabla con al menos cuatro casos de prueba; hay {filas}."


def test_pseudocodigo_en_bloque_de_codigo():
    texto = apartados().get(5, "")
    bloques = re.findall(r"```[a-z]*\n(.*?)```", texto, flags=re.DOTALL)
    assert bloques, "El pseudocódigo del apartado 5 debe ir dentro de un bloque de código (```text ... ```)."
    lineas = [l for l in bloques[0].splitlines() if l.strip()]
    assert len(lineas) >= 6, "El pseudocódigo del apartado 5 parece incompleto (menos de seis líneas)."


def test_diagrama_de_flujo():
    texto = apartados().get(6, "")
    mermaid = re.search(r"```mermaid\n(.*?)```", texto, flags=re.DOTALL)
    if mermaid:
        codigo = mermaid.group(1)
        assert re.match(r"\s*(flowchart|graph)\b", codigo), "El bloque Mermaid debe empezar por «flowchart» o «graph»."
        assert codigo.count("-->") >= 6, "El diagrama Mermaid parece incompleto (menos de seis flechas)."
        return
    enlaces = re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", texto)
    assert enlaces, (
        "El apartado 6 debe enlazar la imagen del diagrama, por ejemplo ![Diagrama](diagramas/adivina.svg), "
        "o incluir un bloque de código mermaid."
    )
    for enlace in enlaces:
        ruta = RAIZ / enlace
        assert ruta.is_file(), f"La imagen enlazada «{enlace}» no existe en el repositorio."
        assert ruta.suffix.lower() in IMAGENES, f"«{enlace}» no es una imagen SVG, PNG o JPG."


def test_fuente_del_diagrama():
    texto = apartados().get(6, "")
    if "```mermaid" in texto:
        pytest.skip("El diagrama está en Mermaid dentro de DISENO.md: el propio código es la fuente.")
    fuentes = [p for p in DIAGRAMAS.glob("*") if p.suffix.lower() in FUENTES]
    assert fuentes, (
        "Falta el archivo fuente del diagrama en la carpeta diagramas (.excalidraw, .drawio o .mmd)."
    )


def test_fuentes_validas():
    for ruta in DIAGRAMAS.glob("*.excalidraw"):
        try:
            datos = json.loads(ruta.read_text(encoding="utf-8"))
        except (ValueError, UnicodeDecodeError):
            pytest.fail(f"«{ruta.name}» no es un archivo de Excalidraw válido (JSON).")
        assert datos.get("type") == "excalidraw", f"«{ruta.name}» no es un archivo de Excalidraw."
        assert datos.get("elements"), f"«{ruta.name}» no contiene ningún elemento."
    for ruta in DIAGRAMAS.glob("*.mmd"):
        codigo = ruta.read_text(encoding="utf-8")
        assert re.match(r"\s*(%%.*\n\s*)*(flowchart|graph)\b", codigo), (
            f"«{ruta.name}» debe empezar por «flowchart» o «graph»."
        )


def test_prueba_de_escritorio():
    filas = filas_de_tabla(apartados().get(7, ""))
    assert filas >= 3, f"La prueba de escritorio del apartado 7 debe tener al menos tres filas; hay {filas}."


def test_tabla_de_valoracion():
    filas = filas_de_tabla(apartados().get(8, ""))
    assert filas >= 2, "El apartado 8 debe incluir una tabla de valoración que compare las dos opciones."


def test_tabla_de_verificacion():
    texto = apartados().get(9, "")
    assert filas_de_tabla(texto) >= 4, (
        "El apartado 9 debe incluir una tabla con la construcción de Python de cada símbolo (al menos cuatro filas)."
    )


def test_historial():
    total = int(git("rev-list", "--count", "HEAD") or 0)
    propios = total - 1
    assert propios >= COMMITS_PROPIOS, (
        f"Se esperan al menos {COMMITS_PROPIOS} commits propios, repartidos a lo largo del trabajo; hay {propios}."
    )
