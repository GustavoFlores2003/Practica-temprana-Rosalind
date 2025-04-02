def calcular_esperanza_dominante(poblacion):
    probabilidades = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    return sum(p * 2 * prob for p, prob in zip(poblacion, probabilidades))

# Datos de entrada

datos = """
17683 17548 18535 17815 18680 16403
"""

# Procesamiento e impresión
for linea in datos.strip().splitlines():
    poblacion = list(map(int, linea.strip().split()))
    resultado = calcular_esperanza_dominante(poblacion)
    print(f"{resultado:.1f}")  # <Mostrar con 1 decimal

