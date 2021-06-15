import algoritmos

arr = [ 2, 3, 4, 10, 40 ]
x = 10

algorithm = int(input("Seleccione al algoritmo que desee usar(1. Busqueda lineal, 2. Busqueda binaria): "))

if algorithm == 1:
    result = algoritmos.linearSearch(arr, x)
    if(result == -1):
        print("El elemento no esta presente")
    else:
        print("El elemento esta presente en el indice", result)


elif algorithm == 2:
    result = algoritmos.binarySearch(arr, 0, len(arr)-1, x)
    if(result == -1):
        print("El elemento no esta presente)"
    else:
        print("El elemento esta presente en el indice", result)
