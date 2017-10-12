# Importar librería random
import random

# 1. Crear lista con silabario hiragana
# 2. Generar un número aleatorio (entero)
# 3. Imprimir entrada de la lista asociada al número generado en 2. 

hiragana = ["a", "i", "u", "e", "o"]
indice = random.randint(0, len(hiragana)-1)
print(hiragana[indice])
