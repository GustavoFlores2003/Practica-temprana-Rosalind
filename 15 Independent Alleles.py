from math import comb

def mendel_second_law(k, N):
    """
    Calcula la probabilidad de que al menos N organismos sean Aa Bb en la generación k.
    """
    total_descendientes = 2 ** k  # Número total de descendientes en la generación k
    p_AaBb = 1/4  # Probabilidad de que un hijo tenga el genotipo Aa Bb
    
    # Probabilidad acumulativa P(X >= N) = 1 - P(X < N)
    probabilidad = sum(comb(total_descendientes, i) * (p_AaBb ** i) * ((1 - p_AaBb) ** (total_descendientes - i)) 
                       for i in range(N))
    
    return round(1 - probabilidad, 3)  # Redondear a 3 decimales según el ejemplo

# Entrada y salida del caso
k, N = 6, 19
resultado = mendel_second_law(k, N)
print(resultado)  
