def leer_fasta(texto):
    """
    Función para leer secuencias en formato FASTA y devolver un diccionario con {ID: secuencia}.
    """
    secuencias = {}       # Diccionario donde se guardarán las secuencias con su identificador
    identificador = ""   # Variable temporal para guardar el ID actual


    for linea in texto.split("\n"): # Se recorre línea por línea el texto
        linea = linea.strip()   # Se eliminan espacios en blanco
        if linea.startswith(">"): # Si la línea comienza con '>', es un nuevo ID
            identificador = linea[1:]   # Se guarda el ID sin el símbolo '>'
            secuencias[identificador] = ""  # Se inicializa la secuencia vacía
        else:
            secuencias[identificador] += linea  # Se va acumulando la secuencia para ese ID


    return secuencias


def construir_grafo_traslape(secuencias, k=3):
    """
    Construye el grafo de traslape para las secuencias dadas con prefijo/sufijo de longitud k.
    """
    nodos = list(secuencias.keys())  # Lista de identificadores (nombres de las secuencias)
    lista_adyacencia = [] # Lista de identificadores (nombres de las secuencias)


    for s in nodos:
        sufijo = secuencias[s][-k:]  # Últimos k caracteres
        for t in nodos:
            if s != t and secuencias[t][:k] == sufijo:  # Si `t` es diferente de `s` y su prefijo coincide
                lista_adyacencia.append((s, t)) # Se agrega la arista (s → t)


    return lista_adyacencia # Retorna la lista de adyacencia con todos los traslapes encontrados


def imprimir_lista_adyacencia(lista_adyacencia):
    """
    Imprime la lista de adyacencia en el formato requerido.
    """
    for s, t in lista_adyacencia:
        print(s, t)  # Imprime cada arista como "origen destino"


# Datos de entrada en formato FASTA
entrada_fasta = """>Rosalind_0964
TCCCTTAGCCGTTCCTCCAGCCCGTTCTGTAAACGCGGGGGGCGGCTAAGCGCTCCAATC
CGTGTAGATTCTAGGTGACAGTCCATAGTGTGCCA
>Rosalind_0970
CCTCGGCACCTATCAGCCTTCGCCAGAGTTTACGAGGCCGTATATGGTCAGGCGAGTGGG
ACTCAGGGCCTGTGTCAGGCCACCTCACTGGCCTTATT
>Rosalind_0476
ATCCAAGTCTAGCAGAGCAGGTAGGATGGGGCGGCCGCCGTCTCATTGCCCTTCACAGAG
ACAGTGCGTCAGTCTCGGCCTCCCCGCT
>Rosalind_2272
CTGCTCCACTACAGAAGATCGGCGGATCCTACTGTCAAAGTACTTTGACGAGCTAAGAAT
ATTAACCACATGGGAGTGGGCTTCTAATTGGAGTACACC
>Rosalind_2029
GACGTCAATGTCGATAAAGGATTACTACCGTTCAATTGCCGCTTACCGAGGATTAGATTC
CTATCGCTCTTTCCGGGACCAGGACCAAGTGAGG
>Rosalind_1303
ATATCGGATATAATTGGTACCTAAAGTAGGATCCGATACTTACGCCCGGCTTTCGTTTAT
CGCTTTCGTACAAATACCCGCACA
>Rosalind_7308
GTCCCTTGTGAGTATCCCCATACACCCAGAGTTATGAATTTCAAACACCAGGGCGGTCCA
CCTGAAAAATAATTCTACAGCGTCG
>Rosalind_0567
GTGTAAGCACCGTGCACGATGACAAGGATTGCCGAGTGATCCTTTCTTAAAAAAAATCTA
TTTCCTTTACACACTGTTATGCGTTTCATCTGTGGG
>Rosalind_4098
ACATTATGCTTATGAGTTTATAGTATGACTTAGAAATCACGACGGTTAGCAATGCAATAG
TGCAGCGACCTCGAGCGATCGAGTCCCGGGCTCTATGGAA
>Rosalind_0190
GATAGACGCAGGAGTGAACAAACAGGATTCGCCCAAAACGCTCTACATATTCGCGGGGCC
CCGCTTCGATGAAATCTGAGACATCG
>Rosalind_4122
TTGAGACGGCTTATAGGTTATCCGCAATCTGGTAGGATCATTTTTCAGGCCTCCTTTTGA
GGAGGCGTGGGTCATTGCCTGTGG
>Rosalind_7739
TAGATCCATACCATAAGATTCCCCTCGCCACGGGCAACCTGGCTAGAGGAGGCTAGGCTT
GGTATTTTAGTCCATGCTTCTCTAGGCTATGCGTTGCC
>Rosalind_5666
CTCGTGTCAAAGATCGCGCCGAATCGCTCGGACGAGTCCTCTCCTAGTTCGAGAAGGACG
TATATTTGACGGTCTGCGGAGACTCTC
>Rosalind_0518
TTCTGTTTTCCTTGATGGCAAGGGCAACCTGAAACTAGATGCCAATCGGACAACCGTCCC
GTGAGTGTCAAAAACCGCAGCGTGCTAAGGGCGG
>Rosalind_4159
ACCGCCGCGCAAAAGAAAGTGTCTTGTCCAAAATCCGATCGGCCGAGTAATAAGCAGGGT
CGGTAAGGTACTCGAGGTGGCTTCCAGTT
>Rosalind_0229
GGGTTCGAAAATATTAGTTCCTGGTACGATTCAGGCAAGATCAGTCCTCACAGGTCGTTC
TTAGCCTTCACGGGAATAAGTCGGCATTCCCGAAAAACG
>Rosalind_1726
CCATCCCTAGCCAGGGATCCCTGTCTTACGAATGGCAGAAAACGGGTACAGTTTTATTAC
CAGTCGATCGAACGTCCATGCGGATGTATAATCCTGGCTC
>Rosalind_2538
TACGGTGAGAGAGTAATCCGCAGCAATTGCCGAACTCTGCCCGTCTAGTTACTGTTTGCA
GGAGACTGTACAGGTTAACACCCGCTAGTTGAGGCC
>Rosalind_7450
TAGGTGTTGACGGTAAGGGTAATGTAACGGTGGCCTGTTATTCCCAGCTCGCCTACATGT
TACACCGAATAAGGATTTTTTCTCATC
>Rosalind_8696
CAGACCGCAACAGCAGGAAGCCCGGCAAACGCGGGCCGGTGGGCGCTACTCTCCGTGGCT
ATGCTCCTTTCTTTACGACCAAACTAGAC
>Rosalind_9649
TTCATCAGAAATACGGTAGTGTAATCAAAGTGTCAGCCTGTTCGGTCTCGGTGAGTTTCA
TGCAGGTGTGATTACCCCGCGCGAATG
>Rosalind_2252
AAATGTTGATGTACAGTACATCAAGACGAATTCCGCATCCATCCCTCGAGCCGTCAGATG
TTTGCACAGGACTAGGCAGTTTGTA
>Rosalind_2115
AGTGGTCTCGAAATGCTCAGATTCTCTGATTCCCATTTACTATAAGATATCTTCTCGCCT
GGCCGATTGATACTGCCAAACAGAATGATTAAGA
>Rosalind_0626
TATGGTTAGAGGACTTAGCTAGCGGAGACGTTTTCTAACATAATTGCAGAGTACACCACT
ACGGGAGCGCACCAGATATAA
>Rosalind_9301
CCATTACCCTTTGGCAAGTGGGGTCAGAGTCACTAAACAGCTATGATGGCGCGCTGCTTA
CAGTTATTTCCAATGGGCGT
>Rosalind_4271
GGACTCTGTATGACCTAAGAGTATTAACTGCCCTATGCAGACTACACCACGTCCCCCACA
CCCTCAAGTCGGCATTGATT
>Rosalind_5614
TTGACACGGGTCCATTTATGGAACCTGCGGGTATACCTAGGGTTGAAGCGGAGCACGACT
GCTCTACTGACCACTAATGCGAGG
>Rosalind_8391
ACCCTCGCATAAAACGACGAAGTAGGCCAGGTTGGGCTAGCCCGATAGGCCCCTCGACGT
TGAGACCGACCAGAGCTGTACTGAAGGCGCA
>Rosalind_6145
TCACTATCATAACATGATTATATCTACACCGAGCGGGTTCCCGGGTTGAGTAAAATCGAA
CGCTACCAGAATCCTCACCCGCCTAATGGGCAT
>Rosalind_6082
CCACGGCCAGAGTCTGCTGGAACTAGCACTAGTTAAGATTTGCTCCTCGCTACGAGATGG
CCTGGAGACTCCCGCTAGCCTTT
>Rosalind_5651
CAAAAGCGCTTGAGTTTTTGAGAGATGAGACTTCATTTAGTACCTTTCGTTTACCGGCGG
GCGTTGATCTTATGTCTGTATAATTTTAGG
>Rosalind_8193
TGGTGCGTCAGACGGAGAATTTTATGTCTCGCACTCCGTTCCACAGAGACTGCATTTTTC
GTCGATTAGTGGCATCCCACATTATG
>Rosalind_7758
CTTTGGTTTCATCTGGGCGGCATGTAGGCACTTGTCACTGATCAGGCTATGGTCCATAAT
GCAGTAGGTGATACCGCCCTGGGAGCA
>Rosalind_4586
GGTCTTTGTCAACGTCCAAGGTTCCACTAATCGCATTGGTTTGGAAATTGTACGCCCACC
AGCGCGGTGGACTTGAGATTCCCCAACAATCGACCCA
>Rosalind_1958
GGTCGGTCGTGCAAAATATTAATCTTTATTTTCTCGCGATCCACCGTGAATTCCCCCCCA
GCCAATAAAGCCAGTAAATCTGCTGAAGGTCGCG
>Rosalind_2080
TCACCCCCGCTCGTCACCAGGCTTGCCATATTATCGTAGCAATTAGGACAACCCCGGATC
GTTCGCGTTCCAGGTAGAATGTGCGGCAGTAGTCGGT
>Rosalind_7165
GTCGGGGCCAATAAGGATGCCACATAGAGCATGACGTAATCTTTGGTCCATCTTATCATT
CGGATGCCTGATTAATCGAAAATT
>Rosalind_3877
CTAGAAGCGCCCCTGATAACCTCTCGATCGTTCGCGCTAAACCCACGATGTGAGGTGCTT
AGAATTGAAATCAGCCCGGACTTACACCAACCCCTGCA
>Rosalind_8136
TGACAGAGCATACCTCTCAATGTCTCGTAAGATGTGCGCACGCCCCGATTCGCATCTCGT
TGTCCCACGGATGTCCGGACCTCTAA
>Rosalind_1963
CGATGCGGCGCAGACCGTAGTATGATATCTTTATACTGTTTCGGTTAAACCTTCGCCTAA
GATCACAAGAATACATGCAAGTT
>Rosalind_1388
ACTCGGGCGTCCCTTCCCGACGTTAGGCTCAGTTCGCCACATCAAAGCTAGGCCCCCGGA
CATCCGAGCTGGGACTTGGGCCGAACTTAGGGAC
>Rosalind_7195
GACTCAAATCCTCCCTACAATAGCAGCATGTAACACCGCCCCACTCAAACTGGCGATTGC
TTGCGACACTCGTGACGATTCAAAGATACACC
>Rosalind_1325
CTATGCTCAATCTGTACGAAGCCTTGGGCGCCAAGTACTAAATCGGAGCAAGTCTGGTTC
TGGCCTGAATGAGATTTCACAT
>Rosalind_5510
TCGAAGCTAGTTGCACCCCAAGATAGCAGAGTTTTCGAGCGTGCTCATTAACAGCGATGA
GGTTGCTTCGGATGAGGTGATCTGGGACCTAGTGAGG
>Rosalind_2780
AGAGCATGCTCCGAGGCGGCAGCCAGCGAGTATAGGAGTGATAAAAAGGTCGTAAGCATT
GCCAGTAAAAAAACCTCAAGACGTACCCGGCCTATTA
>Rosalind_5793
CAGTGTAAAGGGTGAAGGGACACATCCTCTGCGATTCGATTAGGAGTTGGGAGCTTTTAA
GAATCCCAAGTAGGATTTCTTTCGACTACA
>Rosalind_1515
CTCTAAAGTGCCCACAACCATACTGCTTAGTTGTAATACGGGAATCGTCCTGGCAAACAG
GTCGCGGATGGTGGGATCTAAGTCGTGGAGAATCTATATC
>Rosalind_8385
CTAGTGACGATCGGGCGAGCTGCTATTCGCTAGATCATTCGGTGAGCCAATTTTCTATCT
CACACCAATATTCCAGGGCCGCGA
>Rosalind_0132
GTTATACAAACCATCGCGGTTACAATTGACGTTGTGAGAACCCGGCGGGATTGTGTATCT
GTAGGAAGTCTGCTGTTGCCCACAAAC
>Rosalind_6021
GAACTAGGCGAATGAACCAAACACAACACTTCGATTCGTGCAAATGATAAAACATTTGAC
CCTATATGAGGAGTTAACTAGCGAAA
>Rosalind_7312
TTCCCCGCCAGTCTAGTTCTACATAGTGTTTTCGAAATGCACTTTGACATGGCACCGGTC
GGGGACACACTCTGGTCCTAAGTA
>Rosalind_0552
CGCGACATAAGCTACGGGATAACGCGGACATTGCGGCCGAGTGCACAAACATAGAATTGC
GGAAGTATAACGCTCTAGTGCGGTTCCAGGCAC
>Rosalind_3878
CACCGCTGAGCTGGGGCCTGTGGATAGCCTCTTGTTAATAAGCTAAAAGTCCCTCCTATA
GTGACTGGATAAGATGCCAGAATAA
>Rosalind_5264
ACAAATTACATACCACATGGGTACGTCTCTGTAATCGCTTGGGTGACTCAGGCATTTTGT
CGGGACTCGCTCCATTGGATTATCGTACT
>Rosalind_2174
CATTCTGAACCGAAGGTAACAAATTCCACCGTCAGATTTCATCGCAGATACGCAGCATTT
CTGAAACGATGCTTAAGTCCGTAGGAAAACGAGT
>Rosalind_7802
GCGTAGCGCCGTGACACGTATCCTCGCGTTATTACTTTCCAGTCGTGGGTCAGTCTGGGC
GGAGAGCCATGGCCGCAGGG
>Rosalind_8466
TTTGTGGATTACCAAGGGGTAAGAATCTAACTTGAACTGGAAACCTATACGGGGTCTCGG
ATATCCGAGCAGTATCGATGCGGGGAAGTAACG
>Rosalind_8242
AGCTCACAAGCTCTTTAAGGGTGCCATGTGTAAAAGGTTGCGTCAGGAAGCAGTCACAAT
TTTGGTAAAGCGGTCAGGAGGAATTCGTTACTGCAGTA
>Rosalind_1949
CGAGCACTACGTATTTTGGTTTTAAATCGGGCTAATGGTTCAGGGGCAAGTCACCGGCAA
TCATTCGTGAGTGAGAGTCCTAGAGCCGGGACGCAG
>Rosalind_2998
TTTTTTGAAGTATACGATCGGAGCGAGGGCCCTGATGCACGAGAGTTATACTTACAATTC
GGAATTTACAACTGTCTGGTAGGCCC
>Rosalind_1454
ACCAACAGTCCCTAATTCCTCCGGCTCAATGTGACGGGCTCTCTAAATTTATTGGGTTAT
TATTACTTGAGGCCTATGTTCTGCAACTTAATCTTCACG
>Rosalind_5822
CTGCTTTCCATGAAATTGGTCAATGTTTTTCGCGAACTCCGATTGCACACTCTCTTCAGA
GGCCGTAATGGTTAAGAGGGCATTTGCTAAGCAACC
>Rosalind_0823
TTAGTAGTGATACTGTCACTAGGTTTCGTCTCCCCAAGAACGCGGAAGTGGCGTCGCTAG
TGCAATGTCGCTGGATGCGAAGGAAGGGCGCCCA
>Rosalind_3684
GTATTTCATCGCGGCTGAGCTGTACCCCAGGGTGTACGGGGAAAGCCGACCTGGGATTTT
ACCTTCCCGCGCGTAAACACG
>Rosalind_2922
GTCGTCTGAAGACTGGGCGGTTCTCCTTACTCGTAGGGACAATCGTATTTCCGGTTTCAG
GTTCCGCTTAATATGCTTTAGTCCTGGGAAACG
>Rosalind_7150
TTATACGAGCGTACAAGAACTTGTTTTTGCGTTACGGACATTAGGTAATGTATATCCCAA
CCCTACCATGATTGAGTTGAGCAGCACGCCACTCCCAGC
>Rosalind_3678
ATTCACCTCTCCGTGTCACAGCGGAACCCTCATGAAACTGGATCGTCTTAGGCCCGTTAG
AGGGCAACCAAACCGACCTTGTACAAG
>Rosalind_5407
TCCTGTTGACTTGCCTTCAATTGAGCAGCTGCCCGTCGATCCATGAGCCTTATCCGTGCC
ACCCTTTGAAGTGCTGCTATAG
>Rosalind_8158
TTTAACCCTATAGATGTAGACCAGTAAGCCGGACGTCAACACCCTTGTCATGAATTTGTT
TCAAGCCAGAGCCGGTGTAGGACCATAATAACCTGGACCA
>Rosalind_2123
TTTTTTGGATAGCAAAAACCACACCACTCAGGGGTCGGCGAATCTAATAAACAGAAACAG
CCCTCTCGTCATGTAATTTACTTACTTGCCCGACTTCC
>Rosalind_1244
ATTACAAAGTTCACCGTGATGCGTATAACAGGGTACATGGAACCACCTGGTCGGGAGGCC
AATAAGGTTCGAATTACTTGTATCACTAT
>Rosalind_2526
CCTAGCATTCACACTCCCTGTCTCGACCAAGGAGGCCAATACTCGCCTCGCATGTTTGCG
CTGCATTAGGGAAAATTGTA
>Rosalind_9401
GGGGTATTCGGTGCTAGGGGTGTAAGTCATCAGTTGTTAGCGCTCTTATTGGTATGCCTT
GAACCTCAGGGCTGACCGTTGT
>Rosalind_2931
GCTAGTAAGGGAACGACTATATTTTTTAATATACCTGGTGACCTAGCTGAGCACCACGAT
CACACTCGTGTGGCTACTCT
>Rosalind_7703
ATGTTGAGATCCTCGGTTAACTCTTGGACTACCAACTGTTAGTAGCAAAATGGACCCCCC
TCGTGGTGTAATGGGCTACAAGT
>Rosalind_1222
ATTCATATTGCATCAGTAAGAGAAGTTTTGGAACGGCCCCTTAGGTCACTCGCCGCAAGA
TCGATCTGTCCCAACATTCTCTACTACCACGGCCTGTA
>Rosalind_9912
AGTTAACGTACAGTCACGTATTACTTGATCTACAACCGTCGAGCACAGGCAAGCCTCCCT
GAGAACAAATACGTGATAAAAGGAATGTCTGGGCG
>Rosalind_4273
ACATGCCAGTTATGCTTGCTTCCTAAACCCTTACTTCCCATGGGGAGTCCGTAACTTCAG
CTAAGAAACTCGTCGACCCTTTAAGAGATAC
>Rosalind_1666
CCATGGATGAGTCCGACATACCGCGCTTTGCAGAAGTGCGAGGGGTTTTTGTTTTTCAGA
CTCAGAAGATCACACATTCGAAGGCT
>Rosalind_3287
AAATGTCCGCCACACACTAGGAAGGAAGCCAGATCTAAGCGTAGAGACGTACCGGTTCTT
GACGTCACGGAGGGCAACCGCGTCAAG
>Rosalind_9787
ATGACGTGGACACAATGGAGTATTCGCCGGAACTCACGCACCATCGCTACTCCAGCGTGG
GGGCAGTGGTTCGCGAGCCGGTTGAAGCTCGCATCAGAGT
>Rosalind_6230
GTAGAGAGTCGCCTGACCCCCAAGTAGACCACAACCTTAGCGCTTCTAAGCATCAGCTCG
ATCTTTCCTGTCTCCTGTCC
>Rosalind_6901
CATCACTGAACGATCAATCAGGTTCTTGGTTGTCTCCAGTGACATTCATCGGATTCTAGT
CTAATAGATCGTCGACGCTCGCGGCCGCGGTG
>Rosalind_0116
CGGAGTAAGGAATGTTACTAAGCCGGATGCCACCACGTGCGGAAATATTTGGCTAGAAGA
TTGCCAATTGAAGAACTGGACGGTAC
>Rosalind_6278
GTCAAGACTAGAGTTGACCACGTGTCAGGGTAAGTCCACCAGAAATGCGGTTGCTATAGT
AACCTGATATTAATCGTACCC
>Rosalind_2068
TACGGGCCTCATAAGTCGGACCTCCCCTTGGTGGACCGGGGCCGGGTACAATAGCCCGGA
GAATCCCGCGCATGACCATTAGCCTGTTAGA
>Rosalind_4652
AAACCGGCACGACGATCCACACCATTTCAGAGCAGCTGCGAGGGCGTACATTCCACCACC
TTGTTGAAATCTAACATCAAGTACTATCCACCAGGCACG
>Rosalind_6498
TACGGGAGGGAGTCGGAAGTTGGCATGGTCTAGATGTGGACTGCCGCGGCACGGATACGT
TCAAAGGCTGATGACCCCGTATGAACC
>Rosalind_3700
CGGACAGGTTTGTCGCGTACTTGCATGGAGACGGAAGGGTGGGAAGCCTTTAAGCGCTTC
CCTATTAGATAGCAACTCTCAAACCTCCCCCACGAACGAT
>Rosalind_6346
TAAGCGAGTGGTGGGTCCCCTCGCTTCCGCAACCGCCCGTAGACAACGTGTATTCCGTGA
TGTGAATAGAAGTGGCGAGGACCGGCTGCC
>Rosalind_9322
ACGTGCGTAGCTCACGGAACCTTGGCGAGAGAGACGGCTTCGTCCTTTTGCGCTTTATAT
CAGGCTATCGTCGCCAAACAAGCATGCGTCTGATGGTACG
>Rosalind_2765
CAAACCTTACACTAGGTGGAGAGACAGGCATTTTCGTAAATGCGTGGCGCTCACCACCAT
TGCCCTAAAACGGCTGACTGTTGCTGGTTGT
>Rosalind_1421
TCCCTGGAGTCCTTGGGGTAACTCAGATTCCAAAAGCACCGCCTCATACGACTTTTGGAG
CGAGAATTCCATCGGACAACGAGCTCGAGCGAAAAAAG
>Rosalind_7525
CTCCGAGACGGCGCACGGTTCCCATTTTCTCGACAATAGATTCATGGTAGCCCTTACAAG
GGCTGCCTCAGCGGCAGCGGACG
>Rosalind_8356
TAAACAGCACCGAAATTCTTACTTGACGCACTCATTCGACGAGTGGCTGTCATAGCAAGA
GCTACTTGATTTTTGAATGC
>Rosalind_4814
AACATGCAGCTAGCCTAAGCGCACTCACGCCAAGACCCCAAATTGATGTGAGCTGGACCC
TTAAACGAGCCAGAGTTCCATTCGTGGTAAA
>Rosalind_3873
GCGCTTTCCCCGGTGTACACCGGCGTCACTGCAAGCGAGATCGGCTATCAATGCTAGTAG
ATAAATCTCTGTGGTTATGATGCCGGATTTTCG
>Rosalind_1521
CGCCCGTCTGGGATCATAGCTCCACGTGTTCCTCGAGAGGCAGCCCCCAAGTCAGCCGAT
AGGAGTGCTCGCTGTGTGGATCCTGCC
>Rosalind_3247
AGTCTGGCCAGTCCTGCTTTTGGCCACTTACTGGCCTTGACCAGTCTAAGCTTGGTCTAC
ACCTTCCTAATATTTGAAGTAATATATGAATAA
>Rosalind_9159
CACAACACGCGTGAAGTTCTACTGGTCTTGAGCGCCCTGCGTTTGCCCATTGACGCAACC
ATGATTCGAGAAGCCATCTGAACCTATCG"""


# Procesar datos
secuencias = leer_fasta(entrada_fasta) # Se leen las secuencias y se almacenan como {ID: secuencia}
grafo = construir_grafo_traslape(secuencias, k=3)  # Se construye el grafo de traslape con k=3


# Imprimir resultado
imprimir_lista_adyacencia(grafo)
