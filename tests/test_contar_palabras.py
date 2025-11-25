from importlib import util
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "venv"
    / "contador_palabras"
    / "contador.py"
)
spec = util.spec_from_file_location("contador_palabras.contador", MODULE_PATH)
assert spec and spec.loader  # defensa para mypy/linters
contador_mod = util.module_from_spec(spec)
spec.loader.exec_module(contador_mod)
contar_palabras = contador_mod.contar_palabras


def test_contar_palabras_con_puntuacion():
    texto = "Hola, mundo! Esto es una prueba: cuatro palabras más."
    assert contar_palabras(texto) == 10

