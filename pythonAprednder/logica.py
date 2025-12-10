# Ejercicios varios de lógica en Python, diccionarios, tuplas

"""
Crear una funcion que recibe una cadena de texto. Debe contar cuantas veces aparece la letra R y cuantas la J.
- Si las veces que aparece R y J son iguales, devuelve True
- Si no son iguales, devuelve False
-Si no aparece ninguna de las dos letras, devuelve True
"""

texto = "dnawRFRWFJEURJIEidhqnmoqm J J j j J jwirwd9qundwqd dnwudbwtryunerifijandrrr wadnuqwdui awuahdnaw"

def contar_letras (texto):
    # primero pasar todo a minusculas para no tener en cuenta mayusculas
    texto = texto.lower()

    # contamos las veces que aparece cada letra
    contador_R = texto.count("r")
    contador_J = texto.count("j")

    print(f"La letra R aparece {contador_R} veces")
    print(f"La letra J aparece {contador_J} veces")

    # if contador_R == 0 and contador_J == 0:
    #     return True
    # elif contador_R == contador_J:
    #     return True
    # else:
    #     return False
    return contador_J ==contador_R
# comentar varias lineas crtl +k + ctrl +c/u

Veredicto = contar_letras(texto)
print(Veredicto)
