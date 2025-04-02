def fibonacci_rabbits(n, k):
    # Casos base
    if n == 1 or n == 2:
        return 1

    # Programación dinámica para almacenar los valores previos
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + k * dp[i - 2]

    return dp[n]

# Uso para resolver caso
n = 30  # Número de meses
k = 3  # Número de parejas que nacen por cada pareja reproductora
resultado = fibonacci_rabbits(n, k)
print(f"Total de parejas de conejos después de {n} meses: {resultado}")
