#Ejercicio del caballo

movimientos = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]  # MOVIMIENTOS POSIBLES N=1

def posibles_movimientos(numero_actual, movimientos_restantes):
    if movimientos_restantes == 0:
        return 1  # Agotados los movimientos, por lo cual hay una posibilidad.
    else:
        posibilidades = 0
        for i in movimientos[numero_actual]:
            posibilidades += posibles_movimientos(i, movimientos_restantes - 1)
            '''
            Lo que hace es acceder a la lista de movimientos posibles (n=1) del numero actual como puede ser el 1,
            entra en esa sublista y coge el primer número como un movimiento, resta ese movimiento, tras ello accede a la sublista
            movimientos sobre ese numero cogido y así hasta que los movimientos restantes sean 0, en ese caso devuelve 1
            siendo esta una posible solución. Esto lo haría reiteradamente, ya que se trata de un bucle.

            '''
        return posibilidades

def numeros(n):
    posibilidades = [0] * 10
    for i in range(10):
        posibilidades[i] = posibles_movimientos(i, n)
    return posibilidades

n = 21
total = numeros(n)
print(total)
print(sum(total))
