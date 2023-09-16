def amenazas(tablero, fila, columna):
    # Comprobamos si la columna está amenazada: diagonal superior, diagonal inferior y columna.
    for i in range(fila):
        if tablero[i] == columna or tablero[i] - i == columna - fila or tablero[i] + i == columna + fila:
            return False
    return True

def resolver_n_reinas(n):
    tablero = [0] * n  # TABLERO NxN
    soluciones_encontradas = 0

    def resolver_filaxfila(fila):
        nonlocal soluciones_encontradas 

        '''
        La función nonlocal permite acceder a una variable externa.
        '''

        if fila == n: #YA SE ENCONTRÓ UNA SOLUCIÓN
            soluciones_encontradas += 1
            return

        for columna in range(n):
            if amenazas(tablero, fila, columna) is True:
                tablero[fila] = columna
                resolver_filaxfila(fila + 1) #SIGUIENTE FILA

    resolver_filaxfila(0) # Iniciamos la recursividad desde la fila 0

    return soluciones_encontradas

n = 15
total_soluciones = resolver_n_reinas(n)
print(f"Total de soluciones para {n}-reinas: {total_soluciones}")
