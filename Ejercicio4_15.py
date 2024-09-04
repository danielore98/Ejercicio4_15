N = int(input("Escribe la dimension N>=2 del cuadrado a dibujar"))

#Escribe la primera linia de asteriscos
for i in range(N+1):
    print('* ', end="")

print()

#Dibuja las partes laterales
j = 1
while j <= N - 2:
    for k in range(N):
        if k == 0:
            print('* ', end="")
        elif k == N - 1:
            print('  *', end="")
        else:
            print('  ', end="")
    print()
    j += 1

#Fin del ciclo while.

i = 0
while i < N + 1:
    print('* ', end='')
    i += 1

#Fin del algoritmo