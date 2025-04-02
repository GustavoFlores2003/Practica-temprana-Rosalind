def probabilidad_dominante(k, m, n):
    """Calcula la probabilidad de obtener un descendiente con alelo dominante"""
    
    total = k + m + n  # Total de individuos

    # Probabilidad de seleccionar cada combinación de apareamiento
    P_AA_AA = (k / total) * ((k - 1) / (total - 1))  # AA × AA (100%)
    P_AA_Aa = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))  # AA × Aa (100%)
    P_AA_aa = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))  # AA × aa (100%)

    P_Aa_Aa = (m / total) * ((m - 1) / (total - 1)) * 0.75  # Aa × Aa (75%)
    P_Aa_aa = (m / total) * (n / (total - 1)) * 0.5 + (n / total) * (m / (total - 1)) * 0.5  # Aa × aa (50%)

    # No necesitamos calcular P(aa, aa) porque su probabilidad es 0
    probabilidad_total = P_AA_AA + P_AA_Aa + P_AA_aa + P_Aa_Aa + P_Aa_aa

    return round(probabilidad_total, 5)

# entrada para resolver caso
k, m, n = 30, 24, 30

# Imprimimos el resultado
print(probabilidad_dominante(k, m, n))  # Output esperado: 0.78333
