def transcribir_adn_a_arn(cadena_adn):
    # Reemplazar todas las 'T' por 'U' para obtener la cadena de ARN
    cadena_arn = cadena_adn.replace('T', 'U')
    return cadena_arn

# Ejemplo de uso con el dataset de muestra
dna = "GATGGAACTTGACTACGTAAATT"
rna = transcribir_adn_a_arn(dna)

print("Cadena ARN transcrita:", rna)
