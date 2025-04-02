def mortal_fibonacci(n, m):
    """
    Calcula el número de pares de conejos después de n meses, considerando que viven exactamente m meses.
    """
    # Lista para representar las cohortes de conejos según su edad en este caso meses de vida
    poblacion = [0] * m
    poblacion[0] = 1  # Inicialmente hay 1 par de conejos recién nacidos
    
    for mes in range(1, n):
        nuevos_nacidos = sum(poblacion[1:])  # Solo conejos adultos (≥2 meses) se reproducen
        # Desplazar edades: los conejos envejecen
        for i in range(m - 1, 0, -1):
            poblacion[i] = poblacion[i - 1]
        poblacion[0] = nuevos_nacidos  # Asignar los nuevos nacimientos


    return sum(poblacion)  # Sumar todos los conejos vivos


# Entrada y ejecución en base al caso 
n, m = 94, 20
resultado = mortal_fibonacci(n, m)
print(resultado)
